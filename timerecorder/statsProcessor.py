from datetime import timedelta
import time
import simpleaudio as sa

from . import config
from .ambiguousResultHandler import AmbiguousResultHandler
from .database import Database
from .databaseAccess import DatabaseAccess
from .databaseAccess import identify, AMBIGUOUS
from .gearTracker import GearTracker
from .inputTracker import InputTracker
from .log import getLogger
from .progressTracker import ProgressTracker
from .respawnTracker import RespawnTracker
from .speedTracker import SpeedTracker
from .timeTracker import TimeTracker
from .baseTracker import BaseTracker


goLineProgress = 0.0
completionProgress = 0.999

logger = getLogger(__name__)

class StatsProcessor():

    def __init__(self, approot):
        self.speed_unit = config.get.speed_unit
        self.speed_modifier = self.speed_unit == 'mph' and 0.6214 or 1
        self.approot = approot

        self.track = 0
        self.car = 0

        self.database = self.updateResources(approot)
        self.databaseAccess = DatabaseAccess(self.database)
        self.ambiguousResultHandler = AmbiguousResultHandler(self.databaseAccess, approot)

        self.userArray = self.database.initializeLaptimesDb()
        self.initTrackers()

    def updateResources(self, approot):
        database = Database(approot).setup()
        return database

    def formatTopSpeed(self):
        topSpeed_kmh = self.speedTracker.getTopSpeed() * 3.6
        return '%.1f' % (topSpeed_kmh * self.speed_modifier,)

    def formatLapTime(self, laptime):
        return '%.2f' % (laptime,)

    def prettyLapTime(self, laptime_seconds):
        fullDuration = str(timedelta(seconds=laptime_seconds))
        hours, minuteDuration = fullDuration.split(':', 1)
        thousandthsDuration = minuteDuration[:-3]
        return thousandthsDuration if hours == '0' else hours + ':' + thousandthsDuration

    def logResults(self, laptime, track, car, previousBest):
        logger.debug("%s.%s.%s.time:%s|s", self.userArray[0], track, car, self.formatLapTime(laptime))
        logger.debug("%s.%s.%s.topspeed:%s|%s", self.userArray[0], track, car, self.formatTopSpeed(), self.speed_unit)
        logger.info("Completed stage in %s.", self.prettyLapTime(laptime))
        
        # TODO #46 Only meaningful if car could be identified without heuristics...
        if previousBest is not None:
            previousBestTime = previousBest[1]
            logger.info("Beating previous best time of %s.", self.prettyLapTime(previousBestTime))

    def logTrack(self, trackId):
        trackName = self.database.getTrackName(trackId)
        logger.info("TRACK: %s", trackName)

    def logCar(self, carId):
        carName = self.database.getCarName(carId)
        logger.info("CAR: %s", carName)

    def showCarControlInformation(self):
        if identify(self.car) == AMBIGUOUS:
            for car in self.car:
                logger.info(self.databaseAccess.describeCarInterfaces(car))
        else:
            logger.info(self.databaseAccess.describeCarInterfaces(self.car))

    def allZeroStats(self, stats):
        return stats.count(0) == len(stats)

    def statsWithTelemetry(self, stats):
        return not self.allZeroStats(stats)

    def stageAborted(self):
        timeDelta = self.timeTracker.getTimeDelta()
        isAborted = self.respawnTracker.isRestart() or timeDelta < 0
        return isAborted

    def handleStats(self, stats):
        if self.statsWithTelemetry(stats):
            self.respawnTracker.track(stats)
            self.timeTracker.track(stats)
            self.progressTracker.track(stats)
            self.gearTracker.track(stats)
            self.speedTracker.track(stats)

            self.inputTracker.track(stats)

        lap = self.progressTracker.getLap()
        stageProgress = self.progressTracker.getProgress()

        self.handleGameState(self.stageAborted(), self.inStage(), lap, stageProgress, stats)

    def resetRecognition(self):
        self.track = 0
        self.car = 0
        self.initTrackers()

    def inStage(self):
        return self.track != 0 and self.car != 0

    def initTrackers(self):
        self.respawnTracker = RespawnTracker()
        self.timeTracker = TimeTracker()
        self.gearTracker = GearTracker(self.respawnTracker)
        self.progressTracker = ProgressTracker()
        self.speedTracker = SpeedTracker()
        self.inputTracker = InputTracker(self.speedTracker, self.playNotificationSound) if config.get.user_signals else BaseTracker()

    def startStage(self, stats):
        dbAccess = self.databaseAccess

        track_z = stats[6]
        track_length = self.progressTracker.getTrackLength()
        self.track = dbAccess.identifyTrack(track_z, track_length)
        trackId = identify(self.track)
        if trackId != AMBIGUOUS:
            self.logTrack(trackId)

        car_data = stats[63:66]  # max_rpm, idle_rpm, top_gear
        self.car = dbAccess.identifyCar(*tuple(car_data))
        carId = identify(self.car)
        if carId != AMBIGUOUS:
            self.logCar(carId)

        logger.debug("%s.%s.%s.started", self.userArray[0], trackId, carId)

        if config.get.show_car_controls:
            self.showCarControlInformation()

    def finishStage(self, stats):
        laptime = stats[62]
        timestamp = time.time()

        track, car = self.handleAmbiguities(timestamp)

        previousBest = self.databaseAccess.recordResults(track, car, timestamp, laptime, self.formatTopSpeed())
        self.logResults(laptime, track, car, previousBest)

    def handleAmbiguities(self, timestamp):
        car = self.ambiguousResultHandler.handleAmbiguousCars(timestamp, self.car, self.track, self.gearTracker, self.inputTracker)
        if identify(self.car) == AMBIGUOUS and identify(car) != AMBIGUOUS:
            self.logCar(car)

        track = self.ambiguousResultHandler.handleAmbiguousTracks(timestamp, car, self.track)

        return identify(track), identify(car)

    def finishedDR2TimeTrial(self, stats, trackProgess):
        return trackProgess >= completionProgress and self.allZeroStats(stats)

    def handleGameState(self, isAborted, inStage, lap, stageProgress, stats):
        if inStage and (lap == 1 or self.finishedDR2TimeTrial(stats, stageProgress)):
            self.finishStage(stats)
            self.resetRecognition()

        elif isAborted:
            self.resetRecognition()

        elif self.statsWithTelemetry(stats) and stageProgress <= goLineProgress and not inStage:
            self.startStage(stats)
            
    def playNotificationSound(self):
        try:
            waveObj = sa.WaveObject.from_wave_file('notify.wav')
            waveObj.play()
        except:
            logger.debug('Failed to play notification')

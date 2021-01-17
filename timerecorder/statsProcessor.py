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
        self.speed_unit = config.GET.speed_unit
        self.speed_modifier = 0.6214 if self.speed_unit == 'mph' else 1
        self.approot = approot

        self.track = 0
        self.car = 0

        self.database = self._updateResources(approot)
        self.databaseAccess = DatabaseAccess(self.database)
        self.ambiguousResultHandler = AmbiguousResultHandler(self.databaseAccess, approot)

        self.userArray = self.database.initializeLaptimesDb()
        self._initTrackers()

    def _updateResources(self, approot):
        database = Database(approot).setUp()
        return database

    def _formatTopSpeed(self):
        topSpeed_kmh = self.speedTracker.getTopSpeed() * 3.6
        return '{:.1f}'.format(topSpeed_kmh * self.speed_modifier)

    def _formatLapTime(self, laptime):
        return '{:.2f}'.format(laptime)

    def _prettyLapTime(self, laptime_seconds):
        fullDuration = str(timedelta(seconds=laptime_seconds))
        hours, minuteDuration = fullDuration.split(':', 1)
        thousandthsDuration = minuteDuration[:-3]
        return thousandthsDuration if hours == '0' else f'{hours}:{thousandthsDuration}'

    def _logResults(self, laptime, track, car, previousBestTime = None):
        logger.debug("%s.%s.%s.time:%s|s", self.userArray[0], track, car, self._formatLapTime(laptime))
        logger.debug("%s.%s.%s.topspeed:%s|%s", self.userArray[0], track, car, self._formatTopSpeed(), self.speed_unit)
        logger.info("Completed stage in %s.", self._prettyLapTime(laptime))

        if previousBestTime is not None:
            logger.info("Beating previous best time of %s.", self._prettyLapTime(previousBestTime))

    def _logTrack(self, trackId):
        trackName = self.database.getTrackName(trackId)
        logger.info("TRACK: %s", trackName)

    def _logCar(self, carId):
        carName = self.database.getCarName(carId)
        logger.info("CAR: %s", carName)

    def _showCarControlInformation(self):
        if identify(self.car) == AMBIGUOUS:
            for car in self.car:
                logger.info(self.databaseAccess.describeCarInterfaces(car))
        else:
            logger.info(self.databaseAccess.describeCarInterfaces(self.car))

    def _allZeroStats(self, stats):
        return stats.count(0) == len(stats)

    def _statsWithTelemetry(self, stats):
        return not self._allZeroStats(stats)

    def _stageAborted(self):
        timeDelta = self.timeTracker.getTimeDelta()
        isAborted = self.respawnTracker.isRestart() or timeDelta < 0
        return isAborted

    def handleStats(self, stats):
        if self._statsWithTelemetry(stats):
            self.respawnTracker.track(stats)
            self.timeTracker.track(stats)
            self.progressTracker.track(stats)
            self.gearTracker.track(stats)
            self.speedTracker.track(stats)

            self.inputTracker.track(stats)

        lap = self.progressTracker.getLap()
        stageProgress = self.progressTracker.getProgress()

        self._handleGameState(self._stageAborted(), self._inStage(), lap, stageProgress, stats)

    def resetRecognition(self):
        self.track = 0
        self.car = 0
        self._initTrackers()

    def _inStage(self):
        return self.track != 0 and self.car != 0

    def _initTrackers(self):
        self.respawnTracker = RespawnTracker()
        self.timeTracker = TimeTracker()
        self.gearTracker = GearTracker(self.respawnTracker)
        self.progressTracker = ProgressTracker()
        self.speedTracker = SpeedTracker()
        self.inputTracker = InputTracker(self.speedTracker, self._playNotificationSound) if config.GET.user_signals else BaseTracker()

    def _startStage(self, stats):
        dbAccess = self.databaseAccess

        track_z = stats[6]
        track_length = self.progressTracker.getTrackLength()
        self.track = dbAccess.identifyTrack(track_z, track_length)
        trackId = identify(self.track)
        if trackId != AMBIGUOUS:
            self._logTrack(trackId)

        car_data = stats[63:66]  # max_rpm, idle_rpm, top_gear
        self.car = dbAccess.identifyCar(*tuple(car_data))
        carId = identify(self.car)
        if carId != AMBIGUOUS:
            self._logCar(carId)

        logger.debug("%s.%s.%s.started", self.userArray[0], trackId, carId)

        if config.GET.show_car_controls:
            self._showCarControlInformation()

    def _finishStage(self, stats):
        laptime = stats[62]
        timestamp = time.time()

        track, car = self._handleAmbiguities(timestamp)
        previousBest = self.databaseAccess.recordResults(track, car, timestamp, laptime, self._formatTopSpeed())
        ambiguities = identify(self.car) == AMBIGUOUS or identify(self.track) == AMBIGUOUS

        if ambiguities or previousBest is None:
            self._logResults(laptime, track, car)
        else:
            previousBestTime = previousBest[1]
            self._logResults(laptime, track, car, previousBestTime)

    def _handleAmbiguities(self, timestamp):
        car = self.ambiguousResultHandler.handleAmbiguousCars(timestamp, self.car, self.track, self.gearTracker, self.inputTracker)
        if identify(self.car) == AMBIGUOUS and identify(car) != AMBIGUOUS:
            self._logCar(car)

        track = self.ambiguousResultHandler.handleAmbiguousTracks(timestamp, car, self.track)

        return identify(track), identify(car)

    def _finishedDR2TimeTrial(self, stats, trackProgess):
        return trackProgess >= completionProgress and self._allZeroStats(stats)

    def _handleGameState(self, isAborted, inStage, lap, stageProgress, stats):
        if inStage and (lap == 1 or self._finishedDR2TimeTrial(stats, stageProgress)):
            self._finishStage(stats)
            self.resetRecognition()

        elif isAborted:
            self.resetRecognition()

        elif self._statsWithTelemetry(stats) and stageProgress <= goLineProgress and not inStage:
            self._startStage(stats)

    def _playNotificationSound(self):
        try:
            waveObj = sa.WaveObject.from_wave_file('notify.wav')
            waveObj.play()
        except:
            logger.debug('Failed to play notification')

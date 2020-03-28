from .ambiguousResultHandler import AmbiguousResultHandler
from .database import Database
from .databaseAccess import DatabaseAccess
from .databaseAccess import identify
from .gearTracker import GearTracker
from .log import getLogger
from .progressTracker import ProgressTracker
from .respawnTracker import RespawnTracker
from .speedTracker import SpeedTracker
from .timeTracker import TimeTracker
from . import config
from .gearShiftHeuristics import GearShiftHeuristics
from .luckyGuessHeuristics import LuckyGuessHeuristics
import random
import time

goLineProgress = 0.0
completionProgress = 0.999

logger = getLogger(__name__)

# TODO Split off printing stuff
class StatsProcessor():

    def __init__(self, approot):
        self.speed_unit = config.get.speed_unit
        self.speed_modifier = self.speed_unit == 'mph' and 0.6214 or 1
        self.approot = approot
        
        self.track = 0
        self.car = 0

        self.ambiguousResultHandler = AmbiguousResultHandler(Database.laptimesDbName)
        self.database = self.updateResources(approot)

        self.databaseAccess = DatabaseAccess(self.database, self.ambiguousResultHandler)
        self.userArray = self.database.initializeLaptimesDb()
        self.initTrackers()

    def updateResources(self, approot):
        self.ambiguousResultHandler.cleanUp(approot)
        database = Database(approot).setup()
        return database

    def formatTopSpeed(self):
        topSpeed_kmh = self.speedTracker.getTopSpeed() * 3.6
        return '%.1f' % (topSpeed_kmh * self.speed_modifier,)

    def formatLapTime(self, laptime):
        return '%.2f' % (laptime,)

    def printResults(self, laptime, track, car):
        logger.debug("%s.%s.%s.time:%s|s", self.userArray[0], track, car, self.formatLapTime(laptime))
        logger.debug("%s.%s.%s.topspeed:%s|%s", self.userArray[0], track, car, self.formatTopSpeed(), self.speed_unit)
        logger.info("Completed stage in %ss.", self.formatLapTime(laptime))

    def showCarControlInformation(self):
        if isinstance(self.car, (list,)):
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

    def startStage(self, stats):
        dbAccess = self.databaseAccess

        track_z = stats[6]
        track_length = self.progressTracker.getTrackLength()
        self.track = dbAccess.identifyTrack(track_z, track_length)

        car_data = stats[63:66] # max_rpm, idle_rpm, top_gear
        self.car = dbAccess.identifyCar(*tuple(car_data))

        logger.debug("%s.%s.%s.started", self.userArray[0], identify(self.track), identify(self.car))

        # TODO #25 Still show in case of ambiguities?
        self.showCarControlInformation()

    def applyHeuristics(self, car_candidates):
        car_shift_map = self.databaseAccess.mapCarsToShifting(car_candidates)

        heuristics = GearShiftHeuristics(list(car_shift_map), self.gearTracker)
        # TODO The seed should only be fixed per program run, not always 0
        heuristics.withFallback(LuckyGuessHeuristics(car_candidates, random.seed(0)))
        
        return heuristics.guessCar()

    def instructUser(self, track, car, car_instruction, timestamp):
        if isinstance(car, (list, )):
            logger.info(car_instruction)
            self.databaseAccess.printCarUpdates(car, timestamp, track)
        if isinstance(track, (list, )):
            logger.info("Please run one of the scripts below to link the recorded laptime to the correct track:")
            self.databaseAccess.handleTrackUpdates(track, timestamp, car)

    def handleAmbiguities(self, timestamp):
        car_instruction = "Please run one of the scripts below to link the recorded laptime to the correct car:"
        track = self.track
        car = self.car
        
        # TODO #25 Needs to be opt-in per config.yaml
        if isinstance(car, list):
            logger.info("Guessing car...")
            guessed_car = self.applyHeuristics(car)
            if guessed_car is not None:
                self.databaseAccess.logCar(self.database.getCarName(guessed_car))
                car = guessed_car
                car_instruction = "If heuristics-based guess IS WRONG, RUN THE SCRIPT provided to fix the recorded car:"
        
        # TODO #25 Only create script for non-matching cars
        self.instructUser(track, self.car, car_instruction, timestamp)
        return identify(track), identify(car)

    def finishStage(self, stats):
        laptime = stats[62]

        timestamp = time.time()
        
        # TODO Debug
        logger.debug("TOTAL GEAR SHIFT/SKIP: %s/%s", self.gearTracker.getGearChangeCount(), self.gearTracker.getGearSkipCount())
        
        track, car = self.handleAmbiguities(timestamp)
        
        self.databaseAccess.recordResults(track, car, timestamp, laptime, self.formatTopSpeed())
        self.printResults(laptime, track, car)

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

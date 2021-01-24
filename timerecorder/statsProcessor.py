'''
More or less a state machine for the game, and really the heart of this tool
'''
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

GO_LINE_PROGRESS = 0.0
COMPLETION_PROGRESS = 0.999

logger = getLogger(__name__)

class StatsProcessor():

    def __init__(self, approot):
        self.speed_unit = config.GET.speed_unit
        self.speed_modifier = 0.6214 if self.speed_unit == 'mph' else 1
        self.approot = approot

        self.track = 0
        self.car = 0

        self.database = self._updateResources(approot)
        self.database_access = DatabaseAccess(self.database)
        self.ambiguous_result_handler = AmbiguousResultHandler(self.database_access, approot)

        self.user_array = self.database.initializeLaptimesDb()
        self._initTrackers()

    def _updateResources(self, approot):
        database = Database(approot).setUp()
        return database

    def _formatTopSpeed(self):
        topSpeedKmh = self.speed_tracker.getTopSpeed() * 3.6
        return '{:.1f}'.format(topSpeedKmh * self.speed_modifier)

    def _formatLapTime(self, laptime):
        return '{:.2f}'.format(laptime)

    def _prettyLapTime(self, laptimeSeconds):
        fullDuration = str(timedelta(seconds=laptimeSeconds))
        hours, minuteDuration = fullDuration.split(':', 1)
        thousandthsDuration = minuteDuration[:-3]
        return thousandthsDuration if hours == '0' else f'{hours}:{thousandthsDuration}'

    def _logResults(self, laptime, track, car, previousBestTime=None):
        logger.debug("%s.%s.%s.time:%s|s", self.user_array[0], track, car, self._formatLapTime(laptime))
        logger.debug("%s.%s.%s.topspeed:%s|%s", self.user_array[0], track, car, self._formatTopSpeed(), self.speed_unit)
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
                logger.info(self.database_access.describeCarInterfaces(car))
        else:
            logger.info(self.database_access.describeCarInterfaces(self.car))

    def _allZeroStats(self, stats):
        return stats.count(0) == len(stats)

    def _statsWithTelemetry(self, stats):
        return not self._allZeroStats(stats)

    def _stageAborted(self):
        timeDelta = self.time_tracker.getTimeDelta()
        isAborted = self.respawn_tracker.isRestart() or timeDelta < 0
        return isAborted

    def handleStats(self, stats):
        if self._statsWithTelemetry(stats):
            self.respawn_tracker.track(stats)
            self.time_tracker.track(stats)
            self.progress_tracker.track(stats)
            self.gear_tracker.track(stats)
            self.speed_tracker.track(stats)

            self.input_tracker.track(stats)

        lap = self.progress_tracker.getLap()
        stageProgress = self.progress_tracker.getProgress()

        self._handleGameState(self._stageAborted(), self._inStage(), lap, stageProgress, stats)

    def resetRecognition(self):
        self.track = 0
        self.car = 0
        self._initTrackers()

    def _inStage(self):
        return self.track != 0 and self.car != 0

    def _initTrackers(self):
        self.respawn_tracker = RespawnTracker()
        self.time_tracker = TimeTracker()
        self.gear_tracker = GearTracker(self.respawn_tracker)
        self.progress_tracker = ProgressTracker()
        self.speed_tracker = SpeedTracker()
        self.input_tracker = InputTracker(self.speed_tracker, self._playNotificationSound) if config.GET.user_signals else BaseTracker()

    def _startStage(self, stats):
        dbAccess = self.database_access

        trackZ = stats[6]
        trackLength = self.progress_tracker.getTrackLength()
        self.track = dbAccess.identifyTrack(trackZ, trackLength)
        trackId = identify(self.track)
        if trackId != AMBIGUOUS:
            self._logTrack(trackId)

        carData = stats[63:66]  # max_rpm, idle_rpm, top_gear
        self.car = dbAccess.identifyCar(*tuple(carData))
        carId = identify(self.car)
        if carId != AMBIGUOUS:
            self._logCar(carId)

        logger.debug("%s.%s.%s.started", self.user_array[0], trackId, carId)

        if config.GET.show_car_controls:
            self._showCarControlInformation()

    def _finishStage(self, stats):
        laptime = stats[62]
        timestamp = time.time()

        track, car = self._handleAmbiguities(timestamp)
        previousBest = self.database_access.recordResults(track, car, timestamp, laptime, self._formatTopSpeed())
        ambiguities = identify(self.car) == AMBIGUOUS or identify(self.track) == AMBIGUOUS

        if ambiguities or previousBest is None:
            self._logResults(laptime, track, car)
        else:
            previousBestTime = previousBest[1]
            self._logResults(laptime, track, car, previousBestTime)

    def _handleAmbiguities(self, timestamp):
        car = self.ambiguous_result_handler.handleAmbiguousCars(timestamp, self.car, self.track, self.gear_tracker, self.input_tracker)
        if identify(self.car) == AMBIGUOUS and identify(car) != AMBIGUOUS:
            self._logCar(car)

        track = self.ambiguous_result_handler.handleAmbiguousTracks(timestamp, car, self.track)

        return identify(track), identify(car)

    def _finishedDR2TimeTrial(self, stats, trackProgess):
        return trackProgess >= COMPLETION_PROGRESS and self._allZeroStats(stats)

    def _handleGameState(self, isAborted, inStage, lap, stageProgress, stats):
        if inStage and (lap == 1 or self._finishedDR2TimeTrial(stats, stageProgress)):
            self._finishStage(stats)
            self.resetRecognition()

        elif isAborted:
            self.resetRecognition()

        elif self._statsWithTelemetry(stats) and stageProgress <= GO_LINE_PROGRESS and not inStage:
            self._startStage(stats)

    def _playNotificationSound(self):
        try:
            waveObj = sa.WaveObject.from_wave_file('notify.wav')
            waveObj.play()
        except:  #pylint: disable=bare-except
            logger.debug('Failed to play notification')

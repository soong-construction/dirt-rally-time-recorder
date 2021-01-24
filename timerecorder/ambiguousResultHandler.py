'''
This will handle ambiguities in observed telemetry, e.g. by applying heuristics
'''
import random

from . import config
from .gearShiftHeuristics import GearShiftHeuristics
from .luckyGuessHeuristics import LuckyGuessHeuristics
from .userSignalsHeuristics import UserSignalsHeuristics
from .log import getLogger, getProjectUrl
from .updateScriptHandler import UpdateScriptHandler
from .database import Database

logger = getLogger(__name__)

INSTRUCTION = "Please run one of the scripts below to link the recorded laptime to %s:"

class AmbiguousResultHandler():

    def __init__(self, databaseAccess, approot):
        self.database_access = databaseAccess
        self.update_script_handler = UpdateScriptHandler(Database.laptimesDbName)
        self.update_script_handler.cleanUp(approot)

        self.seed = random.randrange(1000)

    def _applyHeuristics(self, carCandidates, gearTracker, inputTracker):
        heuristics = LuckyGuessHeuristics(carCandidates, self.seed)

        if config.GET.authentic_shifting:
            carShiftMap = self.database_access.mapCarsToShifting(carCandidates)
            gearShiftHeuristics = GearShiftHeuristics(list(carShiftMap), gearTracker)
            gearShiftHeuristics.withFallback(heuristics)
            heuristics = gearShiftHeuristics

        if config.GET.user_signals:
            userSignalHeuristics = UserSignalsHeuristics(carCandidates, inputTracker)
            userSignalHeuristics.withFallback(heuristics)
            heuristics = userSignalHeuristics

        return heuristics.guessCar()

    def _logFailedRecognition(self, incompleteUpdate, logLine):
        logger.error(logLine)
        logger.debug(incompleteUpdate)

    def handleAmbiguousCars(self, timestamp, car, track, gearTracker, inputTracker):
        if isinstance(car, int):
            return car

        if len(car) == 0:
            incompleteUpdate = Database.getCarUpdateStatements(timestamp, ['???'])[0]

            self._logFailedRecognition(incompleteUpdate, f'Unmapped car telemetry. Please report at {getProjectUrl()}')
            return car

        if config.GET.heuristics_activated:
            guessedCar = self._applyHeuristics(car, gearTracker, inputTracker)

            if guessedCar is not None:
                logger.info("If heuristics-based guess IS WRONG, RUN THE SCRIPT provided to fix the recorded car:")
                dismissedCars = [c for c in car if c != guessedCar]
                self.database_access.handleCarUpdates(dismissedCars, timestamp, track, self._handleUpdate)
                return guessedCar

        logger.info(INSTRUCTION, "the correct car")
        self.database_access.handleCarUpdates(car, timestamp, track, self._handleUpdate)

        return car

    def handleAmbiguousTracks(self, timestamp, car, track):
        if isinstance(track, int):
            return track

        if len(track) == 0:
            incompleteUpdate = Database.getTrackUpdateStatements(timestamp, ['???'])[0]

            self._logFailedRecognition(incompleteUpdate, f'Unmapped track telemetry. Please report at {getProjectUrl()}')
            return track

        logger.info(INSTRUCTION, "the correct track")
        self.database_access.handleTrackUpdates(track, timestamp, car, self._handleUpdate)

        return track

    def _handleUpdate(self, trackName, carName, timestamp, update):
        scriptName = self.update_script_handler.writeScript(trackName, carName, timestamp, update)
        logger.info(" ==> %s", scriptName)

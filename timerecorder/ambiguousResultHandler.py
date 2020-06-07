import random

from . import config
from .gearShiftHeuristics import GearShiftHeuristics
from .luckyGuessHeuristics import LuckyGuessHeuristics
from .userSignalsHeuristics import UserSignalsHeuristics
from .log import getLogger
from .databaseAccess import identify
from .updateScriptHandler import UpdateScriptHandler
from .database import Database

logger = getLogger(__name__)

instruction = "Please run one of the scripts below to link the recorded laptime to %s:"

class AmbiguousResultHandler():
    
    def __init__(self, databaseAccess, approot):
        self.databaseAccess = databaseAccess
        self.updateScriptHandler = UpdateScriptHandler(Database.laptimesDbName)
        self.updateScriptHandler.cleanUp(approot)

        self.seed = random.randrange(1000)
    
    def applyHeuristics(self, car_candidates, gearTracker, inputTracker):
        heuristics = LuckyGuessHeuristics(car_candidates, random.seed(self.seed))
        
        if config.get.authentic_shifting:
            car_shift_map = self.databaseAccess.mapCarsToShifting(car_candidates)
            gearShiftHeuristics = GearShiftHeuristics(list(car_shift_map), gearTracker)
            gearShiftHeuristics.withFallback(heuristics)
            heuristics = gearShiftHeuristics
            
        if config.get.user_signals:
            userSignalHeuristics = UserSignalsHeuristics(car_candidates, inputTracker)
            userSignalHeuristics.withFallback(heuristics)
            heuristics = userSignalHeuristics
        
        return heuristics.guessCar()

    def handleAmbiguousCars(self, timestamp, car, track, gearTracker, inputTracker):
        if isinstance(car, int):
            return car
        
        if config.get.heuristics_activated:
            guessed_car = self.applyHeuristics(car, gearTracker, inputTracker)
            
            if guessed_car is not None:
                logger.info("If heuristics-based guess IS WRONG, RUN THE SCRIPT provided to fix the recorded car:")
                dismissedCars = [c for c in car if c != guessed_car]
                self.databaseAccess.handleCarUpdates(dismissedCars, timestamp, track, self.handleUpdate)
                return guessed_car

        logger.info(instruction, "the correct car")
        self.databaseAccess.handleCarUpdates(car, timestamp, track, self.handleUpdate)

        return car
    
    def handleAmbiguousTracks(self, timestamp, car, track):
        if isinstance(track, list):
            logger.info(instruction, "the correct track")
            self.databaseAccess.handleTrackUpdates(track, timestamp, car, self.handleUpdate)
        
        return track

    def handleAmbiguities(self, timestamp, car, track):
        car = self.handleAmbiguousCars(timestamp, car, track)
        track = self.handleAmbiguousTracks(timestamp, car, track)

        return identify(track), identify(car)

    def handleUpdate(self, trackName, carName, timestamp, update):
        scriptName = self.updateScriptHandler.writeScript(trackName, carName, timestamp, update)
        logger.info(" ==> %s", scriptName)

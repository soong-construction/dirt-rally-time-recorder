from timerecorder.log import getLogger
from timerecorder.inputTracker import Signal

logger = getLogger(__name__)

# TODO Abstract base class: guessCar, withFallback, isApplicable
class UserSignalsHeuristics():
    
    def __init__(self, car_candidates, inputTracker): 
        self.car_candidates = car_candidates
        self.inputTracker = inputTracker
        
    def withFallback(self, heuristics):  
        self.fallback = heuristics
    
    def guessCar(self):
        userSignal = self.inputTracker.getSignal()
        
        applicable = len(self.car_candidates) <= 2
        if not applicable:
            # TODO Invert: info log applied heuristics
            logger.debug('USER SIGNALS not applicable')
            return

        if userSignal is None:
            guess = self.fallback.guessCar()
            # TODO Advise signal for car
            return guess
        
        logger.info('Applying user signals')
        if userSignal is Signal.THROTTLE_LEFT:
            guess = self.car_candidates[0]
        elif userSignal is Signal.THROTTLE_RIGHT:
            guess = self.car_candidates[1]
        else:
            raise Exception('Unknown signal ' + userSignal)
        
        return guess
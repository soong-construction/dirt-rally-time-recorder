from .log import getLogger
from .inputTracker import Signal
from .heuristics import Heuristics

logger = getLogger(__name__)

class UserSignalsHeuristics(Heuristics):
    
    def __init__(self, car_candidates, inputTracker):
        Heuristics.__init__(self)
        self.car_candidates = car_candidates
        self.userSignal = inputTracker.getSignal()

    def isApplicable(self):
        return len(self.car_candidates) <= 2 and self.userSignal

    def apply(self):
        if self.userSignal is Signal.THROTTLE_LEFT:
            guess = self.car_candidates[0]
        elif self.userSignal is Signal.THROTTLE_RIGHT:
            guess = self.car_candidates[1]
        else:
            raise Exception('Unknown signal ' + self.userSignal)
        
        return guess
    
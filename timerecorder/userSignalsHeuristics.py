'''
Special heuristics, cf. docs
'''
from .log import getLogger
from .inputTracker import Signal
from .heuristics import Heuristics

logger = getLogger(__name__)

class UserSignalsHeuristics(Heuristics):

    def __init__(self, carCandidates, inputTracker):
        Heuristics.__init__(self)
        self.car_candidates = carCandidates
        self.user_signal = inputTracker.getSignal()

    def isApplicable(self):
        return len(self.car_candidates) <= 2 and self.user_signal

    def apply(self):
        if self.user_signal is Signal.THROTTLE_LEFT:
            guess = self.car_candidates[0]
        elif self.user_signal is Signal.THROTTLE_RIGHT:
            guess = self.car_candidates[1]
        else:
            raise Exception(f'Unknown signal {self.user_signal}')

        return guess

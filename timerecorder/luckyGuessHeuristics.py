'''
A simple heuristics, cf. docs
'''
import random as r
from .log import getLogger
from .heuristics import Heuristics

logger = getLogger(__name__)

class LuckyGuessHeuristics(Heuristics):

    def __init__(self, carCandidates, random=r):
        Heuristics.__init__(self)
        self.car_candidates = carCandidates
        self.random = random

    def isApplicable(self):
        return len(self.car_candidates) <= 3

    def apply(self):
        # FIXME Should use self.random, but then passing random.seed fails
        index = r.randrange(0, len(self.car_candidates))
        car = self.car_candidates[index]

        return car

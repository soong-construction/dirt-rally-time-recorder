'''
A simple heuristics, cf. docs
'''
import random
from .log import getLogger
from .heuristics import Heuristics

logger = getLogger(__name__)

class LuckyGuessHeuristics(Heuristics):

    def __init__(self, carCandidates, seed):
        Heuristics.__init__(self)
        self.car_candidates = carCandidates
        self.seed = seed

    def isApplicable(self):
        return len(self.car_candidates) <= 3

    def apply(self):
        random.seed(self.seed)
        index = random.randrange(0, len(self.car_candidates))
        car = self.car_candidates[index]

        return car

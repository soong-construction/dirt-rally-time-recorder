import random
from .log import getLogger
from .heuristics import Heuristics

logger = getLogger(__name__)

class LuckyGuessHeuristics(Heuristics):
    
    def __init__(self, car_candidates, random = random):
        Heuristics.__init__(self)
        self.car_candidates = car_candidates
        self.random = random
        
    def isApplicable(self):
        return len(self.car_candidates) <= 3

    def apply(self):
        index = random.randrange(0, len(self.car_candidates))
        car = self.car_candidates[index]
        
        return car

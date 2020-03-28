import random
from .log import getLogger

logger = getLogger(__name__)

class LuckyGuessHeuristics:
    
    def __init__(self, car_candidates, random = random):
        self.car_candidates = car_candidates
        self.random = random
        
    def guessCar(self):
        index = random.randrange(0, len(self.car_candidates))

        applicable = len(self.car_candidates) <= 3

        if not applicable:
            logger.debug('LUCKY GUESS not applicable')
            return

        car = self.car_candidates[index]
        
        return car

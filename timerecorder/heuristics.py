from abc import abstractmethod, ABC
from .log import getLogger

logger = getLogger(__name__)

class Heuristics(ABC):

    def __init__(self):
        self.fallback = None

    def withFallback(self, heuristics):
        self.fallback = heuristics

    def guessCar(self):
        if self.isApplicable():
            logger.info('Applying %s...', type(self).__name__)
            return self.apply()

        if self.fallback:
            return self.fallback.guessCar()

        return None

    @abstractmethod
    def apply(self):
        pass

    @abstractmethod
    def isApplicable(self):
        pass

from .log import getLogger, VERBOSE
from .baseTracker import BaseTracker

logger = getLogger(__name__)

class GearTracker(BaseTracker):

    def __init__(self, respawnTracker):
        self.respawn_tracker = respawnTracker
        self.last_gear = None
        self.change_count = 0
        self.skip_count = 0

    def checkGearChanged(self, currentGear):
        if currentGear != self.last_gear:
            self.change_count += 1

    def checkGearSkipped(self, currentGear):
        distance = self.last_gear - currentGear
        if abs(distance) > 1:
            self.skip_count += 1
            logger.log(VERBOSE, 'GEAR SKIPPED: %s -> %s', self.last_gear, currentGear)

    def track(self, stats):
        currentGear = stats[33]
        # Ignore neutral = 0
        if currentGear == 0:
            return

        # Handle reverse gear = -1 (DR1: 10.0)
        if currentGear in (-1, 10):
            currentGear = 0

        respawn = self.respawn_tracker.isRecover() or self.respawn_tracker.isRestart()

        if not (respawn or self.last_gear is None):
            self.checkGearChanged(currentGear)
            self.checkGearSkipped(currentGear)

        self.last_gear = currentGear

    def getGearChangeCount(self):
        return self.change_count

    def getGearSkipCount(self):
        return self.skip_count

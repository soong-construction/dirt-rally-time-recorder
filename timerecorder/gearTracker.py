from .log import getLogger, VERBOSE

logger = getLogger(__name__)

class GearTracker():

    def __init__(self, respawnTracker):
        self.respawnTracker = respawnTracker
        self.lastGear = None
        self.changeCount = 0
        self.skipCount = 0

    def checkGearChanged(self, current_gear):
        if current_gear != self.lastGear:
            self.changeCount += 1

    def checkGearSkipped(self, current_gear):
        distance = self.lastGear - current_gear
        if abs(distance) > 1:
            self.skipCount += 1
            logger.log(VERBOSE, 'GEAR SKIPPED: %s -> %s', self.lastGear, current_gear)

    def track(self, stats):
        current_gear = stats[33]
        # Ignore neutral = 0
        if current_gear == 0:
            return

        # Handle reverse gear = -1 (DR1: 10.0)
        if current_gear == -1 or current_gear == 10:
            current_gear = 0

        respawn = self.respawnTracker.isRecover() or self.respawnTracker.isRestart()
        
        if not (respawn or self.lastGear is None):
            self.checkGearChanged(current_gear)
            self.checkGearSkipped(current_gear)

        self.lastGear = current_gear

    def getGearChangeCount(self):
        return self.changeCount

    def getGearSkipCount(self):
        return self.skipCount
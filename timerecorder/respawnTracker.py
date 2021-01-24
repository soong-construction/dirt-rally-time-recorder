'''
Tries to detect sudden changes in car position, e.g. when spawning at the stage start
'''
from .baseTracker import BaseTracker
from .log import getLogger

logger = getLogger(__name__)

# Should handle most respawns, except successive recovers in one place (only DR1)
class RespawnTracker(BaseTracker):

    def __init__(self):
        self.last_x = None
        self.last_y = None
        self.recover = False
        self.restart = False

    def updatePos(self, posX, posY):
        self.last_x = posX
        self.last_y = posY

    def positionDeltaExceeds(self, posX, posY, delta):
        exceedsX = abs(posX - self.last_x) >= delta
        exceedsY = abs(posY - self.last_y) >= delta

        return exceedsX or exceedsY

    def track(self, stats):
        self.recover = False
        self.restart = False
        recoverDelta = 2
        restartDelta = 30
        restartDistance = 10

        posX = stats[4]
        posY = stats[5]
        distance = stats[2]

        if self.last_x is None:
            pass

        elif self.positionDeltaExceeds(posX, posY, restartDelta) and distance <= restartDistance:
            self.restart = True
            logger.debug('RESTART')

        elif self.positionDeltaExceeds(posX, posY, recoverDelta):
            self.recover = True
            logger.debug('RECOVER')

        self.updatePos(posX, posY)

    def isRecover(self):
        return self.recover

    def isRestart(self):
        return self.restart

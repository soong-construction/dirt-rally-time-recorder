from log import getLogger

recoverDelta = 2
restartDelta = 30
restartDistance = 10

logger = getLogger(__name__)

# Should handle most respawns, except successive recovers in one place (only DR1)
class RespawnTracker():
    
    def __init__(self):
        self.last_x = None
        self.last_y = None
        self.recover = False
        self.restart = False

    def updatePos(self, pos_x, pos_y):
        self.last_x = pos_x
        self.last_y = pos_y

    def positionDeltaExceeds(self, pos_x, pos_y, delta):
        exceeds_x = abs(pos_x - self.last_x) >= delta
        exceeds_y = abs(pos_y - self.last_y) >= delta
        
        return exceeds_x or exceeds_y

    def track(self, stats):
        self.recover = False
        self.restart = False
        pos_x = stats[4]
        pos_y = stats[5]
        distance = stats[2]
        
        if self.last_x is None:
            pass
        
        elif self.positionDeltaExceeds(pos_x, pos_y, restartDelta) and distance <= restartDistance:
            self.restart = True
            logger.debug('RESTART')
                
        elif self.positionDeltaExceeds(pos_x, pos_y, recoverDelta):  
            self.recover = True
            logger.debug('RECOVER')

        self.updatePos(pos_x, pos_y)
        
    def isRecover(self):
        return self.recover
    
    def isRestart(self):
        return self.restart

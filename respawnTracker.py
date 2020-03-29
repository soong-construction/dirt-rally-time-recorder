
# Should handle most respawns, except successive recovers in one place (only DR1)
# TODO test
class RespawnTracker():
    recoverDelta = 2
    restartDelta = 30
    
    def __init__(self):
        self.last_x = None
        self.last_y = None

    def updatePos(self, pos_x, pos_y):
        self.last_x = pos_x
        self.last_y = pos_y

    def track(self, stats):
        self.recover = False
        self.restart = False
        pos_x = stats[4]
        pos_y = stats[5]
        
        if self.last_x is None:
            pass
        elif abs(pos_x - self.last_x) > self.restartDelta or abs(pos_y - self.last_y) > self.restartDelta:  
            self.restart = True
            print('[RESTART]')
        elif abs(pos_x - self.last_x) > self.recoverDelta or abs(pos_y - self.last_y) > self.recoverDelta:  
            self.recover = True
            print('[RECOVER]')

        self.updatePos(pos_x, pos_y)
        
    def isRecover(self):
        return self.recover
    
    def isRestart(self):
        return self.restart

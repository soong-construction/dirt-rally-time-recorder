# Field Time is not reset when restarting events (but for: new/proceeding events, second runs on PP).
class TimeTracker():
    
    def __init__(self):
        self.time = 0
        self.previousTime = None

    def track(self, stats):
        self.previousTime = self.time
        self.time = stats[0]
            
    def getTimeDelta(self):
        if self.previousTime is None:
            return 0
        return self.time - self.previousTime

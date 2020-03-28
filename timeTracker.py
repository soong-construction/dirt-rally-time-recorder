class TimeTracker():
    
    def __init__(self):
        self.time = None
        self.previousTime = None

    def track(self, stats):
        self.previousTime = self.time
        self.time = stats[0]
            
    def getTime(self):
        return self.time

    def getPreviousTime(self):
        return self.previousTime
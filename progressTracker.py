class ProgressTracker():
    
    def __init__(self):
        self.distance = None
        self.track_length = None

    def track(self, stats):
        self.distance = stats[2]
        self.track_length = stats[61]
        self.lap = stats[59]
            
    def getTrackLength(self):
        return self.track_length

    def hasData(self):
        return self.track_length is not None and self.distance is not None

    def getProgress(self):
        if self.hasData():
            return self.distance / self.track_length
        
        return None
    
    def getLap(self):
        return self.lap
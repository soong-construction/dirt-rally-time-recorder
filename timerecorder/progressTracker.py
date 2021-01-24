'''
Tracks progress through a stage
'''
from .baseTracker import BaseTracker

class ProgressTracker(BaseTracker):

    def __init__(self):
        self.distance = None
        self.track_length = None
        self.lap = None

    def track(self, stats):
        self.distance = stats[2]
        self.lap = stats[59]

        if self.track_length is None:
            self.track_length = stats[61]

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

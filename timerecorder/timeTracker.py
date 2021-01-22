'''
Essential time tracking.
Note: Field Time is not reset when restarting events (but for: new/proceeding events, second runs on PP).
'''
from .baseTracker import BaseTracker

class TimeTracker(BaseTracker):

    def __init__(self):
        self.time = 0
        self.previous_time = None

    def track(self, stats):
        self.previous_time = self.time
        self.time = stats[0]

    def getTimeDelta(self):
        if self.previous_time is None:
            return 0
        return self.time - self.previous_time

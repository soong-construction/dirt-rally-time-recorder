from .baseTracker import BaseTracker

class SpeedTracker(BaseTracker):
    # unit: m/s

    def __init__(self):
        self.speed = None
        self.top_speed = 0

    def track(self, stats):
        speed = int(stats[7])
        if self.top_speed < speed:
            self.top_speed = speed
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def getTopSpeed(self):
        return self.top_speed

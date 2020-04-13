class SpeedTracker():
    # unit: m/s
    
    def __init__(self):
        self.speed = None
        self.topSpeed = 0

    def track(self, stats):
        speed = int(stats[7])
        if self.topSpeed < speed:
            self.topSpeed = speed
        self.speed = speed
            
    def getSpeed(self):
        return self.speed
            
    def getTopSpeed(self):
        return self.topSpeed

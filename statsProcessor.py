class StatsProcessor():
    
    goLineDistance = 0.0
    
    def __init__(self, receiver):
        self.receiver = receiver
        

    def statsWithTelemetry(self, stats):
        return stats.count(0) != len(stats)

    def handleGameState(self, inStage, finished, lap, time, previousTime, distance, stats):
        # TODO #8 lap always 0 for DR2... but all fields 0.0 after stage completes
        # TODO Test if lap == 1 also works for second PP run
        if not finished and (lap == 1 or not self.statsWithTelemetry(stats)):
            self.receiver.finishStage(stats)
        
        elif time < previousTime:
            # Looks like time is not reset when restarting events (but for: fresh/proceeding events, second runs on PP).
            # New event for which track/car must be reset
            self.receiver.resetStage()
            
        elif distance <= self.goLineDistance and self.statsWithTelemetry(stats):
            # Reset stage data when starting a new stage
            self.receiver.prepareStage()
            
            if (not inStage):
                self.receiver.startStage(stats)
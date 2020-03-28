
class StatsProcessor():
    
    goLineProgress = 0.0
    completionProgress = 0.999
    
    def __init__(self, receiver):
        self.receiver = receiver
        
    def finishedDR2TimeTrial(self, stats, trackProgess):
        return not self.statsWithTelemetry(stats) and trackProgess >= self.completionProgress

    def statsWithTelemetry(self, stats):
        return stats.count(0) != len(stats)

    def handleGameState(self, inStage, finished, lap, time, previousTime, stageProgress, stats):
        if not finished and (lap == 1 or self.finishedDR2TimeTrial(stats, stageProgress)):
            self.receiver.finishStage(stats)
        
        elif time < previousTime:
            # Looks like time is not reset when restarting events (but for: fresh/proceeding events, second runs on PP).
            # New event for which track/car must be reset
            self.receiver.resetStage()
            
        elif stageProgress <= self.goLineProgress and self.statsWithTelemetry(stats):
            # Reset stage data when starting a new stage
            self.receiver.prepareStage()
            
            if (not inStage):
                self.receiver.startStage(stats)


class StatsProcessor():
    
    goLineDistance = 0.0
    completionTrackProgress = 0.999
    
    def __init__(self, receiver):
        self.receiver = receiver
        
    def finishedDR2TimeTrial(self, stats, trackProgess):
        return not self.statsWithTelemetry(stats) and trackProgess >= self.completionTrackProgress

    def statsWithTelemetry(self, stats):
        return stats.count(0) != len(stats)

    # TODO Are shakedowns and test drives ignored properly?
    def handleGameState(self, inStage, finished, lap, time, previousTime, distance, trackProgress, stats):
        if not finished and (lap == 1 or self.finishedDR2TimeTrial(stats, trackProgress)):
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
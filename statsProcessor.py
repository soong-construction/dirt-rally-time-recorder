
class StatsProcessor():
    
    goLineProgress = 0.0
    completionProgress = 0.999
    
    def __init__(self, receiver):
        self.receiver = receiver
        
    def finishedDR2TimeTrial(self, stats, trackProgess):
        return trackProgess >= self.completionProgress and not self.statsWithTelemetry(stats)

    def statsWithTelemetry(self, stats):
        return stats.count(0) != len(stats)

    def handleGameState(self, isRestart, inStage, finished, lap, time, previousTime, stageProgress, stats):
        if not finished and (lap == 1 or self.finishedDR2TimeTrial(stats, stageProgress)):
            self.receiver.finishStage(stats)
        
        elif isRestart or time < previousTime: # TODO Extract to timeTracker.timeReset(), save 1 parameter
            # Field Time is not reset when restarting events (but for: new/proceeding events, second runs on PP).
            self.receiver.resetRecognition()
         
        elif self.statsWithTelemetry(stats) and stageProgress <= self.goLineProgress:
            # Reset stage data when starting a new stage
            self.receiver.prepareStage()
            
            if (not inStage):
                self.receiver.startStage(stats)

import unittest
from unittest.mock import MagicMock

from statsProcessor import StatsProcessor
from database import Database

fieldCount = 66

class TestStatsProcessor(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        self.DatabaseSetupFunction = Database.setup

    def setUp(self):
        Database.setup = MagicMock()
        self.thing = StatsProcessor('mph', 'test.statsProcessor')
        self.thing.resetRecognition = MagicMock()
        self.thing.startStage = MagicMock()
        self.thing.finishStage = MagicMock()
        
        self.thing.print = MagicMock()

        self.stats = range(0, 256)
        self.allZeroStats = [0.0] * 256

    def tearDown(self):
        Database.setup = self.DatabaseSetupFunction

    # Scenario for timeDelta<0 and !restart: 1) cancel DR1 event near the start  2) enter the same event again (similar x/y pos)
    def testStageRestartOrTimeResetLeadToStageAborted(self):
        self.thing.timeTracker.getTimeDelta = MagicMock(return_value = -1)
        self.thing.respawnTracker.isRestart = MagicMock(return_value = False)
        self.assertTrue(self.thing.stageAborted())
    
        self.thing.timeTracker.getTimeDelta = MagicMock(return_value = 1)
        self.thing.respawnTracker.isRestart = MagicMock(return_value = True)
        self.assertTrue(self.thing.stageAborted())

        self.thing.timeTracker.getTimeDelta = MagicMock(return_value = 1)
        self.thing.respawnTracker.isRestart = MagicMock(return_value = False)
        self.assertFalse(self.thing.stageAborted())

    def testStartStage(self):
        self.thing.handleGameState(False, False, 0, -0.2, self.stats)
    
        self.assertFalse(self.thing.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.thing.startStage.called, 'Never called expected receiver method')
        self.assertFalse(self.thing.finishStage.called, 'Actually called unexpected receiver method')

    # This will ultimately lead to a recover to the start line which is treated as Restart (DR2: Disqualify?)
    def testMoveCarBehindStartLineDoesNotBreakRecognition(self):
        self.thing.handleGameState(False, True, 0, -0.2, self.stats)
    
        self.assertFalse(self.thing.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.finishStage.called, 'Actually called unexpected receiver method')
        
    def testStatsAfterAStageLeadToResetButNotStartStage(self):
        self.thing.handleGameState(True, True, 0, 0.9, self.allZeroStats)
    
        self.assertTrue(self.thing.resetRecognition.called, 'Never called expected receiver method')
        self.assertFalse(self.thing.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.finishStage.called, 'Actually called unexpected receiver method')
        
    def testResetRecognitionWhenStageIsAborted(self):
        self.thing.handleGameState(True, False, 0, 0.2, self.stats)

        self.assertTrue(self.thing.resetRecognition.called, 'Never called expected receiver method')
        self.assertFalse(self.thing.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.finishStage.called, 'Actually called unexpected receiver method')
        
    def testFinishStage(self):
        self.thing.handleGameState(False, True, 1, 0.9, self.stats)

        self.assertTrue(self.thing.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.startStage.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.thing.finishStage.called, 'Never called expected receiver method')

    def testFinishStageOnlyOnce(self):
        self.thing.handleGameState(False, False, 1, 0.9, self.stats)

        self.assertFalse(self.thing.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.finishStage.called, 'Never called expected receiver method')

    def testFinishStageInDR2TimeTrial(self):
        self.thing.handleGameState(False, True, 0, 0.999, self.allZeroStats)

        self.assertTrue(self.thing.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.startStage.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.thing.finishStage.called, 'Never called expected receiver method')

    def testDontFinishStageInDR2TimeTrialIfNotAtEndOfStage(self):
        self.thing.handleGameState(False, True, 0, 0.822, self.allZeroStats)

        self.assertFalse(self.thing.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.thing.finishStage.called, 'Actually called unexpected receiver method')
        
    def testTopSpeedConversion(self):
        self.thing = StatsProcessor('kmh', 'testroot')
        self.thing.speedTracker.topSpeed = 33.28

        format_top_speed = self.thing.formatTopSpeed()
        self.assertEqual(format_top_speed, '119.8')

        self.thing = StatsProcessor('mph', 'testroot')
        self.thing.speedTracker.topSpeed = 33.28

        format_top_speed = self.thing.formatTopSpeed()
        self.assertEqual(format_top_speed, '74.4')
        
    def testLapTimeConversion(self):
        format_lap_time = self.thing.formatLapTime(180.249)
        self.assertEqual(format_lap_time, '180.25')
 
    def testHandleFinishStageAndPrintResults(self):
        stats = [1] * fieldCount

        self.thing.inStage = MagicMock(return_value=True)
        self.thing.databaseAccess.recordResults = MagicMock()
        self.thing.databaseAccess.identifyCar = MagicMock(return_value=10)
        self.thing.databaseAccess.identifyTrack = MagicMock(return_value=11)

        # stats[59] == 1 means lap/stage complete
        stats[59] = 1
        self.thing.handleStats(stats)

        self.assertTrue(self.thing.print.recordResults, 'Did not call mock')

    def testHandleStartStageAndDatabaseCalled(self):
        stats = [1] * fieldCount

        self.thing.inStage = MagicMock(return_value=False)
        self.thing.databaseAccess.recordResults = MagicMock()
        self.thing.databaseAccess.identifyCar = MagicMock(return_value=10)
        self.thing.databaseAccess.identifyTrack = MagicMock(return_value=11)

        stats[59] = 0
        self.thing.handleStats(stats)

        self.assertTrue(self.thing.print.identifyCar, 'Did not call mock')
        self.assertTrue(self.thing.print.identifyTrack, 'Did not call mock')

    def testTrackersAreCalledWithStats(self):
        self.thing.timeTracker = MagicMock()
        self.thing.stageAborted = MagicMock(return_value = False)

        stats = [1] * fieldCount
        self.thing.handleStats(stats)

        self.thing.timeTracker.track.assert_called()

    def testTrackersAreNotCalledWithEmptyStats(self):
        self.thing.timeTracker = MagicMock()
        self.thing.stageAborted = MagicMock(return_value = False)

        stats = [0] * fieldCount
        self.thing.handleStats(stats)

        self.thing.timeTracker.track.assert_not_called()

if __name__ == "__main__":
    unittest.main()
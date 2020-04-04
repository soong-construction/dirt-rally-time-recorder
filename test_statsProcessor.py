from unittest import mock
import unittest
from unittest.mock import MagicMock

from receiver import Receiver
from statsProcessor import StatsProcessor
from database import Database

class TestStatsProcessor(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        self.DatabaseSetupFunction = Database.setup
    
    def setUp(self):
        Database.setup = MagicMock()
        Receiver.reconnect = mock.Mock(return_value=None)
        
        self.receiver = Receiver(('localhost', 12345), 'mph', 'test.statsProcessor')
        self.receiver.resetRecognition = MagicMock()
        self.receiver.startStage = MagicMock()
        self.receiver.finishStage = MagicMock()
        
        self.stats = range(0, 256)
        self.allZeroStats = [0.0] * 256
        
        self.thing = StatsProcessor(self.receiver)
        
    def tearDown(self):
        Database.setup = self.DatabaseSetupFunction
        pass

    def testStartStage(self):
        self.thing.handleGameState(False, False, 0, 13, -0.2, self.stats)
    
        self.assertFalse(self.receiver.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.receiver.startStage.called, 'Never called expected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')

    # This will ultimately lead to a recover to the start line which is treated as Restart (DR2: Disqualify?)
    def testMoveCarBehindStartLineDoesNotBreakRecognition(self):
        self.thing.handleGameState(False, True, 0, 13, -0.2, self.stats)
    
        self.assertFalse(self.receiver.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
        
    def testStatsAfterAStageLeadToResetButNotStartStage(self):
        self.thing.handleGameState(False, True, 0, -900, 0.9, self.allZeroStats)
    
        self.assertTrue(self.receiver.resetRecognition.called, 'Never called expected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
        
    # Scenario: After cancelling a DR1 event near the start, enter the same event again (similar x/y pos) 
    def testResetRecognitionWhenTimeIsReset(self):
        self.thing.handleGameState(False, True, 0, -900, 0.2, self.stats)

        self.assertTrue(self.receiver.resetRecognition.called, 'Never called expected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
    
    def testResetRecognitionWhenStageIsRestarted(self):
        self.thing.handleGameState(True, False, 0, 5, 0.2, self.stats)

        self.assertTrue(self.receiver.resetRecognition.called, 'Never called expected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
        
    def testFinishStage(self):
        self.thing.handleGameState(False, True, 1, 13, 0.9, self.stats)

        self.assertTrue(self.receiver.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.receiver.finishStage.called, 'Never called expected receiver method')

    def testFinishStageOnlyOnce(self):
        self.thing.handleGameState(False, False, 1, 13, 0.9, self.stats)

        self.assertFalse(self.receiver.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Never called expected receiver method')

    def testFinishStageInDR2TimeTrial(self):
        self.thing.handleGameState(False, True, 0, 13, 0.999, self.allZeroStats)

        self.assertTrue(self.receiver.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.receiver.finishStage.called, 'Never called expected receiver method')

    def testDontFinishStageInDR2TimeTrialIfNotAtEndOfStage(self):
        self.thing.handleGameState(False, True, 0, 13, 0.822, self.allZeroStats)

        self.assertFalse(self.receiver.resetRecognition.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
        
if __name__ == "__main__":
    unittest.main()
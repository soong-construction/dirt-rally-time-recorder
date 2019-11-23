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
        self.receiver.resetStage = MagicMock()
        self.receiver.prepareStage = MagicMock()
        self.receiver.startStage = MagicMock()
        self.receiver.finishStage = MagicMock()
        
        self.stats = range(0, 256)
        self.allZeroStats = [0.0] * 256
        
        self.thing = StatsProcessor(self.receiver)
        
    def tearDown(self):
        Database.setup = self.DatabaseSetupFunction
        pass

    def testPrepareAndStartStage(self):
        self.thing.handleGameState(False, False, 0, 905, 900, -40, -0.2, self.stats)
    
        self.assertFalse(self.receiver.resetStage.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.receiver.prepareStage.called, 'Never called expected receiver method')
        self.assertTrue(self.receiver.startStage.called, 'Never called expected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')

    # TODO #8 Can this actually happen in DR1?
    def testPrepareStageWithoutStart(self):
        self.thing.handleGameState(True, False, 0, 905, 900, -40, -0.2, self.stats)
    
        self.assertFalse(self.receiver.resetStage.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.receiver.prepareStage.called, 'Never called expected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
        
    def testStatsAfterAStageLeadToResetButNotStartStage(self):
        self.thing.handleGameState(True, True, 0, 0, 900, 0, 0.9, self.allZeroStats)
    
        self.assertTrue(self.receiver.resetStage.called, 'Never called expected receiver method')
        self.assertFalse(self.receiver.prepareStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
        
    def testResetStage(self):
        self.thing.handleGameState(False, True, 0, 0, 900, 40, 0.2, self.stats)

        self.assertTrue(self.receiver.resetStage.called, 'Never called expected receiver method')
        self.assertFalse(self.receiver.prepareStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
        
    def testFinishStage(self):
        self.thing.handleGameState(False, False, 1, 1888, 1854, 12202, 0.9, self.stats)

        self.assertFalse(self.receiver.resetStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.prepareStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.receiver.finishStage.called, 'Never called expected receiver method')

    def testFinishStageInDR2TimeTrial(self):
        self.thing.handleGameState(True, False, 0, 1888, 1854, 12202, 0.999, self.allZeroStats)

        self.assertFalse(self.receiver.resetStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.prepareStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertTrue(self.receiver.finishStage.called, 'Never called expected receiver method')

    def testDontFinishStageInDR2TimeTrialIfNotAtEndOfStage(self):
        self.thing.handleGameState(True, False, 0, 1888, 1854, 12000, 0.822, self.allZeroStats)

        self.assertFalse(self.receiver.resetStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.prepareStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.startStage.called, 'Actually called unexpected receiver method')
        self.assertFalse(self.receiver.finishStage.called, 'Actually called unexpected receiver method')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestDatabaseAccess.testPrepareAndStartStage']
    unittest.main()
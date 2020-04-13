import unittest
from unittest.mock import MagicMock
from timerecorder.respawnTracker import RespawnTracker
from timerecorder.gearTracker import GearTracker

fieldCount = 66

class TestGearTracker(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.respawnTracker = RespawnTracker()
        self.respawnTracker.isRecover = MagicMock(return_value=False)
        self.respawnTracker.isRestart = MagicMock(return_value=False)
        self.thing = GearTracker(self.respawnTracker)

    def tearDown(self):
        pass
    
    def testGearChangeCountIncreasesForDifferentGear(self):
        stats = [0] * fieldCount
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0)
        
        stats[33] = 1
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0)
        
        stats[33] = 2
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 1)
        
    def testGearsSkippedCount(self):
        stats = [1] * fieldCount
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearSkipCount(), 0)

        stats[33] = 2
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 1) 
        self.assertEqual(self.thing.getGearSkipCount(), 0) 
        
        stats[33] = 4
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 2) 
        self.assertEqual(self.thing.getGearSkipCount(), 1) 
      
    def testShouldIgnoreNeutral(self):
        stats = [3] * fieldCount
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0) 
        self.assertEqual(self.thing.getGearSkipCount(), 0)

        stats[33] = 0
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0) 
        self.assertEqual(self.thing.getGearSkipCount(), 0) 
        
        stats[33] = 1
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 1) 
        self.assertEqual(self.thing.getGearSkipCount(), 1)   

    def testGearsNotSkippedForReverseDR1(self):
        stats = [1] * fieldCount
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0) 
        self.assertEqual(self.thing.getGearSkipCount(), 0)

        stats[33] = 10
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 1) 
        self.assertEqual(self.thing.getGearSkipCount(), 0) 
        
        stats[33] = 1
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 2) 
        self.assertEqual(self.thing.getGearSkipCount(), 0) 

    def testGearsNotSkippedForReverseDR2(self):
        stats = [1] * fieldCount
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0) 
        self.assertEqual(self.thing.getGearSkipCount(), 0)

        stats[33] = -1
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 1) 
        self.assertEqual(self.thing.getGearSkipCount(), 0) 
        
        stats[33] = 1
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 2) 
        self.assertEqual(self.thing.getGearSkipCount(), 0) 

    def testGearsNotChangedOrSkippedForRespawn(self):
        stats = [1] * fieldCount
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0) 
        self.assertEqual(self.thing.getGearSkipCount(), 0)

        self.respawnTracker.isRecover = MagicMock(return_value = True)
        stats[33] = 3
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0) 
        self.assertEqual(self.thing.getGearSkipCount(), 0)
        
        self.respawnTracker.isRecover = MagicMock(return_value = False)
        self.respawnTracker.isRestart = MagicMock(return_value = True)
        stats[33] = -1
        self.thing.track(stats)
        self.assertEqual(self.thing.getGearChangeCount(), 0) 
        self.assertEqual(self.thing.getGearSkipCount(), 0)

if __name__ == '__main__':
    unittest.main()
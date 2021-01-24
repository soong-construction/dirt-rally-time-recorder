import unittest
from timerecorder.respawnTracker import RespawnTracker

FIELD_COUNT = 66

class TestRespawnTracker(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.thing = RespawnTracker()

    def tearDown(self):
        pass

    def testNoRespawnForFirstStats(self):
        stats = [0] * FIELD_COUNT
        stats[4] = 100.0

        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

    def testNoRespawnForLowXDeltas(self):
        stats = [0] * FIELD_COUNT
        stats[4] = 100.0
        self.thing.track(stats)

        stats[4] = 101.1
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

        stats[4] = 100.8
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

        stats[4] = 99.9
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

    def testNoRespawnForLowYDeltas(self):
        stats = [0] * FIELD_COUNT
        stats[5] = 100.0
        self.thing.track(stats)

        stats[5] = 101.1
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

        stats[5] = 100.8
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

        stats[5] = 99.9
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

    def testNoRespawnForCombinedDeltas(self):
        stats = [0] * FIELD_COUNT
        stats[4] = 100.0
        stats[5] = 100.0
        self.thing.track(stats)

        stats[4] = 101.1
        stats[5] = 101.0
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

        stats[4] = 100.8
        stats[5] = 102.2
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover() or self.thing.isRestart())

    def testSmallDeltaIsRecover(self):
        stats = [0] * FIELD_COUNT
        stats[4] = 100.0
        stats[5] = 100.0
        self.thing.track(stats)

        stats[4] = 95.0
        stats[5] = 100.0
        self.thing.track(stats)
        self.assertTrue(self.thing.isRecover())
        self.assertFalse(self.thing.isRestart())

        stats[4] = 96.8
        stats[5] = 99.9
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover())
        self.assertFalse(self.thing.isRestart())

        stats[4] = 97.0
        stats[5] = 105.0
        self.thing.track(stats)
        self.assertTrue(self.thing.isRecover())
        self.assertFalse(self.thing.isRestart())

    def testLargeDeltaIsRestartForDistanceValueNearZero(self):
        stats = [0] * FIELD_COUNT
        stats[2] = 13
        stats[4] = 100.0
        stats[5] = 100.0
        self.thing.track(stats)

        stats[2] = 5
        stats[4] = 20.0
        stats[5] = 100.0
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover())
        self.assertTrue(self.thing.isRestart())

        stats[4] = 10.0
        stats[5] = 15.0
        self.thing.track(stats)
        self.assertFalse(self.thing.isRecover())
        self.assertTrue(self.thing.isRestart())

    def testLargeDeltaIsRecoverForHigherDistanceValue(self):
        stats = [0] * FIELD_COUNT
        stats[2] = 25
        stats[4] = 100.0
        stats[5] = 100.0
        self.thing.track(stats)

        stats[4] = 20.0
        stats[5] = 100.0
        self.thing.track(stats)
        self.assertTrue(self.thing.isRecover())
        self.assertFalse(self.thing.isRestart())

        stats[4] = 10.0
        stats[5] = 15.0
        self.thing.track(stats)
        self.assertTrue(self.thing.isRecover())
        self.assertFalse(self.thing.isRestart())

if __name__ == '__main__':
    unittest.main()

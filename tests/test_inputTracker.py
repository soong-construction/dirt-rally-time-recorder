import unittest
from timerecorder.inputTracker import InputTracker, Signal
from unittest.mock import MagicMock


fieldCount = 66

class TestInputTracker(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.speedTracker = MagicMock()
        self.speedTracker.getTopSpeed = MagicMock(return_value = 0)
        self.thing = InputTracker(self.speedTracker)

    def tearDown(self):
        pass

    def testSignalBeforeData(self):
        self.assertIsNone(self.thing.signal, 'Signal must be initially None')

    def testSignalThrottleLeft(self):
        stats = [0] * fieldCount
        stats[29] = 0.6
        stats[30] = -0.6

        self.thing.track(stats)
        self.assertEqual(self.thing.signal, Signal.THROTTLE_LEFT)

    def testNoTrackingIfNotEnabled(self):
        self.thing.enabled = True
        stats = [0] * fieldCount
        
        self.thing.track(stats)
        self.speedTracker.getTopSpeed.assert_called_once()
        self.speedTracker.getTopSpeed.reset_mock()
        
        self.thing.enabled = False
        self.thing.track(stats)
        self.speedTracker.getTopSpeed.assert_not_called()
        
    def testSignalThrottleRight(self):
        self.speedTracker.getTopSpeed = MagicMock(return_value = 0)
        stats = [0] * fieldCount
        stats[29] = 0.6
        stats[30] = 0.6

        self.thing.track(stats)
        self.assertEqual(self.thing.signal, Signal.THROTTLE_RIGHT)

if __name__ == '__main__':
    unittest.main()
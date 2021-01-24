import unittest
from unittest.mock import MagicMock
from timerecorder.inputTracker import InputTracker, Signal

FIELD_COUNT = 66

class TestInputTracker(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.speed_tracker = MagicMock()
        self.speed_tracker.getTopSpeed = MagicMock(return_value=0)
        self.notify = MagicMock()
        self.thing = InputTracker(self.speed_tracker, self.notify)

    def tearDown(self):
        pass

    def testNoSignalBeforeData(self):
        self.assertIsNone(self.thing.input, 'Input must be initially None')
        self.assertIsNone(self.thing.signal, 'Signal must be initially None')

    def testIsSignalLeft(self):
        self.assertTrue(self.thing.isSignalLeft(0.6, -0.6))

    def testIsSignalRight(self):
        self.assertTrue(self.thing.isSignalRight(0.6, 0.6))

    def testIsNoSignal(self):
        thing = self.thing

        throttle = 0.6
        steer = -0.2
        self.assertFalse(thing.isSignalLeft(throttle, steer))
        self.assertFalse(thing.isSignalRight(throttle, steer))

        throttle = 0.6
        steer = 0.2
        self.assertFalse(thing.isSignalLeft(throttle, steer))
        self.assertFalse(thing.isSignalRight(throttle, steer))

        throttle = 0.2
        steer = -0.6
        self.assertFalse(thing.isSignalLeft(throttle, steer))
        self.assertFalse(thing.isSignalRight(throttle, steer))

        throttle = 0.2
        steer = 0.6
        self.assertFalse(thing.isSignalLeft(throttle, steer))
        self.assertFalse(thing.isSignalRight(throttle, steer))

    def testNoTrackingIfNotEnabled(self):
        self.thing.enabled = True
        stats = [0] * FIELD_COUNT

        self.thing.track(stats)
        self.speed_tracker.getTopSpeed.assert_called_once()
        self.speed_tracker.getTopSpeed.reset_mock()

        self.thing.enabled = False
        self.thing.track(stats)
        self.speed_tracker.getTopSpeed.assert_not_called()

    def testSignalLeftOnlyAfterInputGone(self):
        self.notify.assert_not_called()
        self.speed_tracker.getTopSpeed = MagicMock(return_value=0)
        stats = [0] * FIELD_COUNT
        stats[29] = 0.6
        stats[30] = -0.6

        self.thing.track(stats)
        self.assertEqual(self.thing.input, Signal.THROTTLE_LEFT)
        self.notify.assert_called_once()
        self.assertIsNone(self.thing.signal)

        stats[29] = 0.0
        self.thing.track(stats)
        self.assertIsNone(self.thing.input)
        self.notify.assert_called_once()
        self.assertEqual(self.thing.signal, Signal.THROTTLE_LEFT)

    def testSignalRightOnlyAfterInputGone(self):
        self.notify.assert_not_called()
        self.speed_tracker.getTopSpeed = MagicMock(return_value=0)
        stats = [0] * FIELD_COUNT
        stats[29] = 0.6
        stats[30] = 0.6

        self.thing.track(stats)
        self.assertEqual(self.thing.input, Signal.THROTTLE_RIGHT)
        self.notify.assert_called_once()
        self.assertIsNone(self.thing.signal)

        stats[29] = 0.0
        self.thing.track(stats)
        self.assertIsNone(self.thing.input)
        self.notify.assert_called_once()
        self.assertEqual(self.thing.signal, Signal.THROTTLE_RIGHT)

if __name__ == '__main__':
    unittest.main()

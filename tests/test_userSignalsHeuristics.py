import unittest

from timerecorder.userSignalsHeuristics import UserSignalsHeuristics
from unittest.mock import MagicMock
from timerecorder.inputTracker import InputTracker, Signal

class TestUserSignalsHeuristics(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def testNotApplicableForManyCandidates(self):
        car_candidates = [100, 200, 300]
        inputTracker = MagicMock()
        self.thing = UserSignalsHeuristics(car_candidates, inputTracker)
        self.assertIsNone(self.thing.guessCar())

    def testReturnsMatchingCandidateIfSignalLeftReceived(self):
        car_candidates = [100, 200]
        inputTracker = InputTracker(MagicMock())
        inputTracker.getSignal = MagicMock(return_value = Signal.THROTTLE_LEFT)

        self.thing = UserSignalsHeuristics(car_candidates, inputTracker)
        self.thing.withFallback(MagicMock())

        car = self.thing.guessCar()
        self.assertEqual(car, 100, 'Did not return signaled candidate')

    def testReturnsMatchingCandidateIfSignalRightReceived(self):
        car_candidates = [100, 200]
        inputTracker = InputTracker(MagicMock())
        inputTracker.getSignal = MagicMock(return_value = Signal.THROTTLE_RIGHT)

        self.thing = UserSignalsHeuristics(car_candidates, inputTracker)
        self.thing.withFallback(MagicMock())

        car = self.thing.guessCar()
        self.assertEqual(car, 200, 'Did not return signaled candidate')

    def testCallsFallbackWithoutSignalReceived(self):
        car_candidates = [100, 200]
        inputTracker = InputTracker(MagicMock())
        inputTracker.getSignal = MagicMock(return_value = None)

        self.thing = UserSignalsHeuristics(car_candidates, inputTracker)
        fallback = MagicMock()
        fallback.guessCar = MagicMock(return_value = 100)
        self.thing.withFallback(fallback)

        car = self.thing.guessCar()

        fallback.guessCar.assert_called_once()
        self.assertEqual(car, 100, 'Did not return fallback guess')

if __name__ == '__main__':
    unittest.main()
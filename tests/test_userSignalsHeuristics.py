import unittest
from unittest.mock import MagicMock
from timerecorder.userSignalsHeuristics import UserSignalsHeuristics

from timerecorder.inputTracker import InputTracker, Signal

class TestUserSignalsHeuristics(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def testNotApplicableForManyCandidates(self):
        carCandidates = [100, 200, 300]
        inputTracker = MagicMock()
        self.thing = UserSignalsHeuristics(carCandidates, inputTracker)
        self.assertIsNone(self.thing.guessCar())

    def testReturnsMatchingCandidateIfSignalLeftReceived(self):
        carCandidates = [100, 200]
        inputTracker = InputTracker(MagicMock(), MagicMock())
        inputTracker.getSignal = MagicMock(return_value=Signal.THROTTLE_LEFT)

        self.thing = UserSignalsHeuristics(carCandidates, inputTracker)
        self.thing.withFallback(MagicMock())

        car = self.thing.guessCar()
        self.assertEqual(car, 100, 'Did not return signaled candidate')

    def testReturnsMatchingCandidateIfSignalRightReceived(self):
        carCandidates = [100, 200]
        inputTracker = InputTracker(MagicMock(), MagicMock())
        inputTracker.getSignal = MagicMock(return_value=Signal.THROTTLE_RIGHT)

        self.thing = UserSignalsHeuristics(carCandidates, inputTracker)
        self.thing.withFallback(MagicMock())

        car = self.thing.guessCar()
        self.assertEqual(car, 200, 'Did not return signaled candidate')

    def testCallsFallbackWithoutSignalReceived(self):
        carCandidates = [100, 200]
        inputTracker = InputTracker(MagicMock(), MagicMock())
        inputTracker.getSignal = MagicMock(return_value=None)

        self.thing = UserSignalsHeuristics(carCandidates, inputTracker)
        fallback = MagicMock()
        fallback.guessCar = MagicMock(return_value=100)
        self.thing.withFallback(fallback)

        car = self.thing.guessCar()

        fallback.guessCar.assert_called_once()
        self.assertEqual(car, 100, 'Did not return fallback guess')

if __name__ == '__main__':
    unittest.main()

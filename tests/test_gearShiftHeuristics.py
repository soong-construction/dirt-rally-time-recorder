import unittest
from unittest.mock import MagicMock

from timerecorder.gearShiftHeuristics import GearShiftHeuristics

class TestLuckyGuessHeuristics(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.gear_tracker = MagicMock()
        self.gear_tracker.getGearChangeCount = MagicMock(return_value=25)

    def tearDown(self):
        pass

    def testReturnsMatchingCandidateWithGearsSkipped(self):
        carCandidates = [(100, 'H-PATTERN'), (200, 'SEQUENTIAL')]
        self.gear_tracker.getGearSkipCount = MagicMock(return_value=2)

        self.thing = GearShiftHeuristics(carCandidates, self.gear_tracker)
        self.thing.withFallback(MagicMock())

        car = self.thing.guessCar()

        self.assertEqual(car, 100, 'Did not return matching candidate')

    def testReturnsMatchingCandidateWithoutGearsSkipped(self):
        carCandidates = [(100, 'H-PATTERN'), (200, 'SEQUENTIAL')]
        self.gear_tracker.getGearSkipCount = MagicMock(return_value=0)

        self.thing = GearShiftHeuristics(carCandidates, self.gear_tracker)
        self.thing.withFallback(MagicMock())

        car = self.thing.guessCar()

        self.assertEqual(car, 200, 'Did not return matching candidate')

    def testCallsFallbackWithoutDifferingShifting(self):
        carCandidates = [(100, 'H-PATTERN'), (200, 'H-PATTERN')]
        self.gear_tracker.getGearSkipCount = MagicMock(return_value=2)

        self.thing = GearShiftHeuristics(carCandidates, self.gear_tracker)
        fallback = MagicMock()
        fallback.guessCar = MagicMock(return_value=100)
        self.thing.withFallback(fallback)

        car = self.thing.guessCar()

        fallback.guessCar.assert_called_once()
        self.assertEqual(car, 100, 'Did not return fallback guess')

    def testCallsFallbackWithoutSufficientShifts(self):
        carCandidates = [(100, 'H-PATTERN'), (200, 'SEQUENTIAL')]
        self.gear_tracker.getGearSkipCount = MagicMock(return_value=2)
        self.gear_tracker.getGearChangeCount = MagicMock(return_value=3)

        self.thing = GearShiftHeuristics(carCandidates, self.gear_tracker)
        fallback = MagicMock()
        fallback.guessCar = MagicMock(return_value=100)
        self.thing.withFallback(fallback)

        car = self.thing.guessCar()

        fallback.guessCar.assert_called_once()
        self.assertEqual(car, 100, 'Did not return fallback guess')

    def testCallsFallbackForManyCandidates(self):
        carCandidates = [(100, 'H-PATTERN'), (200, 'H-PATTERN'), (300, 'H-PATTERN')]
        self.thing = GearShiftHeuristics(carCandidates, self.gear_tracker)
        fallback = MagicMock()
        fallback.guessCar = MagicMock(return_value=100)
        self.thing.withFallback(fallback)

        car = self.thing.guessCar()

        fallback.guessCar.assert_called_once()
        self.assertEqual(car, 100, 'Did not return fallback guess')

if __name__ == '__main__':
    unittest.main()

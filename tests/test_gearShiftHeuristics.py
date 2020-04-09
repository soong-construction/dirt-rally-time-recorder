import unittest
from unittest.mock import MagicMock

from timerecorder.gearShiftHeuristics import GearShiftHeuristics

class TestLuckyGuessHeuristics(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.gearTracker = MagicMock()
        self.gearTracker.getGearChangeCount = MagicMock(return_value = 25)

    def tearDown(self):
        pass
    
    def testReturnsMatchingCandidateWithGearsSkipped(self):
        car_candidates = [(100, 'H-PATTERN'), (200, 'SEQUENTIAL')]
        self.gearTracker.getGearSkipCount = MagicMock(return_value = 2)
        
        self.thing = GearShiftHeuristics(car_candidates, self.gearTracker)
        self.thing.withFallback(MagicMock())
        
        car = self.thing.guessCar()
        
        self.assertEqual(car, 100, 'Did not return matching candidate')
    
    def testReturnsMatchingCandidateWithoutGearsSkipped(self):
        car_candidates = [(100, 'H-PATTERN'), (200, 'SEQUENTIAL')]
        self.gearTracker.getGearSkipCount = MagicMock(return_value = 0)
        
        self.thing = GearShiftHeuristics(car_candidates, self.gearTracker)
        self.thing.withFallback(MagicMock())
        
        car = self.thing.guessCar()
        
        self.assertEqual(car, 200, 'Did not return matching candidate')
    
    def testCallsFallbackWithoutDifferingShifting(self):
        car_candidates = [(100, 'H-PATTERN'), (200, 'H-PATTERN')]
        self.gearTracker.getGearSkipCount = MagicMock(return_value = 2)
        
        self.thing = GearShiftHeuristics(car_candidates, self.gearTracker)
        fallback = MagicMock()
        fallback.guessCar = MagicMock(return_value = 100)
        self.thing.withFallback(fallback)
        
        car = self.thing.guessCar()
        
        fallback.guessCar.assert_called_once()
        self.assertIn(car, [100, 200])
    
    def testCallsFallbackWithoutSufficientShifts(self):
        car_candidates = [(100, 'H-PATTERN'), (200, 'SEQUENTIAL')]
        self.gearTracker.getGearSkipCount = MagicMock(return_value = 2)
        self.gearTracker.getGearChangeCount = MagicMock(return_value = 3)
        
        self.thing = GearShiftHeuristics(car_candidates, self.gearTracker)
        fallback = MagicMock()
        fallback.guessCar = MagicMock(return_value = 100)
        self.thing.withFallback(fallback)
        
        car = self.thing.guessCar()
        
        fallback.guessCar.assert_called_once()
        self.assertIn(car, [100, 200])

    def testCallsFallbackForManyCandidates(self):
        car_candidates = [(100, 'H-PATTERN'), (200, 'H-PATTERN'), (300, 'H-PATTERN')]
        self.thing = GearShiftHeuristics(car_candidates, self.gearTracker)
        fallback = MagicMock()
        fallback.guessCar = MagicMock(return_value = 100)
        self.thing.withFallback(fallback)
        
        car = self.thing.guessCar()
        
        fallback.guessCar.assert_called_once()
        self.assertIn(car, [100, 200, 300])
        
if __name__ == '__main__':
    unittest.main()
import random
import unittest
from timerecorder.luckyGuessHeuristics import LuckyGuessHeuristics

class TestLuckyGuessHeuristics(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def testReturnsMatchingCandidate(self):
        car_candidates = [100, 200]
        self.thing = LuckyGuessHeuristics(car_candidates)
        self.assertIn(self.thing.guessCar(), car_candidates, 'Did not return candidate')

    def testNotApplicableForManyCandidates(self):
        car_candidates = [100, 200, 300, 400]
        self.thing = LuckyGuessHeuristics(car_candidates)
        self.assertIsNone(self.thing.guessCar())

    def testReturnsSameCandidateForSeededRandom(self):
        car_candidates = [100, 200, 300]
        
        self.thing = LuckyGuessHeuristics(car_candidates, random.seed(0))
        self.thing2 = LuckyGuessHeuristics(car_candidates, random.seed(0)) 
        self.assertEqual(self.thing.guessCar(), self.thing2.guessCar())

if __name__ == '__main__':
    unittest.main()
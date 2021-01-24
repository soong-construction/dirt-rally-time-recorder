import random
import unittest
from timerecorder.luckyGuessHeuristics import LuckyGuessHeuristics

class TestLuckyGuessHeuristics(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def testReturnsMatchingCandidate(self):
        carCandidates = [100, 200]
        self.thing = LuckyGuessHeuristics(carCandidates)
        self.assertIn(self.thing.guessCar(), carCandidates, 'Did not return candidate')

    def testNotApplicableForManyCandidates(self):
        carCandidates = [100, 200, 300, 400]
        self.thing = LuckyGuessHeuristics(carCandidates)
        self.assertIsNone(self.thing.guessCar())

    def testReturnsSameCandidateForSeededRandom(self):
        carCandidates = [100, 200, 300]

        for _ in range(0, 1000):
            thing = LuckyGuessHeuristics(carCandidates, random.seed(0))
            thing2 = LuckyGuessHeuristics(carCandidates, random.seed(0))
            self.assertEqual(thing.guessCar(), thing2.guessCar())

if __name__ == '__main__':
    unittest.main()

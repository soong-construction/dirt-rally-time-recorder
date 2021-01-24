import unittest
from timerecorder.luckyGuessHeuristics import LuckyGuessHeuristics

class TestLuckyGuessHeuristics(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def testReturnsMatchingCandidate(self):
        carCandidates = [100, 200]
        thing = LuckyGuessHeuristics(carCandidates, 0)
        self.assertIn(thing.guessCar(), carCandidates, 'Did not return candidate')

    def testNotApplicableForManyCandidates(self):
        carCandidates = [100, 200, 300, 400]
        thing = LuckyGuessHeuristics(carCandidates, 0)
        self.assertIsNone(thing.guessCar())

    def testReturnsSameCandidateForSeededRandom(self):
        carCandidates = [100, 200, 300]

        for i in range(0, 1000):
            thing = LuckyGuessHeuristics(carCandidates, 1)
            thing2 = LuckyGuessHeuristics(carCandidates, 1)
            self.assertEqual(thing.guessCar(), thing2.guessCar(), f'Seeding failed in run {i}')

if __name__ == '__main__':
    unittest.main()

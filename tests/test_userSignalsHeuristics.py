import unittest

from timerecorder.userSignalsHeuristics import UserSignalsHeuristics
from unittest.mock import MagicMock

class TestUserSignalsHeuristics(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def testNotApplicableForManyCandidates(self):
        car_candidates = [100, 200, 300]
        inputTracker = MagicMock()
        self.thing = UserSignalsHeuristics(car_candidates, inputTracker)
        self.assertIsNone(self.thing.guessCar())

if __name__ == '__main__':
    unittest.main()
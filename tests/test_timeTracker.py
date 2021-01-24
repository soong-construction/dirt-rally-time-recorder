import unittest
from timerecorder.timeTracker import TimeTracker

FIELD_COUNT = 66

class TestTimeTracker(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.thing = TimeTracker()

    def tearDown(self):
        pass

    def testTimeChangeTracked(self):
        self.assertEqual(self.thing.getTimeDelta(), 0)

        stats = [0] * FIELD_COUNT
        stats[0] = 100
        self.thing.track(stats)
        self.assertEqual(self.thing.getTimeDelta(), 100)

        stats[0] = 150
        self.thing.track(stats)
        self.assertEqual(self.thing.getTimeDelta(), 50)

if __name__ == '__main__':
    unittest.main()

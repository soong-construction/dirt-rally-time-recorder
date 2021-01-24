import unittest
from timerecorder.speedTracker import SpeedTracker

FIELD_COUNT = 66

class TestSpeedTracker(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.thing = SpeedTracker()

    def tearDown(self):
        pass

    def testSpeedTracked(self):
        stats = [0] * FIELD_COUNT
        self.thing.track(stats)
        self.assertEqual(self.thing.getSpeed(), 0)
        self.assertEqual(self.thing.getTopSpeed(), 0)

        stats[7] = 10.2
        self.thing.track(stats)
        self.assertEqual(self.thing.getSpeed(), 10)
        self.assertEqual(self.thing.getTopSpeed(), 10)

        stats[7] = 13
        self.thing.track(stats)
        self.assertEqual(self.thing.getSpeed(), 13)
        self.assertEqual(self.thing.getTopSpeed(), 13)

        stats[7] = 9.8
        self.thing.track(stats)
        self.assertEqual(self.thing.getSpeed(), 9)
        self.assertEqual(self.thing.getTopSpeed(), 13)

if __name__ == '__main__':
    unittest.main()

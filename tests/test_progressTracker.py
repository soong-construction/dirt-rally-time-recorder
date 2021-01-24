import unittest
from timerecorder.progressTracker import ProgressTracker

FIELD_COUNT = 66

class TestProgressTracker(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.thing = ProgressTracker()

    def tearDown(self):
        pass

    def testProgressBeforeData(self):
        self.assertEqual(self.thing.getTrackLength(), None)
        self.assertEqual(self.thing.getProgress(), None)

    def testTrackLengthTrackedOnce(self):
        self.assertEqual(self.thing.getTrackLength(), None)
        stats = [0] * FIELD_COUNT
        stats[61] = 10000

        self.thing.track(stats)
        self.assertEqual(self.thing.getTrackLength(), 10000)

        stats[61] = 0
        self.thing.track(stats)
        self.assertEqual(self.thing.getTrackLength(), 10000)

    def testProgressTracked(self):
        stats = [0] * FIELD_COUNT
        stats[2] = 1000
        stats[61] = 10000
        self.thing.track(stats)
        self.assertEqual(self.thing.getTrackLength(), 10000)
        self.assertEqual(self.thing.getProgress(), 0.1)

        stats[2] = 10000
        self.thing.track(stats)
        self.assertEqual(self.thing.getTrackLength(), 10000)
        self.assertEqual(self.thing.getProgress(), 1.0)

    def testNegativeProgressTracked(self):
        stats = [0] * FIELD_COUNT
        stats[2] = -5
        stats[61] = 10000

        self.thing.track(stats)
        self.assertEqual(self.thing.getTrackLength(), 10000)
        self.assertEqual(self.thing.getProgress(), -0.0005)

    def testLapTracked(self):
        self.assertIsNone(self.thing.getLap())

        stats = [0] * FIELD_COUNT
        stats[59] = 1
        self.thing.track(stats)
        self.assertEqual(self.thing.getLap(), 1)

        stats = [1] * FIELD_COUNT
        self.thing.track(stats)
        self.assertEqual(self.thing.getLap(), 1)

if __name__ == '__main__':
    unittest.main()

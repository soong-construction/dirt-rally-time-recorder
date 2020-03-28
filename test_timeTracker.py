import unittest

from timeTracker import TimeTracker


fieldCount = 66

class TestTimeTracker(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.thing = TimeTracker()

    def tearDown(self):
        pass
    
    def testTimeChangeTracked(self):
        stats = [0] * fieldCount
        self.thing.track(stats)
        self.assertEqual(self.thing.getTime(), 0)
        self.assertEqual(self.thing.getPreviousTime(), None)
        
        stats[0] = 100
        self.thing.track(stats)
        self.assertEqual(self.thing.getTime(), 100)
        self.assertEqual(self.thing.getPreviousTime(), 0)
        
        stats[1] = 100
        self.thing.track(stats)
        self.assertEqual(self.thing.getTime(), 100)
        self.assertEqual(self.thing.getPreviousTime(), 100)
        
if __name__ == '__main__':
    unittest.main()
import unittest

from database import Database
import time

class TestDatabase(unittest.TestCase):


    def setUp(self):
        self.thing = Database('test')
        
    def tearDown(self):
        pass

    def testResetStage(self):
        statements = self.thing.getCarUpdateStatements(123456, [1])

        self.assertEqual(statements, ['UPDATE laptimes SET Car=1 WHERE Timestamp="123456";'])

    def testGetMultipleCarUpdateStatements(self):
        statements = self.thing.getCarUpdateStatements(123456, [1, 5])

        self.assertEqual(statements, ['UPDATE laptimes SET Car=1 WHERE Timestamp="123456";', 'UPDATE laptimes SET Car=5 WHERE Timestamp="123456";'])

    def testGetMultipleTrackUpdateStatements(self):
        statements = self.thing.getTrackUpdateStatements(123456, [1, 5])

        self.assertEqual(statements, ['UPDATE laptimes SET Track=1 WHERE Timestamp="123456";', 'UPDATE laptimes SET Track=5 WHERE Timestamp="123456";'])

    def testUnidentifiedTrackUpdateStatements(self):
        statements = self.thing.getTrackUpdateStatements(123456, [])

        self.assertEqual(statements, [])

    def testGetUserId(self):
        userId = self.thing.createUserId();
        print(userId)
        self.assertIsNotNone(userId, "userId must exist")

    def testUserIdDiffersOverTime(self):
        userId1 = self.thing.createUserId();
        time.sleep(1)
        userId2 = self.thing.createUserId();
        self.assertNotEqual(userId1, userId2, "userId must differ over time")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestDatabaseAccess.testResetStage']
    unittest.main()
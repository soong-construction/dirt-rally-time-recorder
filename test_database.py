import unittest

from database import Database

class TestDatabaseAccess(unittest.TestCase):


    def setUp(self):
        self.thing = Database('test')
        
    def tearDown(self):
        pass

    def testGetSingleUpdateStatement(self):
        statements = self.thing.getUpdateStatements(123456, [1])

        self.assertEqual(statements, ['UPDATE laptimes SET Car=1 WHERE Timestamp="123456";'])

    def testGetMultipleUpdateStatements(self):
        statements = self.thing.getUpdateStatements(123456, [1, 5])

        self.assertEqual(statements, ['UPDATE laptimes SET Car=1 WHERE Timestamp="123456";', 'UPDATE laptimes SET Car=5 WHERE Timestamp="123456";'])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestDatabaseAccess.testGetSingleUpdateStatement']
    unittest.main()
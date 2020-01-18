import unittest

from databaseMigration import DatabaseMigration

@unittest.skip("works only locally")
class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.thing = DatabaseMigration('test-files')
        
    def tearDown(self):
        pass

    def testUserVersion(self):
        self.thing.setup()
        userVersion = self.thing.getUserVersion()
        self.assertEqual(userVersion, 0, "user_version not 0")
        
    def testSetUserVersion(self):
        self.thing.setup()
        self.thing.setUserVersion(100)
        
        userVersion = self.thing.getUserVersion()
        self.assertEqual(userVersion, 100, "user_version not set correctly")
        
        self.thing.setUserVersion(0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestDatabaseAccess.testUserVersion']
    unittest.main()
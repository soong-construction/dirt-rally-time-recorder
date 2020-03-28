import unittest

from databaseMigration import DatabaseMigration
from unittest.mock import MagicMock

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.lapDb = MagicMock()
        self.thing = DatabaseMigration(self.lapDb)
        
        self.cursor = MagicMock()
        self.lapDb.execute = MagicMock(return_value=self.cursor)
        
        self.cursor.fetchall = MagicMock(return_value=[[0]])
        
    def tearDown(self):
        pass

    def testUserVersion(self):
        userVersion = self.thing.getUserVersion()
        self.assertEqual(userVersion, 0, "user_version not 0")
        
    def testSetUserVersion(self):
        initialVersion = 1_000_000
        
        self.thing.setUserVersion(initialVersion)
        
        self.assertEqual(self.lapDb.execute.call_count, 1)
        self.lapDb.execute.assert_called_with('PRAGMA user_version = 1000000')
        
    def testVersionExpansion(self):
        expand_version = self.thing.expandVersion('1.0.0')
        self.assertEqual(expand_version, 1_000_000);

        expand_version = self.thing.expandVersion('12.1.21')
        self.assertEqual(expand_version, 12_001_021);
        
    def testVersionExpansionWithWhitespace(self):
        expand_version = self.thing.expandVersion(' 1.2.3\r\n')
        self.assertEqual(expand_version, 1_002_003);

    def testVersionExpansionWithIllegalVersion(self):
        with self.assertRaises(RuntimeError):
            self.thing.expandVersion('1.1')

    def testInitialMigrationFromVersion1_0_0(self):
        initialVersion = 1_000_000
        self.cursor.fetchall = MagicMock(return_value=[[initialVersion]])
        
        self.thing.migrate_2_2_0();

        self.assertEqual(self.lapDb.execute.call_count, 2)
        self.lapDb.execute.assert_called_with('PRAGMA user_version = 2002000')

    def testInitialMigrationSkipped(self):
        initialVersion = 2_002_000
        self.cursor.fetchall = MagicMock(return_value=[[initialVersion]])
        
        self.thing.migrate_2_2_0();

        self.lapDb.execute.assert_called_once_with('PRAGMA user_version;')
        
    def testAutoMigration(self):
        initialVersion = 0
        self.cursor.fetchall = MagicMock(return_value=[[initialVersion]])
        
        self.thing.migrateDb()
        
        self.assertGreater(self.lapDb.execute.call_count, 0)
        
if __name__ == "__main__":
    unittest.main()
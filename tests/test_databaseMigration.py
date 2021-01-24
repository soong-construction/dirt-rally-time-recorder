import unittest

from unittest.mock import MagicMock
from timerecorder.databaseMigration import DatabaseMigration

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.lap_db = MagicMock()
        self.thing = DatabaseMigration(self.lap_db)

        self.cursor = MagicMock()
        self.lap_db.execute = MagicMock(return_value=self.cursor)

        self.cursor.fetchall = MagicMock(return_value=[[0]])

    def tearDown(self):
        pass

    def testUserVersion(self):
        userVersion = self.thing.getUserVersion()
        self.assertEqual(userVersion, 0, "user_version not 0")

    def testSetUserVersion(self):
        initialVersion = 1_000_000

        self.thing.setUserVersion(initialVersion)

        self.assertEqual(self.lap_db.execute.call_count, 1)
        self.lap_db.execute.assert_called_with('PRAGMA user_version = 1000000')

    def testVersionExpansion(self):
        expandVersion = self.thing.expandVersion('1.0.0')
        self.assertEqual(expandVersion, 1_000_000)

        expandVersion = self.thing.expandVersion('12.1.21')
        self.assertEqual(expandVersion, 12_001_021)

    def testVersionExpansionWithWhitespace(self):
        expandVersion = self.thing.expandVersion(' 1.2.3\r\n')
        self.assertEqual(expandVersion, 1_002_003)

    def testVersionExpansionWithIllegalVersion(self):
        with self.assertRaises(RuntimeError):
            self.thing.expandVersion('1.1')

    def testInitialMigrationFromVersion1_0_0(self):  #pylint: disable=invalid-name
        initialVersion = 1_000_000
        self.cursor.fetchall = MagicMock(return_value=[[initialVersion]])

        self.thing._migrate_2_2_0()

        self.assertEqual(self.lap_db.execute.call_count, 2)
        self.lap_db.execute.assert_called_with('PRAGMA user_version = 2002000')

    def testInitialMigrationSkipped(self):
        initialVersion = 2_002_000
        self.cursor.fetchall = MagicMock(return_value=[[initialVersion]])

        self.thing._migrate_2_2_0()

        self.lap_db.execute.assert_called_once_with('PRAGMA user_version;')

    def testAutoMigration(self):
        initialVersion = 0
        self.cursor.fetchall = MagicMock(return_value=[[initialVersion]])

        self.thing.migrateDb()

        self.assertGreater(self.lap_db.execute.call_count, 0)

if __name__ == "__main__":
    unittest.main()

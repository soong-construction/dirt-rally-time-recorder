import unittest

import time
from unittest.mock import MagicMock
from timerecorder.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.thing = Database('test')
        self.thing.database = MagicMock()

    def tearDown(self):
        pass

    def testLoadCars(self):
        cars = [(1, 'car1')]
        self.thing.database.fetchall = MagicMock(return_value=cars)

        loadedCars = self.thing.loadCars(1000, 100, 5)

        self.assertEqual(loadedCars, cars, "Did not return car")

    def testIdentifyCarNoResult(self):
        cars = []
        self.thing.database.fetchall = MagicMock(return_value=cars)

        loadedCars = self.thing.loadCars(1000, 100, 5)

        self.assertEqual(loadedCars, cars, "Did not return empty result")

    def testLoadTracksWithResults(self):
        tracks = [(1, 'track1'), (2, 'track2')]
        self.thing.database.fetchall = MagicMock(return_value=tracks)

        loadedTracks = self.thing.loadTracks(10000, 10)

        self.assertEqual(loadedTracks, tracks, "Did not return tracks")

    def testLoadTracksWithoutResults(self):
        tracks = []
        self.thing.database.fetchall = MagicMock(return_value=tracks)

        loadedTracks = self.thing.loadTracks(10000, 10)

        self.assertEqual(loadedTracks, tracks, "Did not return empty result")

    def testGetSingleCarUpdateStatements(self):
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

    def testGetCarInsertStatement(self):
        statement = self.thing.getCarInsertStatement(700, 200)

        self.assertEqual(statement, 'INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (ID, \'CAR_NAME\', 700, 200);')

    def testGetTrackInsertStatement(self):
        statement = self.thing.getTrackInsertStatement(10000, -1220)

        self.assertEqual(statement, 'INSERT INTO Tracks (id, name, length, startz) VALUES (ID, \'TRACK_NAME\', 10000, -1220);')

    def testGetUserId(self):
        userId = self.thing._createUserId()
        self.assertIsNotNone(userId, "userId must exist")

    def testUserIdDiffersOverTime(self):
        userId1 = self.thing._createUserId()
        time.sleep(1)
        userId2 = self.thing._createUserId()
        self.assertNotEqual(userId1, userId2, "userId must differ over time")

    def testRecordResultsWithoutTimeRecorded(self):
        conn = MagicMock()
        cursor = MagicMock()
        conn.cursor = MagicMock(return_value=cursor)
        cursor.execute = MagicMock()
        cursor.fetchone = MagicMock(return_value=None)
        self.thing._getLapDbConnection = MagicMock(return_value=conn)

        arguments = (100, 200, 1586278198.59, 220.4, 144)
        result = self.thing.recordResults(*arguments)
        self.assertIsNone(result)

        cursor.execute.assert_called_with('INSERT INTO laptimes (Track, Car, Timestamp, Time, Topspeed) VALUES (?, ?, ?, ?, ?)', arguments)
        conn.commit.assert_called_once()
        conn.close.assert_called_once()

    def testRecordResultsWithNewBestTime(self):
        conn = MagicMock()
        cursor = MagicMock()
        conn.cursor = MagicMock(return_value=cursor)
        cursor.execute = MagicMock()
        self.thing._getLapDbConnection = MagicMock(return_value=conn)

        previousBest = (1546275814.11, 230.4)
        cursor.fetchone = MagicMock(return_value=previousBest)

        arguments = (100, 200, 1586278198.59, 220.4, 144)
        result = self.thing.recordResults(*arguments)
        self.assertEqual(result, previousBest)

        cursor.execute.assert_called_with('INSERT INTO laptimes (Track, Car, Timestamp, Time, Topspeed) VALUES (?, ?, ?, ?, ?)', arguments)
        self.assertEqual(cursor.execute.call_count, 2)

        conn.commit.assert_called_once()
        conn.close.assert_called_once()

    def testRecordResultsWithStandingBestTime(self):
        conn = MagicMock()
        cursor = MagicMock()
        conn.cursor = MagicMock(return_value=cursor)
        cursor.execute = MagicMock()
        self.thing._getLapDbConnection = MagicMock(return_value=conn)

        previousBest = (1546275814.11, 210.4)
        cursor.fetchone = MagicMock(return_value=previousBest)

        arguments = (100, 200, 1586278198.59, 220.4, 144)
        result = self.thing.recordResults(*arguments)
        self.assertIsNone(result)

        cursor.execute.assert_called_with('INSERT INTO laptimes (Track, Car, Timestamp, Time, Topspeed) VALUES (?, ?, ?, ?, ?)', arguments)
        self.assertEqual(cursor.execute.call_count, 2)

        conn.commit.assert_called_once()
        conn.close.assert_called_once()

    def testInitializeLaptimeDbMigrationFails(self):
        conn = MagicMock()
        conn.commit = MagicMock()
        cursor = MagicMock()
        conn.cursor = MagicMock(return_value=cursor)
        cursor.execute = MagicMock()
        self.thing._migrate = MagicMock(side_effect=IOError)
        self.thing._getLapDbConnection = MagicMock(return_value=conn)

        self.thing.setUpLaptimesDb = MagicMock()
        self.thing._fetchUser = MagicMock()

        self.thing.initializeLaptimesDb()

        self.thing.setUpLaptimesDb.assert_called_once()
        conn.commit.assert_called_once()
        conn.close.assert_called_once()

    def testInitializeLaptimeDbFailsAltogether(self):
        conn = MagicMock()
        conn.cursor = MagicMock(side_effect=IOError)
        self.thing._getLapDbConnection = MagicMock(return_value=conn)
        self.thing.setUpLaptimesDb = MagicMock()

        # TODO Actually should terminate. TODO Same with recordResults
#         with self.assertRaises(IOError):
        self.thing.initializeLaptimesDb()

        self.thing.setUpLaptimesDb.assert_not_called()
        conn.commit.assert_not_called()
        conn.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()

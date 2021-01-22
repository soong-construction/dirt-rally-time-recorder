import unittest

from unittest.mock import MagicMock, call
from timerecorder.database import Database
from timerecorder.databaseAccess import DatabaseAccess

class TestDatabaseAccess(unittest.TestCase):

    def setUp(self):
        self.database = Database('test')
        self.database.recordResults = MagicMock()
        self.thing = DatabaseAccess(self.database)

    def tearDown(self):
        pass

    def testIdentifyTrackUnambiguous(self):
        tracks = [(1, 'track1')]
        self.database.loadTracks = MagicMock(return_value=tracks)

        loadedTrack = self.thing.identifyTrack(10, 10000)

        self.assertEqual(loadedTrack, 1, "Wrong ID")

    def testIdentifyTrackNoResult(self):
        tracks = []
        self.database.loadTracks = MagicMock(return_value=tracks)

        loadedTrack = self.thing.identifyTrack(10, 10000)

        self.assertEqual(loadedTrack, [], "Shouldn't identify track")

    def testIdentifyTrackAmbiguous(self):
        tracks = [(1, 'track1'), (2, 'track2')]
        self.database.loadTracks = MagicMock(return_value=tracks)

        loadedTrack = self.thing.identifyTrack(55, 10000)

        self.assertEqual(loadedTrack, [1, 2], "Should return all tracks")

    def testIdentifyCarUnambiguous(self):
        cars = [(1, 'car1')]
        self.database.loadCars = MagicMock(return_value=cars)

        loadedCar = self.thing.identifyCar(1000, 100, 5)

        self.assertEqual(loadedCar, 1, "Wrong ID")

    def testIdentifyCarNoResult(self):
        cars = []
        self.database.loadCars = MagicMock(return_value=cars)

        loadedCar = self.thing.identifyCar(1000, 100, 5)

        self.assertEqual(loadedCar, [], "Shouldn't identify car")

    def testIdentifyCarAmbiguous(self):
        cars = [(1, 'car1'), (2, 'car2')]
        self.database.loadCars = MagicMock(return_value=cars)

        loadedCar = self.thing.identifyCar(1000, 100, 5)
        self.assertEqual(loadedCar, [1, 2], "Should return all cars")

    def testGetCarInterfacesStatementWithoutData(self):
        handbrakeData = [(None)]
        self.database.loadHandbrakeData = MagicMock(side_effect=handbrakeData)
        carNames = ["Unknown Car"]
        noneData = [(None)]
        self.database.loadShiftingData = MagicMock(side_effect=noneData)
        self.database.loadGearsData = MagicMock(side_effect=noneData)
        self.database.loadClutchData = MagicMock(side_effect=noneData)

        self.database.getCarName = MagicMock(side_effect=carNames)

        self.assertEqual(self.thing.describeCarInterfaces([1]), "Unknown Car: NO CONTROL DATA")

    def testGetCarInterfacesStatements(self):
        handbrakeData = [(0), (1)]
        self.database.loadHandbrakeData = MagicMock(side_effect=handbrakeData)
        shiftingData = [('H-PATTERN'), ('2 PADDLES')]
        self.database.loadShiftingData = MagicMock(side_effect=shiftingData)
        carNames = ['Classic Car', 'Modern Car']
        self.database.getCarName = MagicMock(side_effect=carNames)
        gearsData = [(4), (6)]
        self.database.loadGearsData = MagicMock(side_effect=gearsData)
        clutchData = [(1), (0)]
        self.database.loadClutchData = MagicMock(side_effect=clutchData)

        firstCarInterface = self.thing.describeCarInterfaces(1)
        self.assertEqual(firstCarInterface, "Classic Car: H-PATTERN shifting, 4 speed, with manual CLUTCH")

        secondCarInterface = self.thing.describeCarInterfaces(2)
        self.assertEqual(secondCarInterface, "Modern Car: 2 PADDLES shifting, 6 speed, with HANDBRAKE")

    def testMapToShiftingData(self):
        shiftingData = [('H-PATTERN'), ('SEQUENTIAL')]
        self.database.loadShiftingData = MagicMock(side_effect=shiftingData)

        carCandidates = [100, 200]
        result = self.thing.mapCarsToShifting(carCandidates)

        self.assertEqual(list(result), [(100, 'H-PATTERN'), (200, 'SEQUENTIAL')])

    def testHandleCarUpdatesInvokesLambda(self):
        self.database.getCarUpdateStatements = MagicMock(return_value=['update100', 'update200'])

        carNames = ['Classic Car', 'Modern Car']
        self.database.getCarName = MagicMock(side_effect=carNames)

        updateHandler = MagicMock()
        self.thing.handleCarUpdates([100, 200], 123456789, [], updateHandler)

        call1 = call('UNKNOWN', 'Classic Car', 123456789, 'update100')
        call2 = call('UNKNOWN', 'Modern Car', 123456789, 'update200')

        updateHandler.assert_has_calls([call1, call2])

    def testHandleTrackUpdatesInvokesLambda(self):
        self.database.getTrackUpdateStatements = MagicMock(return_value=['update100', 'update200'])

        trackNames = ['Sprint', 'Complete']
        self.database.getTrackName = MagicMock(side_effect=trackNames)

        updateHandler = MagicMock()
        self.thing.handleTrackUpdates([100, 200], 123456789, [], updateHandler)

        call1 = call('Sprint', 'UNKNOWN', 123456789, 'update100')
        call2 = call('Complete', 'UNKNOWN', 123456789, 'update200')

        updateHandler.assert_has_calls([call1, call2])

if __name__ == "__main__":
    unittest.main()

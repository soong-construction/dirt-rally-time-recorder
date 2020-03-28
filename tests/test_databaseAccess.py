import unittest

from unittest.mock import MagicMock
from timerecorder.database import Database
from timerecorder.databaseAccess import DatabaseAccess

class TestDatabaseAccess(unittest.TestCase):


    def setUp(self):
        self.database = Database('test')
        self.database.recordResults = MagicMock()
        self.ambiguousResultHandler = MagicMock()
        self.thing = DatabaseAccess(self.database, self.ambiguousResultHandler)

    def tearDown(self):
        pass

    def testIdentifyTrackNoResult(self):
        tracks = []
        self.database.loadTracks = MagicMock(return_value=tracks)
        
        loadedTrack = self.thing.identifyTrack(10, 10000)

        self.assertEqual(loadedTrack, [], "Shouldn't identify track")

    def testIdentifyTrackUnambiguous(self):
        tracks = [(1, 'track1', 10)]
        self.database.loadTracks = MagicMock(return_value=tracks)
        
        loadedTrack = self.thing.identifyTrack(10, 10000)

        self.assertEqual(loadedTrack, 1, "Wrong ID")

    def testIdentifyTrackByZValue(self):
        tracks = [(1, 'track1', 10), (2, 'track2', 100)]
        self.database.loadTracks = MagicMock(return_value=tracks)
        
        loadedTrack = self.thing.identifyTrack(10, 10000)

        self.assertEqual(loadedTrack, 1, "Wrong ID")

    def testCannotIdentifyTrackByZValueIfIdentical(self):
        tracks = [(1, 'track1', 100), (2, 'track2', 100)]
        self.database.loadTracks = MagicMock(return_value=tracks)
        
        loadedTrack = self.thing.identifyTrack(100, 10000)

        self.assertEqual(loadedTrack, [1, 2], "Should return all tracks")

    def testIdentifyTrackAmbiguous(self):
        tracks = [(1, 'track1', 100), (2, 'track2', 100)]
        self.database.loadTracks = MagicMock(return_value=tracks)
        
        loadedTrack = self.thing.identifyTrack(10, 10000)

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
        
        car_candidates = [100, 200]
        result = self.thing.mapCarsToShifting(car_candidates)
        
        self.assertEqual(list(result), [(100, 'H-PATTERN'), (200,'SEQUENTIAL')])
        
if __name__ == "__main__":
    unittest.main()
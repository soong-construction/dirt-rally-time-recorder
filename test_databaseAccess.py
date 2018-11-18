import unittest

from unittest.mock import MagicMock
from database import Database
from databaseAccess import DatabaseAccess

class TestDatabaseAccess(unittest.TestCase):


    def setUp(self):
        self.database = Database('test')
        self.thing = DatabaseAccess(self.database)

    def tearDown(self):
        pass


    def testIdentifyTrackUnambiguous(self):
        tracks = [(1, 'track1', 10)]
        self.database.loadTracks = MagicMock(return_value=tracks)
        
        loadedTrack = self.thing.identifyTrack(10, 10000)

        self.assertEqual(loadedTrack, 1, "Wrong ID")

    def testIdentifyTrackByZValue(self):
        tracks = [(1, 'track1', 100), (2, 'track2', 10)]
        self.database.loadTracks = MagicMock(return_value=tracks)
        
        loadedTrack = self.thing.identifyTrack(10, 10000)

        self.assertEqual(loadedTrack, 2, "Wrong ID")

    def testIdentifyTrackByAmbiguous(self):
        tracks = [(1, 'track1', 100), (2, 'track2', 100)]
        self.database.loadTracks = MagicMock(return_value=tracks)
        
        loadedTrack = self.thing.identifyTrack(10, 10000)

        self.assertEqual(loadedTrack, -1, "Shouldn't identify track")

    def testIdentifyCarUnambiguous(self):
        cars = [(1, 'car1')]
        self.database.loadCars = MagicMock(return_value=cars)
        
        loadedCar = self.thing.identifyCar(100, 1000)

        self.assertEqual(loadedCar, 1, "Wrong ID")

    def testIdentifyCarNoResult(self):
        cars = []
        self.database.loadCars = MagicMock(return_value=cars)
        
        loadedCar = self.thing.identifyCar(100, 1000)

        self.assertEqual(loadedCar, [], "Shouldn't identify car")

    def testIdentifyCarAmbiguous(self):
        cars = [(1, 'car1'), (2, 'car2')]
        self.database.loadCars = MagicMock(return_value=cars)
        
        loadedCar = self.thing.identifyCar(100, 1000)
        self.assertEqual(loadedCar, [1, 2], "Should return all cars")

    def testHandleResultsWithAmbiguousCars(self):
        cars = [(1, 'car1'), (2, 'car2')]
        
        self.database.getCarName = MagicMock(side_effect=list(name for (_,name) in cars))
        
        self.thing.recordResults(100, cars, 234.44)
        
    def testHasHandbrake(self):
        data = [(1), (0), (None)]
        self.database.loadHandbrakeData = MagicMock(side_effect=data)
        
        self.assertEqual(self.thing.hasHandbrake(1), True)
        self.assertEqual(self.thing.hasHandbrake(2), False)
        self.assertEqual(self.thing.hasHandbrake(-1), None)
    
    def testGetCarInterfacesStatementWithoutData(self):
        handbrakeData = [(None)]
        self.database.loadHandbrakeData = MagicMock(side_effect=handbrakeData)
        carNames = ["Unknown Car"]
        noneData = [(None)]
        self.database.loadShiftingData = MagicMock(side_effect=noneData)
        self.database.loadGearsData = MagicMock(side_effect=noneData)
        
        self.database.getCarName = MagicMock(side_effect=carNames)
        
        self.assertEqual(self.thing.describeCarInterfaces([1]), "Unknown Car: NO CONTROL DATA")

    def testGetCarInterfacesStatementAllControls(self):
        handbrakeData = [(1)]
        self.database.loadHandbrakeData = MagicMock(side_effect=handbrakeData)
        shiftingData = [('H-PATTERN')]
        self.database.loadShiftingData = MagicMock(side_effect=shiftingData)
        carNames = ["Classic Car"]
        self.database.getCarName = MagicMock(side_effect=carNames)
        gearsData = [(4)]
        self.database.loadGearsData = MagicMock(side_effect=gearsData)
        
        carInterfaceLines = self.thing.describeCarInterfaces([1])

        self.assertEqual(carInterfaceLines, "Classic Car: H-PATTERN shifting, 4 speed, with HANDBRAKE")
        
    def testDemoOutput(self):
        print("Ford Focus RS Rally 2007: PADDLE shifting, 6 speed, with HANDBRAKE")
        print("Audi Sport Quattro Rallye: H-PATTERN shifting, clutch PEDAL, 5 speed")

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestDatabaseAccess.testIdentifyTrackUnambiguous']
    unittest.main()
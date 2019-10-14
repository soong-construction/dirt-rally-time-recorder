import time
from ambiguousResultHandler import AmbiguousResultHandler

class DatabaseAccess:
    
    def __init__(self, database):
        self.database = database
        self.ambiguousResultHandler = AmbiguousResultHandler()
    
    def identifyTrack(self, z, tracklength):
        tracks = self.database.loadTracks(tracklength)

        if (len(tracks) == 0):
            print("Failed to identify track: %s" % (str(tracklength)))
            return []
        
        elif (len(tracks) == 1):
            index, name, startZ = tracks[0]
            print("TRACK: %s" % str(name))
            return index
        
        elif (len(tracks) == 2):
            
            matchingTrack = None
            lastZ = None
            for index, name, startZ in tracks:
                # Cannot distinguish Pikes Peak tracks which are identical 
                tracksDiffer = lastZ != startZ
                matchingZ = tracksDiffer and abs(z - startZ) < 50
                matchingTrack = (index, name) if matchingZ else matchingTrack
                lastZ = startZ
                
            if matchingTrack and tracksDiffer:
                index, name = matchingTrack
                print("TRACK: %s" % (str(name)))
                return index
        
        print("Ambiguous track data, %s matches: %s (Z: %s)" % (len(tracks), str(tracklength), str(z)))
        return list(index for (index, name, startZ) in tracks)
    
    def logCar(self, rpm, max_rpm, name):
        print("CAR: %s (%s - %s)" % (name, str(rpm), str(max_rpm)))

    def identifyCar(self, rpm, max_rpm):
        cars = self.database.loadCars(rpm, max_rpm)
        if (len(cars) == 0):
            print("Failed to identify car: %s - %s" % (str(rpm), str(max_rpm)))
            return []
        
        elif (len(cars) == 1):
            index, name = cars[0]
            self.logCar(rpm, max_rpm, name)
            return index
        
        else:
            print("Ambiguous car data, %s matches: %s - %s" % (len(cars), str(rpm), str(max_rpm)))
            return list(index for (index, name) in cars)


    def printCarUpdates(self, car, timestamp):
        updates = self.database.getCarUpdateStatements(timestamp, car)
        print("Please update the recorded laptimes according to the correct car:")
        for index, update in enumerate(updates):
            elementId = car[index]
            carName = self.database.getCarName(elementId)
            print("%s ==> %s" % (carName, update))


    def handleTrackUpdates(self, track, timestamp, car):
        updates = self.database.getTrackUpdateStatements(timestamp, track)
        print("Please update the recorded laptimes according to the correct track:")
        for index, update in enumerate(updates):
            elementId = track[index]
            trackName = self.database.getTrackName(elementId)
            carName = self.database.getCarName(car) if self.identify(car) != -1 else '???'
            
            script = self.ambiguousResultHandler.handleUpdateStatement(trackName, carName, timestamp, update)
            
            print("%s ==> run %s" % (trackName, script))

    def recordResults(self, track, car, laptime):
        timestamp = time.time()
        self.database.recordResults(self.identify(track), self.identify(car), timestamp, laptime)
        
        if isinstance(car, (list,)):
            self.printCarUpdates(car, timestamp, track)
                
        if isinstance(track, (list,)):
            self.handleTrackUpdates(track, timestamp, car)

    def identify(self, element):
        return element if isinstance(element, int) else -1

    def describeHandbrake(self, car):
        hasHandbrake = self.database.loadHandbrakeData(car)
        if (hasHandbrake):
            return "with HANDBRAKE" + ", "
        return ""

    def describeShifting(self, car):
        shiftingData = self.database.loadShiftingData(car)
        return shiftingData + " shifting, " if shiftingData else ""

    def describeGears(self, car):
        gearData = self.database.loadGearsData(car)
        return str(gearData) + " speed, " if gearData else ""

    def describeClutch(self, car):
        hasClutchPedal = self.database.loadClutchData(car)
        if (hasClutchPedal):
            return "with manual CLUTCH" + ", "
        return ""

    def describeCarInterfaces(self, car):
        line = ""
        line += self.describeShifting(car)
        line += self.describeGears(car)
        line += self.describeClutch(car)
        line += self.describeHandbrake(car)
        
        if (line == ""):
            line = "NO CONTROL DATA"
        else:
            line = line[:-2]
            
        return self.database.getCarName(car) + ": " + line

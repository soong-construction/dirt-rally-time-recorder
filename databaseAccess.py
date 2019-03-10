import time

class DatabaseAccess:
    
    def __init__(self, database):
        self.database = database
    
    def identifyTrack(self, z, tracklength):
        tracks = self.database.loadTracks(tracklength)

        if (len(tracks) == 1):
            index, name, startz = tracks[0]
            print("TRACK: %s" % str(name))
            return index
        
        elif (len(tracks) > 1):
            for index, name, startz in tracks:
                if abs(z - startz) < 50:
                    print("TRACK: %s (Z: %s)" % (str(name), str(z)))
                    return index
        
        else:
            print("Failed to identify track: %s (Z: %s)" % (str(tracklength), str(z)))
        
        return -1
    
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

    def recordResults(self, track, car, laptime):
        timestamp = time.time()
        self.database.recordResults(track, car if isinstance(car, int) else -1, timestamp, laptime)
        
        if isinstance(car, (list,)):
            updates = self.database.getUpdateStatements(timestamp, car)
            print("Please update the recorded laptimes according to the correct car:")
            
            for index, update in enumerate(updates):
                carId = car[index]
                carName = self.database.getCarName(carId)
                print("%s ==> %s" % (carName, update))

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

    # TODO #6 Include clutch
    def describeCarInterfaces(self, car):
        line = ""
        line += self.describeShifting(car)
        line += self.describeGears(car)
        line += self.describeHandbrake(car)
        
        if (line == ""):
            line = "NO CONTROL DATA"
        else:
            line = line[:-2]
            
        return self.database.getCarName(car) + ": " + line

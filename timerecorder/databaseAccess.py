from .log import getLogger, VERBOSE

logger = getLogger(__name__)

def identify(element):
    return element if isinstance(element, int) else -1

class DatabaseAccess:
    
    def __init__(self, database, ambiguousResultHandler):
        self.database = database
        self.ambiguousResultHandler = ambiguousResultHandler
    
    def identifyTrack(self, z, tracklength):
        tracks = self.database.loadTracks(tracklength)

        if (len(tracks) == 0):
            logger.warning("Failed to identify track")
            logger.debug("Length: %s", str(tracklength))
            logger.log(VERBOSE, self.database.getTrackInsertStatement(tracklength, z))
            
            return []
        
        elif (len(tracks) == 1):
            index, name, startZ = tracks[0]
            logger.info("TRACK: %s", str(name))
            return index
        
        # TODO Can't Z-based recognition be part of the SQL query? Looks much too complicated...
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
                logger.info("TRACK: %s", str(name))
                return index
        
        logger.warning("Ambiguous track data, %s matches", len(tracks))
        logger.debug("Length: %s (Z: %s)", str(tracklength), str(z))
        return list(index for (index, name, startZ) in tracks)
    
    def logCar(self, name):
        logger.info("CAR: %s", name)

    def identifyCar(self, max_rpm, idle_rpm, top_gear):
        cars = self.database.loadCars(idle_rpm, max_rpm, top_gear)
        if (len(cars) == 0):
            logger.warning("Failed to identify car")
            logger.debug("Idle/Max RPM: %s - %s", str(idle_rpm), str(max_rpm))
            logger.log(VERBOSE, self.database.getCarInsertStatement(max_rpm, idle_rpm))
            
            return []
        
        elif (len(cars) == 1):
            index, name = cars[0]
            self.logCar(name)
            return index
        
        else:
            logger.warning("Ambiguous car data, %s matches", len(cars))
            logger.debug("Idle/Max RPM: %s - %s", str(idle_rpm), str(max_rpm))
            return list(index for (index, name) in cars)

    def handleCarUpdates(self, car_list, timestamp, track):
        updates = self.database.getCarUpdateStatements(timestamp, car_list)
        for index, update in enumerate(updates):
            elementId = car_list[index]
            carName = self.database.getCarName(elementId)
            trackName = self.database.getTrackName(track) if identify(track) != -1 else 'UNKNOWN'
            
            scriptName = self.ambiguousResultHandler.writeScript(trackName, carName, timestamp, update)
            
            logger.info(" ==> %s", scriptName)

    def handleTrackUpdates(self, track_list, timestamp, car):
        updates = self.database.getTrackUpdateStatements(timestamp, track_list)
        for index, update in enumerate(updates):
            elementId = track_list[index]
            trackName = self.database.getTrackName(elementId)
            carName = self.database.getCarName(car) if identify(car) != -1 else 'UNKNOWN'
            
            scriptName = self.ambiguousResultHandler.writeScript(trackName, carName, timestamp, update)
            
            logger.info(" ==> %s", scriptName)

    def mapCarsToShifting(self, car_candidates):
        shifting_data = map(self.database.loadShiftingData, car_candidates)
        return zip(car_candidates, shifting_data)
    
    def recordResults(self, track, car, timestamp, laptime, topspeed):
        self.database.recordResults(track, car, timestamp, laptime, topspeed)
        
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

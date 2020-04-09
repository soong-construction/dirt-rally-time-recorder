import time
from log import getLogger

logger = getLogger(__name__)

class DatabaseAccess:
    
    def __init__(self, database, ambiguousResultHandler):
        self.database = database
        self.ambiguousResultHandler = ambiguousResultHandler
    
    def identifyTrack(self, z, tracklength):
        tracks = self.database.loadTracks(tracklength)

        if (len(tracks) == 0):
            logger.warning("Failed to identify track")
            logger.debug("Length: %s", str(tracklength))
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
            return []
        
        elif (len(cars) == 1):
            index, name = cars[0]
            self.logCar(name)
            return index
        
        else:
            logger.warning("Ambiguous car data, %s matches", len(cars))
            logger.debug("Idle/Max RPM: %s - %s", str(idle_rpm), str(max_rpm))
            return list(index for (index, name) in cars)


    def printCarUpdates(self, car, timestamp, track):
        updates = self.database.getCarUpdateStatements(timestamp, car)
        logger.info("Please run one of the scripts below to link the recorded laptime to the correct car:")
        for index, update in enumerate(updates):
            elementId = car[index]
            carName = self.database.getCarName(elementId)
            trackName = self.database.getTrackName(track) if self.identify(track) != -1 else 'UNKNOWN'
            
            script = self.ambiguousResultHandler.handleUpdateStatement(trackName, carName, timestamp, update)
            
            logger.info(" ==> %s", script)

    def handleTrackUpdates(self, track, timestamp, car):
        updates = self.database.getTrackUpdateStatements(timestamp, track)
        logger.info("Please run one of the scripts below to link the recorded laptime to the correct track:")
        for index, update in enumerate(updates):
            elementId = track[index]
            trackName = self.database.getTrackName(elementId)
            carName = self.database.getCarName(car) if self.identify(car) != -1 else 'UNKNOWN'
            
            script = self.ambiguousResultHandler.handleUpdateStatement(trackName, carName, timestamp, update)
            
            logger.info(" ==> %s", script)

    def recordResults(self, track, car, laptime, topspeed):
        timestamp = time.time()
        self.database.recordResults(self.identify(track), self.identify(car), timestamp, laptime, topspeed)
        
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

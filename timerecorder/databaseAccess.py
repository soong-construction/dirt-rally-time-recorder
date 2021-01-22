'''
Abstraction for the database, allowing for tests
'''
from .log import getLogger, VERBOSE

logger = getLogger(__name__)
AMBIGUOUS = -1

def identify(element):
    return element if isinstance(element, int) else AMBIGUOUS

class DatabaseAccess:

    def __init__(self, database):
        self.database = database

    def _tryIdentify(self, it, itList, debugLog, verboseLog):
        if len(itList) == 0:
            logger.warning("Failed to identify %s", it)
            debugLog(logger)
            verboseLog(logger, self.database)

            return []

        if len(itList) == 1:
            index, _ = itList[0]
            return index

        logger.warning("Ambiguous %s data, %s matches", it, len(itList))
        debugLog(logger)

        return list(index for (index, _) in itList)

    def identifyTrack(self, startZ, tracklength):
        debugLog = lambda logger: logger.debug("Length: %s (Z: %s)", str(tracklength), str(startZ))
        verboseLog = lambda logger, db: logger.log(VERBOSE, db.getTrackInsertStatement(tracklength, startZ))

        itList = self.database.loadTracks(tracklength, startZ)
        return self._tryIdentify("track", itList, debugLog, verboseLog)

    def identifyCar(self, maxRpm, idleRpm, topGear):
        debugLog = lambda logger: logger.debug("Idle/Max RPM: %s - %s", str(idleRpm), str(maxRpm))
        verboseLog = lambda logger, db: logger.log(VERBOSE, db.getCarInsertStatement(maxRpm, idleRpm))

        itList = self.database.loadCars(idleRpm, maxRpm, topGear)

        return self._tryIdentify("car", itList, debugLog, verboseLog)

    def handleCarUpdates(self, carList, timestamp, track, updateHandler):
        updates = self.database.getCarUpdateStatements(timestamp, carList)
        for index, update in enumerate(updates):
            elementId = carList[index]
            carName = self.database.getCarName(elementId)
            trackName = self.database.getTrackName(track) if identify(track) != AMBIGUOUS else 'UNKNOWN'

            updateHandler(trackName, carName, timestamp, update)

    def handleTrackUpdates(self, trackList, timestamp, car, updateHandler):
        updates = self.database.getTrackUpdateStatements(timestamp, trackList)
        for index, update in enumerate(updates):
            elementId = trackList[index]
            trackName = self.database.getTrackName(elementId)
            carName = self.database.getCarName(car) if identify(car) != AMBIGUOUS else 'UNKNOWN'

            updateHandler(trackName, carName, timestamp, update)

    def mapCarsToShifting(self, carCandidates):
        shiftingData = map(self.database.loadShiftingData, carCandidates)
        return zip(carCandidates, shiftingData)

    def recordResults(self, track, car, timestamp, laptime, topspeed):
        return self.database.recordResults(track, car, timestamp, laptime, topspeed)

    def _describeHandbrake(self, car):
        hasHandbrake = self.database.loadHandbrakeData(car)
        if hasHandbrake:
            return "with HANDBRAKE" + ", "
        return ""

    def _describeShifting(self, car):
        shiftingData = self.database.loadShiftingData(car)
        return shiftingData + " shifting, " if shiftingData else ""

    def _describeGears(self, car):
        gearData = self.database.loadGearsData(car)
        return str(gearData) + " speed, " if gearData else ""

    def _describeClutch(self, car):
        hasClutchPedal = self.database.loadClutchData(car)
        if hasClutchPedal:
            return "with manual CLUTCH" + ", "
        return ""

    def describeCarInterfaces(self, car):
        line = ""
        line += self._describeShifting(car)
        line += self._describeGears(car)
        line += self._describeClutch(car)
        line += self._describeHandbrake(car)

        if line == "":
            line = "NO CONTROL DATA"
        else:
            line = line[:-2]

        return self.database.getCarName(car) + ": " + line

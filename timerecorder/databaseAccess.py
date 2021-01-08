from .log import getLogger, VERBOSE

logger = getLogger(__name__)
AMBIGUOUS = -1

def identify(element):
    return element if isinstance(element, int) else AMBIGUOUS

class DatabaseAccess:

    def __init__(self, database):
        self.database = database

    # TODO Identify methods are copy code
    def identifyTrack(self, z, tracklength):
        tracks = self.database.loadTracks(tracklength, z)

        if (len(tracks) == 0):
            logger.warning("Failed to identify track")
            logger.debug("Length: %s", str(tracklength))
            logger.log(VERBOSE, self.database.getTrackInsertStatement(tracklength, z))

            return []

        elif (len(tracks) == 1):
            index, _ = tracks[0]
            return index

        logger.warning("Ambiguous track data, %s matches", len(tracks))
        logger.debug("Length: %s (Z: %s)", str(tracklength), str(z))
        return list(index for (index, _) in tracks)

    def identifyCar(self, max_rpm, idle_rpm, top_gear):
        cars = self.database.loadCars(idle_rpm, max_rpm, top_gear)
        if (len(cars) == 0):
            logger.warning("Failed to identify car")
            logger.debug("Idle/Max RPM: %s - %s", str(idle_rpm), str(max_rpm))
            logger.log(VERBOSE, self.database.getCarInsertStatement(max_rpm, idle_rpm))

            return []

        elif (len(cars) == 1):
            index, _ = cars[0]
            return index

        else:
            logger.warning("Ambiguous car data, %s matches", len(cars))
            logger.debug("Idle/Max RPM: %s - %s", str(idle_rpm), str(max_rpm))
            return list(index for (index, _) in cars)

    def handleCarUpdates(self, car_list, timestamp, track, updateHandler):
        updates = self.database.getCarUpdateStatements(timestamp, car_list)
        for index, update in enumerate(updates):
            elementId = car_list[index]
            carName = self.database.getCarName(elementId)
            trackName = self.database.getTrackName(track) if identify(track) != AMBIGUOUS else 'UNKNOWN'

            updateHandler(trackName, carName, timestamp, update)

    def handleTrackUpdates(self, track_list, timestamp, car, updateHandler):
        updates = self.database.getTrackUpdateStatements(timestamp, track_list)
        for index, update in enumerate(updates):
            elementId = track_list[index]
            trackName = self.database.getTrackName(elementId)
            carName = self.database.getCarName(car) if identify(car) != AMBIGUOUS else 'UNKNOWN'

            updateHandler(trackName, carName, timestamp, update)

    def mapCarsToShifting(self, car_candidates):
        shifting_data = map(self.database.loadShiftingData, car_candidates)
        return zip(car_candidates, shifting_data)

    def recordResults(self, track, car, timestamp, laptime, topspeed):
        return self.database.recordResults(track, car, timestamp, laptime, topspeed)

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

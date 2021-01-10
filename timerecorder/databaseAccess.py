from .log import getLogger, VERBOSE

logger = getLogger(__name__)
AMBIGUOUS = -1

def identify(element):
    return element if isinstance(element, int) else AMBIGUOUS

class DatabaseAccess:

    def __init__(self, database):
        self.database = database

    def tryIdentify(self, it, it_list, debug_log, verbose_log):
        if len(it_list) == 0:
            logger.warning("Failed to identify %s", it)
            debug_log(logger)
            verbose_log(logger, self.database)

            return []

        if len(it_list) == 1:
            index, _ = it_list[0]
            return index

        logger.warning("Ambiguous %s data, %s matches", it, len(it_list))
        debug_log(logger)

        return list(index for (index, _) in it_list)

    def identifyTrack(self, z, tracklength):
        debug_log = lambda logger: logger.debug("Length: %s (Z: %s)", str(tracklength), str(z))
        verbose_log = lambda logger, db: logger.log(VERBOSE, db.getTrackInsertStatement(tracklength, z))

        it_list = self.database.loadTracks(tracklength, z)
        return self.tryIdentify("track", it_list, debug_log, verbose_log)

    def identifyCar(self, max_rpm, idle_rpm, top_gear):
        debug_log = lambda logger: logger.debug("Idle/Max RPM: %s - %s", str(idle_rpm), str(max_rpm))
        verbose_log = lambda logger, db: logger.log(VERBOSE, db.getCarInsertStatement(max_rpm, idle_rpm))

        it_list = self.database.loadCars(idle_rpm, max_rpm, top_gear)

        return self.tryIdentify("car", it_list, debug_log, verbose_log)

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
        if hasHandbrake:
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
        if hasClutchPedal:
            return "with manual CLUTCH" + ", "
        return ""

    def describeCarInterfaces(self, car):
        line = ""
        line += self.describeShifting(car)
        line += self.describeGears(car)
        line += self.describeClutch(car)
        line += self.describeHandbrake(car)

        if line == "":
            line = "NO CONTROL DATA"
        else:
            line = line[:-2]

        return self.database.getCarName(car) + ": " + line

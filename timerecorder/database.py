import sqlite3
import getpass
import time
from .databaseMigration import DatabaseMigration
from .log import getLogger
from . import config

UPDATE_STATEMENT = 'UPDATE laptimes SET {}={} WHERE Timestamp="{}";'

logger = getLogger(__name__)

class Database:

    laptimesDbName = 'dirtrally-laptimes.db'
    laptimesDb = '/' + laptimesDbName
    baseDb = '/dirtrally-lb.db'

    def __init__(self, approot):
        self.approot = approot

    def setup(self):
        try:
            conn = sqlite3.connect(self.approot + self.baseDb)
            db = conn.cursor()
            trackCount = db.execute('SELECT count(*) FROM Tracks').fetchall()[0]
            carCount = db.execute('SELECT count(*) FROM cars').fetchall()[0]
            logger.info('Found %s tracks and %s cars', trackCount[0], carCount[0])
            self.db = db
            return self
        except Exception as exc:
            logger.exception("Error when reading from %s, please check set-up instructions in the README", self.baseDb)
            raise exc

    def fetchUser(self, lapdb):
        lapdb.execute('SELECT user FROM user;')
        res = lapdb.fetchall()
        userArray = res[0]
        return userArray

    def setDbVersion(self, lapdb):
        migration = DatabaseMigration(lapdb)
        versionString = config.readVersion(self.approot)
        version = migration.expandVersion(versionString)
        migration.setUserVersion(version)

    def setupLaptimesDb(self, lapdb):
        logger.debug("First run, setting up recording tables")
        lapdb.execute('CREATE TABLE laptimes (Track INTEGER, Car INTEGER, Timestamp INTEGER, Time REAL, Topspeed REAL);')
        lapdb.execute('CREATE TABLE user (user TEXT);')
        userId = self.createUserId()
        lapdb.execute('INSERT INTO user VALUES (?)', (userId, ))

        self.setDbVersion(lapdb)

    def migrate(self, lapdb):
        logger.info("Checking laptimes database")
        DatabaseMigration(lapdb).migrateDb()

    def initializeLaptimesDb(self):
        try:
            lapconn = self.getLapDbConnection()
            lapdb = lapconn.cursor()

            self.migrate(lapdb)
            lapconn.commit()
            return self.fetchUser(lapdb)

        except Exception:
            try:
                self.setupLaptimesDb(lapdb)
                lapconn.commit()
                return self.fetchUser(lapdb)

            except Exception:
                logger.exception("Error initializing %s", self.laptimesDbName)

        finally:
            lapconn.close()

    def createUserId(self):
        user = getpass.getuser()
        user = 'defaultuser' if user is None else user
        epoch = int(time.time())
        return str(user) + str(epoch)

    def loadTracks(self, tracklength, startz):
        select = ('SELECT id, name '
                    'FROM Tracks '
                    'WHERE abs(length - ?) < 0.001 AND (startz is null OR abs(startz - ?) < 50)')
        self.db.execute(select, (tracklength, startz))
        return self.db.fetchall()

    def loadCars(self, idle_rpm, max_rpm, top_gear):
        select = ('SELECT cars.id, cars.name '
                    'FROM cars INNER JOIN controls USING(id) '
                    'WHERE abs(cars.maxrpm - ?) < 1.0 AND abs(cars.idlerpm - ?) < 1.0 AND controls.topgear = ? '
                    'ORDER BY cars.id ASC')
        self.db.execute(select, (max_rpm, idle_rpm, top_gear))
        return self.db.fetchall()

    def getLapDbConnection(self):
        return sqlite3.connect(self.approot + self.laptimesDb)

    def compareTime(self, previousBest, laptime):
        return previousBest if laptime < previousBest[1] else None

    def recordResults(self, track, car, timestamp, laptime, topspeed):
        try:
            lapconn = self.getLapDbConnection()
            lapdb = lapconn.cursor()
            lapdb.execute('SELECT Timestamp, Time '
                          'FROM laptimes '
                          'WHERE Track = ? AND Car = ? '
                          'ORDER BY Time ASC, Timestamp ASC', (track, car))
            fetch = lapdb.fetchone()
            previous_best = self.compareTime(fetch, laptime) if fetch else None

            lapdb.execute('INSERT INTO laptimes (Track, Car, Timestamp, Time, Topspeed) VALUES (?, ?, ?, ?, ?)', (track, car, timestamp, laptime, topspeed))
            lapconn.commit()
            lapconn.close()

            return previous_best
        except Exception:
            logger.exception("Error connecting to %s", self.laptimesDbName)

    @staticmethod
    def getCarUpdateStatements(timestamp, cars):
        to_update = lambda car: UPDATE_STATEMENT.format('Car', car, timestamp)
        return list(map(to_update, cars))

    @staticmethod
    def getTrackUpdateStatements(timestamp, tracks):
        to_update = lambda track: UPDATE_STATEMENT.format('Track', track, timestamp)
        return list(map(to_update, tracks))

    def getCarInsertStatement(self, max_rpm, idle_rpm):
        return f'INSERT INTO cars (id, name, maxrpm, idlerpm) VALUES (ID, \'CAR_NAME\', {max_rpm}, {idle_rpm});'

    def getTrackInsertStatement(self, tracklength, z):
        return f'INSERT INTO Tracks (id, name, length, startz) VALUES (ID, \'TRACK_NAME\', {tracklength}, {z});'

    def getCarName(self, car):
        self.db.execute('SELECT name FROM cars WHERE id = ?', (car,))
        return self.db.fetchone()[0]

    def getTrackName(self, track):
        self.db.execute('SELECT name FROM Tracks WHERE id = ?', (track,))
        return self.db.fetchone()[0]

    def loadHandbrakeData(self, car):
        self.db.execute('SELECT handbrake FROM controls WHERE id = ?', (car,))
        fetch = self.db.fetchone()
        return bool(fetch[0]) if fetch else None

    def loadShiftingData(self, car):
        self.db.execute('SELECT shifting FROM controls WHERE id = ?', (car,))
        fetch = self.db.fetchone()
        return fetch[0] if fetch else None

    def loadClutchData(self, car):
        self.db.execute('SELECT manualclutch FROM controls WHERE id = ?', (car,))
        fetch = self.db.fetchone()
        return bool(fetch[0]) if fetch else None

    def loadGearsData(self, car):
        self.db.execute('SELECT topgear FROM controls WHERE id = ?', (car,))
        fetch = self.db.fetchone()
        return fetch[0] if fetch else None

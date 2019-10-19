import sqlite3
import getpass
import time

UPDATE_STATEMENT = 'UPDATE laptimes SET %s=%s WHERE Timestamp="%s";'


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
            print('Found %s tracks and %s cars' % (trackCount[0], carCount[0]))
            self.db = db
            return self
        except (Exception) as exc:
            print("Error when reading from %s, please check set-up instructions in the README" % (self.baseDb))
            raise exc

    def initializeLaptimesDb(self):
        try:
            lapconn = sqlite3.connect(self.approot + self.laptimesDb)
            lapdb = lapconn.cursor()
            lapdb.execute('SELECT user FROM user;')
            res = lapdb.fetchall()
            userArray = res[0]
        except (Exception) as exc:
            try:
                print("First run, setting up recording tables")
                lapdb.execute('CREATE TABLE laptimes (Track INTEGER, Car INTEGER, Timestamp INTEGER, Time REAL);')
                
                lapdb.execute('CREATE TABLE user (user TEXT);')
                userId = self.createUserId()
                lapdb.execute('INSERT INTO user VALUES (?)', (userId,))
                lapconn.commit()
                lapdb.execute('SELECT user FROM user;')
                res = lapdb.fetchall()
                userArray = res[0]
            except (Exception) as exc:
                print("Error initializing " + self.laptimesDb, exc)
        finally:
            lapconn.close()
        
        return userArray
    
    def createUserId(self):
        user = getpass.getuser()
        user = 'defaultuser' if (user == None) else user
        epoch = int(time.time())
        return str(user) + str(epoch)

    def loadTracks(self, tracklength):
        self.db.execute('SELECT id, name, startz FROM Tracks WHERE abs(length - ?) < 0.001', (tracklength,))
        return self.db.fetchall()

    def loadCars(self, rpm, max_rpm):
        # Some more delta allowed for startrpm as 2nd Pikes Peak run seems to simulate worn/warmed up engine
        # (1.0 - ?) = deviation rate. To account for varying rpm reported via UDP (DR2), allow some slack
        carSelectStatement = 'SELECT id, name FROM cars WHERE abs(maxrpm - ?) < 0.01 AND startrpm > (1.0 - ?) * ? AND startrpm <= ?'
        self.db.execute(carSelectStatement, (max_rpm, 0.01, rpm, rpm))
        result = self.db.fetchall()
        if (len(result) == 0):
            fuzzyFactor = 0.2
            print("No car matched, trying to fuzzy match (%s deviation)..." % (fuzzyFactor, ))
            self.db.execute(carSelectStatement, (max_rpm, fuzzyFactor, rpm, rpm))
            result = self.db.fetchall()
        return result

    def recordResults(self, track, car, timestamp, laptime):
        try:
            lapconn = sqlite3.connect(self.approot + self.laptimesDb)
            lapdb = lapconn.cursor()
            lapdb.execute('INSERT INTO laptimes (Track, Car, Timestamp, Time) VALUES (?, ?, ?, ?)', (track, car, timestamp, laptime))
            lapconn.commit()
            lapconn.close()
        except (Exception) as exc:
            print("Error connecting to database:", exc)
            
    def getCarUpdateStatements(self, timestamp, cars):
        result = []
        for index in cars:
            result.append(UPDATE_STATEMENT % ('Car', index, timestamp))
        
        return result
    
    def getTrackUpdateStatements(self, timestamp, tracks):
        # TODO #8 Debug
        if len(tracks) == 0:
            print(UPDATE_STATEMENT % ('Track', 'NEW-ID', timestamp))

        result = []
        for track in tracks:
            result.append(UPDATE_STATEMENT % ('Track', track, timestamp))
        
        return result

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
        self.db.execute('SELECT forwardgears FROM controls WHERE id = ?', (car,))
        fetch = self.db.fetchone()
        return fetch[0] if fetch else None

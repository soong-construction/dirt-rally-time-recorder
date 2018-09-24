import sqlite3
import time


class Database:
    
    laptimesDb = '\dirtrally-laptimes.db'
    
    def __init__(self, approot):
        self.approot = approot
        self.db = self.checkSetup(approot)
        self.track = None
        self.car = None
    
    def checkSetup(self, approot):
        try:
            conn = sqlite3.connect(approot + '/dirtrally-lb.db')
            db = conn.cursor()
            return db
        except (Exception) as exc:
            # TODO Set it up with tracks.sql and cars.sql
            print("Error connecting to database:", exc)

    def initializeLaptimesDb(self):
        try:
            lapconn = sqlite3.connect(self.approot + self.laptimesDb)
            lapdb = lapconn.cursor()
            lapdb.execute('SELECT user,pass FROM user;')
            res = lapdb.fetchall()
            userArray = res[0]
        except (Exception) as exc:
            try:
                print("Trying to init the db", exc)
                lapdb.execute('CREATE TABLE laptimes (Track INTEGER, Car INTEGER, Timestamp INTEGER, Time REAL);')
                lapdb.execute('CREATE TABLE user (user TEXT, pass TEXT);')
                # TODO Read username from config.yml
                lapdb.execute('INSERT INTO user VALUES (?, ?)', ('defaultuser', 'defaultpassword'))
                lapconn.commit()
                # TODO Drop password?
                lapdb.execute('SELECT user,pass FROM user;')
                res = lapdb.fetchall()
                userArray = res[0]
            except (Exception) as exc:
                print("Error initializing " + self.laptimesDb, exc)
        finally:
            lapconn.close()
        
        return userArray

    def identifyTrack(self, z, tracklength):
        self.db.execute('SELECT id, name, startz FROM Tracks WHERE abs(length - ?) < 0.001', (tracklength,))
        track = self.db.fetchall()

        if (len(track) == 1):
            index, name, startz = track[0]
            self.track = index
            print("Track: %s" % str(name))
        elif (len(track) > 1):
            for index, name, startz in track:
                if abs(z - startz) < 50:
                    self.track = index
                    print("Track: %s (Z: %s)" % (str(name), str(z)))
        
        else:
            self.track = -1
            print("Failed to identify track: %s (Z: %s)" % (str(tracklength), str(z)))
        return self.track
    

    def saveCar(self, rpm, max_rpm, index, name):
        self.car = index
        print("Car: %s (%s - %s)" % (name, str(rpm), str(max_rpm)))

    def identifyCar(self, rpm, max_rpm):
        # Some more delta allowed for startrpm as 2nd Pikes Peak run seems to simulate worn/warmed up engine
        self.db.execute('SELECT id, name FROM cars WHERE abs(maxrpm - ?) < 0.01 AND abs(startrpm - ?) < 2.0', (max_rpm, rpm))
        car = self.db.fetchall()
        # TODO Equivalent cars: Ford RS200/Lancia Evo, Renault Alpine/Mini Countryman, Ford RS500/Impreza 1995 and many modern 4WD cars...
        # TODO #1 maxWheelDelta not helpful to distinguish 4WD cars. 
        # Take -1. For c in car log warnings like "ambigious car data" plus suggest "update laptimes set car=X where timestamp=Y"  
        if (len(car) == 1):
            index, name = car[0]
            self.saveCar(rpm, max_rpm, index, name)
        elif (len(car) == 2):
            # Peugeot 205 T16 Rally and Hillclimb cars have identical RPMs
            self.car = 0
            for index, name in car:
                if (self.track >= 1000 and index >= 1000):
                    self.saveCar(rpm, max_rpm, index, name)
                if (self.track < 1000 and index < 1000):
                    self.saveCar(rpm, max_rpm, index, name)
        
        else:
            self.car = -1
            print("Failed to identify car: %s - %s" % (str(rpm), str(max_rpm)))
        return self.car

    def recordResults(self, laptime):
        try:
            lapconn = sqlite3.connect(self.approot + self.laptimesDb)
            lapdb = lapconn.cursor()
            lapdb.execute('INSERT INTO laptimes (Track, Car, Timestamp, Time) VALUES (?, ?, ?, ?)', (self.track, self.car, time.time(), laptime))
            lapconn.commit()
            lapconn.close()
            # TODO Record topspeed?
        except (Exception) as exc:
            print("Error connecting to database:", exc)

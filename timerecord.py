import asyncore
import os.path
import socket
import sqlite3
import struct
import sys

import yaml


class Receiver(asyncore.dispatcher):

    def __init__(self, address, speed_units, db, approot, userArray):
        asyncore.dispatcher.__init__(self)
        self.speed_units = speed_units
        self.speed_modifier = speed_units == 'mph' and 0.6214 or 1
        self.address = address
        self.reconnect()
        self.db = db
        self.approot = approot
        self.finished = False
        self.started = False
        self.track = 0
        self.car = 0
        self.userArray = userArray
        self.topspeed = 0
        self.currentgear = 0

    def reconnect(self):
        self.received_data = False

        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind(self.address)
        print("Waiting for data on %s:%s" % self.address)

    def writable(self):
        return False

    def handle_expt(self):
        print('exception occurred!')
        self.close()

    def readable(self):
        return True

    def handle_read(self):
        data = self.recv(512)
        
        if not data:
            return
        
        if not self.received_data:
            self.received_data = True
            print("Receiving data on %s:%s" % self.address)

        self.parse(data)
        
    def printResults(self, laptime):
        data = "dirtrally.%s.%s.%s.time:%f|ms" % (self.userArray[0], self.track, self.car, laptime * 1000)
        print(data)
        data = "dirtrally.%s.%s.%s.topspeed:%s|%s" % (self.userArray[0], self.track, self.car, self.topspeed, self.speed_units)
        print(data)

    def parse(self, data):
        stats = struct.unpack('64f', data[0:256])

        time = stats[0]
        gear = stats[33]
        rpm = stats[37]  # *10 to get real value
        max_rpm = stats[63]  # *10 to get real value
        z = stats[6]
        tracklength = stats[61]
        speed = int(stats[7] * 3.6)
        if self.topspeed < speed:
            self.topspeed = speed

        lap = stats[59]
        totallap = stats[60]
        laptime = stats[62]
        
        if not self.finished and totallap == lap:
            print("Laptime: " + str(laptime))
            try:
                lapconn = sqlite3.connect(self.approot + '\dirtrally-laptimes.db')
                lapdb = lapconn.cursor()
                lapdb.execute('INSERT INTO laptimes (Track, Car, Time)VALUES (?, ?, ?)', (self.track, self.car, laptime))
                
                lapconn.commit()
                lapconn.close()
                self.finished = True

                self.printResults(laptime)
                # TODO Record topspeed?
                # TODO Record timestamp
            except (Exception) as exc:
                print("Error connecting to database:", exc)

        if time < 0.5:
            # We assume this is the start of race
            self.finished = False
            self.started = False
            self.topspeed = 0
            
            self.db.execute('SELECT id,name, startz FROM Tracks WHERE abs(length - ?) <0.000000001', (tracklength,))
            track = self.db.fetchall()
            if (len(track) == 1):
                (index, name, startz) = track[0]
                self.track = index
                print("Track: " + name)
            elif (len(track) > 1):
                for (index, name, startz) in track:
                    if abs(z - startz) < 50:
                        self.track = index
                        print("Track: " + str(name) + " Z: " + str(z))
            else:
                self.track = -1
                print("Failed to get track: " + str(tracklength) + " / " + str(z))
            self.db.execute('SELECT id, name FROM cars WHERE abs(maxrpm - ?) < 0.01 AND abs(startrpm - ?)<0.01', (max_rpm, rpm))
            car = self.db.fetchall()
            if (len(car) == 1):
                (index, name) = car[0]
                self.car = car[0][0]
                print("Car: " + name)
            elif (len(car) == 2):
                self.car = 0
                for (index, name) in car:
                    if (self.track >= 1000 and index >= 1000):
                        self.car = index
                    if (self.track < 1000 and index < 1000):
                        self.car = index
            else:
                # If we're on Pikes Peak, we try to keep the previous car index (bug with 2nd run)
                if (self.track <= 1000):
                    self.car = -1
                print("Failed to get car name: " + str(max_rpm) + " / " + str(rpm))
                for row in car:
                    print(row)
        else:
            if not self.started:
                data = "dirtrally.%s.%s.%s.started:1|c" % (self.userArray[0], self.track, self.car)
                print(data)
                self.started = True
            if gear > self.currentgear:
                pass
                # TODO Count gear changes. Count H-Shifting differently?
        self.currentgear = gear
                    
if __name__ == '__main__':
    if getattr(sys, 'frozen', None):
        approot = os.path.dirname(sys.executable)
    else:
        approot = os.path.dirname(os.path.realpath(__file__))

    try:
        config = yaml.load(open(approot + '/config.yml', 'r'))
    except (yaml.YAMLError) as exc:
        print("Error in configuration file:", exc)\

    try:
        conn = sqlite3.connect(approot + '/dirtrally-lb.db')
        db = conn.cursor()
    except (Exception) as exc:
        print("Error connecting to database:", exc)

    try:
        lapconn = sqlite3.connect(approot + '\dirtrally-laptimes.db')
        lapdb = lapconn.cursor()
        lapdb.execute('SELECT user,pass FROM user;');
        res = lapdb.fetchall()
        userArray = res[0]

    except (Exception) as exc:
        try:
                print("Trying to init the db", exc)
                lapdb.execute('CREATE TABLE laptimes (Track INTEGER, Car INTEGER, Time REAL);')
                lapdb.execute('CREATE TABLE user (user TEXT, pass TEXT);')
                # url = domain+"newUser.php";
                # with urllib.request.urlopen(url) as response:
                #       resp = response.read()
                # DEBUG (resp[1:13].decode(), resp[13:25].decode()) -> ('defaultuser', 'defaultpassword')
                lapdb.execute('INSERT INTO user VALUES (?, ?)', ('defaultuser', 'defaultpassword'))
                lapconn.commit()
                
                # TODO Drop password?
                lapdb.execute('SELECT user,pass FROM user;');
                res = lapdb.fetchall()
                userArray = res[0]
                lapconn.close()
        except (Exception) as exc:
            print("Error initializing laptimes.db", exc)

    server = (config['telemetry_server']['host'], config['telemetry_server']['port'])
    speed_units = config['speed_units']

    game = Receiver(server, speed_units, db, approot, userArray)

    asyncore.loop()

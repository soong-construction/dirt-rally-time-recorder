import asyncore
import socket
import struct
from databaseAccess import DatabaseAccess
from database import Database
from sampler import Sampler
import time as python_time
from statsProcessor import StatsProcessor

class Receiver(asyncore.dispatcher):

    def __init__(self, address, speed_units, approot):
        asyncore.dispatcher.__init__(self)
        self.speed_units = speed_units
        self.speed_modifier = speed_units == 'mph' and 0.6214 or 1
        self.address = address
        self.approot = approot
        self.finished = False
        self.track = 0
        self.car = 0
        self.topspeed = 0
        self.previousTime = 0
        
        self.database = Database(approot).setup()
        self.databaseAccess = DatabaseAccess(self.database)
        self.userArray = self.database.initializeLaptimesDb()
        self.statsProcessor = StatsProcessor(self)
        
        self.carSampler = Sampler('sampling/dr2')
        self.tracksSampler = Sampler('sampling/dr2_tracks')
        self.last_time = 0
        self.previousDistance = 0
        self.tracklength = -1
        
        self.reconnect()

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
        dbAccess = self.databaseAccess
        data = "dirtrally.%s.%s.%s.time:%f|ms" % (self.userArray[0], dbAccess.identify(self.track), dbAccess.identify(self.car), laptime * 1000)
        print(data)
        data = "dirtrally.%s.%s.%s.topspeed:%s|%s" % (self.userArray[0], dbAccess.identify(self.track), dbAccess.identify(self.car), self.topspeed, self.speed_units)
        print(data)


    def showCarControlInformation(self):
        if isinstance(self.car, (list,)):
            for car in self.car:
                print(self.databaseAccess.describeCarInterfaces(car))
        else:
            print(self.databaseAccess.describeCarInterfaces(self.car))

    def appendInsert(self, file_param, line):
        insertFile = open(file=file_param, mode='a', encoding='utf-8', newline='\n')
        insertFile.write(line)

    def sampleTrack(self, z, tracklength):
        ambiguousSample = self.carSampler.sample(z, tracklength)
        if (ambiguousSample):
            print("ambiguous sample for z:%s tracklength:%s" % (z, tracklength))
        else:
            print("stored sample for z:%s tracklength:%s" % (z, tracklength))
        line = 'INSERT INTO Tracks (id, name, length, startz, finish_distance) VALUES (ID, \'TRACK_NAME\', %s, %s' % (tracklength, z)
        self.appendInsert('tracks_inserts.sql', line)
        

    def sampleCar(self, rpm, max_rpm):
        ambiguousSample = self.carSampler.sample(rpm, max_rpm)
        if (ambiguousSample):
            print("ambiguous sample for rpm:%s max_rpm:%s" % (rpm, max_rpm))
        else:
            print("stored sample for rpm:%s max_rpm:%s" % (rpm, max_rpm))
        line = 'INSERT INTO cars (id, name, maxrpm, startrpm) VALUES (ID, \'CAR_NAME\', %s, %s);\n' % (max_rpm, rpm)
        self.appendInsert('car_inserts.sql', line)

    def parse(self, data):
        stats = struct.unpack('64f', data[0:256])
        
        time = stats[0]
        lap = stats[59]
        distance = stats[2]
        
        speed = int(stats[7] * 3.6)
        if self.topspeed < speed:
            self.topspeed = speed

        # TODO #8 Debugging
        currentlap1 = stats[36]
        time_now = int(python_time.time())
        if (time_now - self.last_time > 2):
            print('currentlap1 %s, currentlap2 %s' % (currentlap1, lap))
            self.last_time = time_now
            
        trackProgress = distance / self.tracklength
        self.statsProcessor.handleGameState(self.inStage(), self.finished, lap, time, self.previousTime, distance, trackProgress, stats)

        self.previousTime = time
        self.previousDistance = distance

    def resetStage(self):
        self.track = 0
        self.car = 0
        
    def inStage(self):
        return self.track != 0 and self.car != 0

    def prepareStage(self):
        self.finished = False
        self.topspeed = 0
        
    def startStage(self, stats):
        rpm = stats[37]  # *10 to get real value
        max_rpm = stats[63]  # *10 to get real value
        z = stats[6]
        tracklength = stats[61]

        dbAccess = self.databaseAccess
        self.track = dbAccess.identifyTrack(z, tracklength)
        self.car = dbAccess.identifyCar(rpm, max_rpm)
        
        self.tracklength = tracklength
        self.sampleTrack(z, tracklength)
        # TODO Don't sample both simultaneously
        # self.sampleCar(rpm, max_rpm)

        data = "dirtrally.%s.%s.%s.started:1|c" % (self.userArray[0], dbAccess.identify(self.track), dbAccess.identify(self.car))
        print(data)
        
        # TODO #8 Include DR2 cars
        # self.showCarControlInformation()

    def finishStage(self, stats):
        laptime = stats[62]
        self.databaseAccess.recordResults(self.track, self.car, laptime)
        self.printResults(laptime)
        self.finished = True
        print('final distance: %s at: %s' % (self.previousDistance, self.previousDistance / self.tracklength))
        self.appendInsert('tracks_inserts.sql', ', %s);\n' % (self.previousDistance))

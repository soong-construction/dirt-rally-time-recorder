import asyncore
import socket
import struct
from databaseAccess import DatabaseAccess
from database import Database
from statsProcessor import StatsProcessor
from ambiguousResultHandler import AmbiguousResultHandler

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
        self.fieldCount = 66
        
        self.database = Database(approot).setup()
        self.ambiguousResultHandler = AmbiguousResultHandler(Database.laptimesDbName)
        self.databaseAccess = DatabaseAccess(self.database, self.ambiguousResultHandler)
        self.userArray = self.database.initializeLaptimesDb()
        self.statsProcessor = StatsProcessor(self)
        
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
        data = self.recv(self.fieldCount * 8)
        
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

    def parse(self, data):
        stats = struct.unpack(str(self.fieldCount) + 'f', data[0:self.fieldCount * 4])
        
        time = stats[0]
        lap = stats[59]
        distance = stats[2]
        
        speed = int(stats[7] * 3.6)
        if self.topspeed < speed:
            self.topspeed = speed

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
        idle_rpm = stats[64]  # *10 to get real value
        max_rpm = stats[63]  # *10 to get real value
        z = stats[6]
        tracklength = stats[61]
        
        dbAccess = self.databaseAccess
        self.track = dbAccess.identifyTrack(z, tracklength)
        self.car = dbAccess.identifyCar(idle_rpm, max_rpm)
        
        self.tracklength = tracklength
        
        data = "dirtrally.%s.%s.%s.started:1|c" % (self.userArray[0], dbAccess.identify(self.track), dbAccess.identify(self.car))
        print(data)
        
        # TODO #8 Include DR2 cars: https://docs.google.com/spreadsheets/d/1B0MNyHmtHrl0PN2R18tQ4mBkaqnouWR_dm6MPHu3qhE/edit#gid=296137675
        self.showCarControlInformation()

    def finishStage(self, stats):
        laptime = stats[62]
        self.databaseAccess.recordResults(self.track, self.car, laptime)
        self.printResults(laptime)
        self.finished = True

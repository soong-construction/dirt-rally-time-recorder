import asyncore
import socket
import struct
from databaseAccess import DatabaseAccess
from database import Database

class Receiver(asyncore.dispatcher):

    goLineDistance = 0.0
    
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
        distance = stats[2]
        
        dbAccess = self.databaseAccess
        
        if not self.finished and (totallap == lap):
            dbAccess.recordResults(self.track, self.car, laptime)
            self.printResults(laptime)
            self.finished = True

        # Looks like time is not reset when restarting events (but for: fresh/proceeding events, second runs on PP).
        elif time < self.previousTime:
            # New event for which track/car must be reset 
            self.track = 0
            self.car = 0
            self.maxWheelDelta = 0
            
        elif distance <= self.goLineDistance:
            # Reset stage data when finishing stage
            self.finished = False
            self.topspeed = 0
            
            if (self.track == 0):
                self.track = dbAccess.identifyTrack(z, tracklength)
                self.car = dbAccess.identifyCar(rpm, max_rpm)
                
                data = "dirtrally.%s.%s.%s.started:1|c" % (self.userArray[0], dbAccess.identify(self.track), dbAccess.identify(self.car))
                print(data)
                
                self.showCarControlInformation()

        self.previousTime = time

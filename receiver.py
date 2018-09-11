import asyncore
import socket
import struct
from database import Database

class Receiver(asyncore.dispatcher):

    goLineDistance = 0.0
    
    def __init__(self, address, speed_units, approot):
        asyncore.dispatcher.__init__(self)
        self.speed_units = speed_units
        self.speed_modifier = speed_units == 'mph' and 0.6214 or 1
        self.address = address
        self.reconnect()
        self.approot = approot
        self.finished = False
        self.track = 0
        self.car = 0
        self.topspeed = 0
        self.currentgear = 0
        self.maxWheelDelta = 0
        self.database = Database(approot)
        self.userArray = self.database.initializeLaptimesDb()
        self.previousTime = 0

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


    def approachingStart(self, distance):
        # Careful: Distance never < 0 in Värmland
        return distance <= self.goLineDistance


    def isRallyStage(self):
        return self.track < 1000

    def parse(self, data):
        stats = struct.unpack('64f', data[0:256])
        
        time = stats[0]
        gear = stats[33]
        rpm = stats[37]  # *10 to get real value
        # TODO Does this change with upgrades!? E.g. Delta HF Integrale
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
        
        if not self.finished and totallap == lap:
            self.database.recordResults(laptime)
            self.printResults(laptime)
            self.finished = True

        # Looks like time is not reset when restarting events (but for: fresh/proceeding events, second runs on PP). TODO But when proceeding to next event??
        elif time < self.previousTime:
            # New event for which track/car must be reset 
            self.track = 0
            self.car = 0
            
        elif distance <= self.goLineDistance:
            # Reset stage data when finishing stage
            self.finished = False
            self.topspeed = 0
            self.maxWheelDelta = 0
            
            if (self.track == 0):
                track, car = (self.database.identifyTrack(z, tracklength), self.database.identifyCar(rpm, max_rpm))
                self.track = track
                self.car = car
                
                data = "dirtrally.%s.%s.%s.started:1|c" % (self.userArray[0], self.track, self.car)
                print(data)

        # TODO Count gear changes. Count H-Shifting differently?
        self.currentgear = gear
        
        self.previousTime = time
        
        if (self.approachingStart(distance) and self.isRallyStage()):
            # Approaching the start line
            wheelStats = list( stats[i] for i in [25, 26, 27, 28] )
            wheelDelta = wheelStats[0] - wheelStats[3] # Delta between rear and front left wheel
            if (wheelDelta > self.maxWheelDelta):
                self.maxWheelDelta = wheelDelta
                print("maxWheelDelta: %s" % self.maxWheelDelta)

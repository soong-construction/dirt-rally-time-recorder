import asyncore
import socket
import struct
from databaseAccess import DatabaseAccess
from database import Database
from statsProcessor import StatsProcessor
from ambiguousResultHandler import AmbiguousResultHandler

class Receiver(asyncore.dispatcher):

    def __init__(self, address, speed_unit, approot):
        asyncore.dispatcher.__init__(self)
        self.speed_unit = speed_unit
        self.speed_modifier = speed_unit == 'mph' and 0.6214 or 1
        self.address = address
        self.approot = approot
        self.finished = False
        self.track = 0
        self.car = 0
        self.topspeed = 0 # unit: m/s
        self.previousTime = 0
        self.fieldCount = 66
        
        self.database = Database(approot).setup()
        self.ambiguousResultHandler = AmbiguousResultHandler(Database.laptimesDbName)
        self.databaseAccess = DatabaseAccess(self.database, self.ambiguousResultHandler)
        self.userArray = self.database.initializeLaptimesDb()
        self.statsProcessor = StatsProcessor(self)
        
        self.previousDistance = 0
        self.tracklength = -1

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
        
    def formatTopSpeed(self):
        topspeed_kmh = self.topspeed * 3.6
        return '%.1f' % (topspeed_kmh * self.speed_modifier,)
    
    def formatLapTime(self, laptime):
        return '%.2f' % (laptime,)

    def printResults(self, laptime):
        dbAccess = self.databaseAccess
        # FIXME Uncaught error, handle better/log. Also, test this method
        #data = "dirtrally.%s.%s.%s.time:%f|s" % (self.userArray[0], dbAccess.identify(self.track), dbAccess.identify(self.car), self.formatLapTime(laptime))
        ##error: uncaptured python exception, closing channel <receiver.Receiver 127.0.0.1:20778 at 0x16c613a6748> (<class 'TypeError'>:must be real number, not str [D:\Python\lib\asyncore.py|read|83] [D:\Python\lib\asyncore.py|handle_read_event|420] [G:\git-repos\dirt-rally-time-recorder\receiver.py|handle_read|60] [G:\git-repos\dirt-rally-time-recorder\receiver.py|parse|95] [G:\git-repos\dirt-rally-time-recorder\statsProcessor.py|handleGameState|19] [G:\git-repos\dirt-rally-time-recorder\receiver.py|finishStage|131] [G:\git-repos\dirt-rally-time-recorder\receiver.py|printResults|71])
        data = "dirtrally.%s.%s.%s.time:%s|s" % (self.userArray[0], dbAccess.identify(self.track), dbAccess.identify(self.car), self.formatLapTime(laptime))
        print(data)
        data = "dirtrally.%s.%s.%s.topspeed:%s|%s" % (self.userArray[0], dbAccess.identify(self.track), dbAccess.identify(self.car), self.formatTopSpeed(), self.speed_unit)
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
        
        speed = int(stats[7])
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
        
        self.showCarControlInformation()

    def finishStage(self, stats):
        laptime = stats[62]
        self.databaseAccess.recordResults(self.track, self.car, laptime)
        self.printResults(laptime)
        self.finished = True

import socket
import struct
import asyncore
#import serial
import yaml
import os.path
import sys
import sqlite3
import urllib.request

class Sender:
    def __init__(self, serial_name):
        try:
            self.ser = serial.Serial(
                serial_name, 
                115200, 
                writeTimeout=0, 
                timeout=0, 
                parity=serial.PARITY_NONE, 
                stopbits=serial.STOPBITS_ONE
            )
        except (serial.serialutil.SerialException) as exc:
            pass #sys.exit("Could not connect to serial port: %s" % serial_name)

        print("Connected to serial port: %s" % serial_name)

    def send(self, data):
        self.ser.write(struct.pack('>cHHchcB', 'R', data['rpm'], data['max_rpm'], 'S', data['speed'], 'G', data['gear']))

class Receiver(asyncore.dispatcher):
    def __init__(self, address, sender, speed_units, db, approot, userArray):
        asyncore.dispatcher.__init__(self)
        self.sender = sender
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
        
    def parse(self, data):
        # Unpack the data.
        stats = struct.unpack('64f', data[0:256])

        time = stats[0]
        gear = stats[33]
        rpm = stats[37] # *10 to get real value
        max_rpm = stats[63] # *10 to get real value
        z = stats[6]
        tracklength = stats[61]
        speed= int(stats[7] * 3.6)
        if self.topspeed < speed:
            self.topspeed = speed

        #sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        lap = stats[59]
        totallap = stats[60]
        laptime = stats[62]
        
        if not self.finished and totallap==lap:
            print("Laptime: " + str(laptime))
            try:
                lapconn = sqlite3.connect(self.approot+'\dirtrally-laptimes.db')
                lapdb = lapconn.cursor()
                lapdb.execute('INSERT INTO laptimes (Track, Car, Time)VALUES (?, ?, ?)', (self.track, self.car, laptime))
                
                lapconn.commit()
                lapconn.close()
                self.finished = True
                #sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data="dirtrally.%s.%s.%s.time:%f|ms" % (self.userArray[0],self.track,self.car,laptime*1000)
                print(data)
                #sock.sendto(data.encode(), (statsd,8125))
                data="dirtrally.%s.%s.%s.finished:1|c" % (self.userArray[0],self.track,self.car)
                print(data)
                #sock.sendto(data.encode(), (statsd,8125))
                data="dirtrally.%s.%s.%s.topspeed:%s|%s" % (self.userArray[0],self.track,self.car,self.topspeed,self.speed_units)
				# TODO Record topspeed?
				# TODO Record timestamp
                print(data)
                #sock.sendto(data.encode(), (statsd,8125))
                #url = domain + "saveTime.php?u=%s&t=%s&c=%s&ms=%f&h=%s" % (self.userArray[0], self.track, self.car, laptime, self.userArray[1])
                #print(url)
                #with urllib.request.urlopen(url) as response:
                #   html = response.read()
                #print("Check your times at: %s/showTimes.php?u=%s" %(domain,self.userArray[0]))
            except (Exception) as exc:
                print("Error connecting to database:", exc)
            

        if time < 0.5:
            # We assume this is the start of race
            self.finished = False
            self.started = False
            self.topspeed = 0
            
			# FIXME Seems that self.db is actually dirtrally-laptimes.db not dirtrally-lb.db (which stores tracks/cars)
            self.db.execute('SELECT id,name, startz FROM Tracks WHERE abs(length - ?) <0.000000001', (tracklength,))
            track = self.db.fetchall()
            if (len(track)==1):
                (index, name, startz) = track[0]
                self.track = index
                print("Track: " + name)
            elif (len(track)>1):
                for (index, name, startz) in track:
                    if abs(z - startz)<50:
                        self.track = index
                        print("Track: " + str(name) + " Z: " + str(z))
            else:
                self.track=-1
                print("Failed to get track: " + str(tracklength) + " / " + str(z))
            self.db.execute('SELECT id, name FROM cars WHERE abs(maxrpm - ?) < 0.01 AND abs(startrpm - ?)<0.01', (max_rpm, rpm))
            car = self.db.fetchall()
            if (len(car)==1):
                (index, name) = car[0]
                self.car = car[0][0]
                print("Car: " + name)
            elif (len(car)==2):
                self.car=0
                for (index, name) in car:
                    if (self.track >= 1000 and index>=1000):
                        self.car = index
                    if (self.track < 1000 and index < 1000):
                        self.car = index
            else:
                # If we're on Pikes Peak, we try to keep the previous car index (bug with 2nd run)
                if (self.track <= 1000):
                    self.car=-1
                print("Failed to get car name: " + str(max_rpm) + " / " + str(rpm))
                for row in car:
                    print(row)
        else:
            if not self.started:
                #sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data="dirtrally.%s.%s.%s.started:1|c" % (self.userArray[1],self.track,self.car)
                #sock.sendto(data.encode(), (statsd,8125))
                self.started = True
            if gear > self.currentgear:
                data="dirtrally.%s.%s.%s.gear.up.%s:1|ms" % (self.userArray[0],self.track,self.car,int(gear))
                #sock.sendto(data.encode(), (statsd,8125))
            elif gear < self.currentgear:
                data="dirtrally.%s.%s.%s.gear.down.%s:1|ms" % (self.userArray[0],self.track,self.car,int(gear))
                #sock.sendto(data.encode(), (statsd,8125))
        self.currentgear = gear
                    
        data = {
            'speed': int(stats[7] * 3.6 * self.speed_modifier),
            'gear': int(stats[33]),
            'rpm': int(stats[37] * 10),
            'max_rpm': int(stats[63] * 10)
        }
#        print(data)

        #for i in range(len(stats)):
        #    print(str(i) + " : " + str(stats[i]))
        #self.sender.send(data)

#domain="http://dirtrally.marcoz.org/"
#url = domain + "/getStatsdHost.html"
#with urllib.request.urlopen(url) as response:
#        statsd = response.read().decode()[:-1]

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
        conn = sqlite3.connect(approot+'/dirtrally-lb.db')
        db = conn.cursor()
    except (Exception) as exc:
        print("Error connecting to database:", exc)

    try:
        lapconn = sqlite3.connect(approot+'\dirtrally-laptimes.db')
        lapdb = lapconn.cursor()
        lapdb.execute('SELECT user,pass FROM user;');
        res = lapdb.fetchall()
        userArray = res[0]

    except (Exception) as exc:
        try:
                print("Trying to init the db", exc)
                lapdb.execute('CREATE TABLE laptimes (Track INTEGER, Car INTEGER, Time REAL);')
                lapdb.execute('CREATE TABLE user (user TEXT, pass TEXT);')
                #url = domain+"newUser.php";
                #with urllib.request.urlopen(url) as response:
                #       resp = response.read()
                # DEBUG (resp[1:13].decode(), resp[13:25].decode()) -> ('defaultuser', 'defaultpassword')
                lapdb.execute('INSERT INTO user VALUES (?, ?)', ('defaultuser', 'defaultpassword'))
                lapconn.commit()
                
                lapdb.execute('SELECT user,pass FROM user;');
                res = lapdb.fetchall()
                userArray = res[0]
                lapconn.close()
        except (Exception) as exc:
            print("Error initializing laptimes.db", exc)
    #print("Check your times at: %s/showTimes.php?u=%s" %(domain,userArray[0]))

    #arduino = Sender(config['arduino_port'])
    arduino = ""
    server = (config['telemetry_server']['host'], config['telemetry_server']['port'])
    speed_units = config['speed_units']

    game = Receiver(server, arduino, speed_units, db, approot, userArray)

    asyncore.loop()

import asyncore
import socket
import struct

from statsProcessor import StatsProcessor

class Receiver(asyncore.dispatcher):

    def __init__(self, address, speed_unit, approot):
        asyncore.dispatcher.__init__(self)
        self.address = address
        self.fieldCount = 66
        self.statsProcessor = StatsProcessor(speed_unit, approot)

    def reconnect(self):
        self.received_data = False

        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind(self.address)
        self.print("Waiting for data on %s:%s" % self.address)

    def writable(self):
        return False

    def handle_expt(self):
        self.print('exception occurred!')
        self.handle_close()

    def handle_error(self):
        # TODO #17 Log errors to file and ask to contact developer
        asyncore.dispatcher.handle_error(self)

    def informCloseAndWaitForInput(self):
        self.print('The connection was closed.')
        input('Press ENTER to end program.')

    def handle_close(self):
        self.close()
        self.informCloseAndWaitForInput()

    def readable(self):
        return True

    def handle_read(self):
        data = self.recv(self.fieldCount * 8)

        if not data:
            return

        if not self.received_data:
            self.received_data = True
            self.print("Receiving data on %s:%s" % self.address)

        self.parse(data)

    def parse(self, data):
        stats = struct.unpack(str(self.fieldCount) + 'f', data[0:self.fieldCount * 4])

        self.statsProcessor.handleStats(stats)

    def print(self, message):
        print(message)
        

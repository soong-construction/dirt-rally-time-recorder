'''
The basic UDP logic, should rarely change and is difficult to test
'''
import asyncore
import socket
import struct

from .statsProcessor import StatsProcessor
from .log import getLogger
from . import config

logger = getLogger(__name__)

class Receiver(asyncore.dispatcher):

    def __init__(self, approot):
        asyncore.dispatcher.__init__(self)
        self.address = config.GET.server
        self.field_count = 66
        self.stats_processor = StatsProcessor(approot)
        self.received_data = False

    def reconnect(self):
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind(self.address)
        logger.info("Waiting for data on %s:%s", *self.address)

    def writable(self):
        return False

    def handle_expt(self):
        self.handle_close()
        raise IOError('An exception occured while reading from socket')

    def handle_error(self):
        self.handle_close()
        raise  #pylint: disable=misplaced-bare-raise

    def handle_close(self):
        self.close()

    def readable(self):
        return True

    def handle_read(self):
        data = self.recv(self.field_count * 8)

        if not data:
            return

        if not self.received_data:
            self.received_data = True
            logger.debug("Receiving data on %s:%s", *self.address)

        self.parse(data)

    def parse(self, data):
        stats = struct.unpack(str(self.field_count) + 'f', data[0:self.field_count * 4])

        self.stats_processor.handleStats(stats)

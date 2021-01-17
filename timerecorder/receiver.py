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
        self.fieldCount = 66
        self.statsProcessor = StatsProcessor(approot)

    def reconnect(self):
        self.received_data = False

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
        data = self.recv(self.fieldCount * 8)

        if not data:
            return

        if not self.received_data:
            self.received_data = True
            logger.debug("Receiving data on %s:%s", *self.address)

        self.parse(data)

    def parse(self, data):
        stats = struct.unpack(str(self.fieldCount) + 'f', data[0:self.fieldCount * 4])

        self.statsProcessor.handleStats(stats)

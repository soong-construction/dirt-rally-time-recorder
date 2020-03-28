import unittest

from unittest.mock import MagicMock
from receiver import Receiver
from database import Database
import struct
import asyncore

sixtySixFields = b'\xe9}\xb9A\x00\x00\x00\x00\x00\xf1 \xc0\x00\x00\x00\x00L\xdb(E\xcc\xde\x07D\xd1F\x87\xc5\xeep\x03<\x11\xe8\xf9\xbas\x94\xd7\xba\x0c\x99\xf9;\xeb\xe0F\xbe\xc8\nF<:\x1b{\xbfz\xd4z\xbfdfP\xbd\x88\x04F>\x99\xdd\x19@lh!?\xe9\x17f@U\x98V@\xda\xf7\x0f\xc2=\x89\x07\xc2\x86\xe6\x15\xc2D{\x0c\xc2\x00\x00\x00\x00\x00\x00\x00\x003\xb4\xb5;\x0c\x8a\xdd;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x871<,\xd3`:\x00\x00\x00\x00+b\xe6B\x00\x00\x80?\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\xe1\x02\xa4E\x00\x00\x00\x00`\x00iD+b\xe6B\x00\x00\xc0@'


class TestReceiver(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        self.DatabaseSetupFunction = Database.setup

    def setUp(self):
        Database.setup = MagicMock()
        self.thing = Receiver(('localhost', 1024), 'kmh', 'testroot')

    def tearDown(self):
        # TODO This restoration should be used throughout the test base
        Database.setup = self.DatabaseSetupFunction
        try:
            self.thing.close()
        except:
            raise

    def testTopSpeedConversion(self):
        self.thing = Receiver(('localhost', 1024), 'kmh', 'testroot')
        self.thing.topspeed = 33.28

        format_top_speed = self.thing.formatTopSpeed()
        self.assertEqual(format_top_speed, '119.8')

        self.thing = Receiver(('localhost', 1024), 'mph', 'testroot')
        self.thing.topspeed = 33.28

        format_top_speed = self.thing.formatTopSpeed()
        self.assertEqual(format_top_speed, '74.4')

    def testLapTimeConversion(self):
        format_lap_time = self.thing.formatLapTime(180.249)
        self.assertEqual(format_lap_time, '180.25')

    def testHandleReadCallsParse(self):
        self.thing.reconnect()

        self.thing.parse = MagicMock()

        self.thing.recv = MagicMock(return_value=sixtySixFields)

        self.thing.handle_read()

        self.assertTrue(self.thing.parse.called, 'Never called parse')

    def testHandleFinishStageAndPrintResults(self):
        self.thing.reconnect()

        self.thing.inStage = MagicMock(return_value=True)
        self.thing.print = MagicMock()
        self.thing.databaseAccess.recordResults = MagicMock()
        self.thing.databaseAccess.identifyCar = MagicMock(return_value=10)
        self.thing.databaseAccess.identifyTrack = MagicMock(return_value=11)

        stats = struct.unpack(str(self.thing.fieldCount) + 'f', sixtySixFields[0:self.thing.fieldCount * 4])
        # stats[59] == 1 means lap/stage complete
        stats = stats[:59] + (1.0,) + stats[60:]
        stats = struct.pack(str(self.thing.fieldCount) + 'f', *stats)

        self.thing.recv = MagicMock(return_value=stats)

        self.thing.handle_read()

        self.thing.print.assert_called()
        self.thing.databaseAccess.recordResults.assert_called()
        self.assertTrue(self.thing.finished, 'Did not toggle finished')

    def testHandleStartStageAndDatabaseCalled(self):
        self.thing.reconnect()

        self.thing.inStage = MagicMock(return_value=False)
        self.thing.print = MagicMock()
        self.thing.databaseAccess.recordResults = MagicMock()
        self.thing.databaseAccess.identifyCar = MagicMock(return_value=10)
        self.thing.databaseAccess.identifyTrack = MagicMock(return_value=11)

        stats = struct.unpack(str(self.thing.fieldCount) + 'f', sixtySixFields[0:self.thing.fieldCount * 4])
        # stats[59] == 1 means lap/stage complete
        stats = stats[:59] + (0.0,) + stats[60:]
        stats = struct.pack(str(self.thing.fieldCount) + 'f', *stats)

        self.thing.recv = MagicMock(return_value=stats)

        self.thing.handle_read()

        self.thing.print.assert_called()
        self.thing.databaseAccess.identifyCar.assert_called()
        self.thing.databaseAccess.identifyTrack.assert_called()

    def testCloseGracefullyOnError(self):
        self.thing.reconnect()

        self.thing.recv = MagicMock(return_value=sixtySixFields)
        self.thing.parse = MagicMock(side_effect=TypeError)
        self.thing.informCloseAndWaitForInput = MagicMock()

        asyncore.read(self.thing)

        self.thing.informCloseAndWaitForInput.assert_called()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestReceiver.testTopSpeedConversion']
    unittest.main()

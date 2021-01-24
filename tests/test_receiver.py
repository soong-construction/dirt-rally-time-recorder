import asyncore
import unittest
from unittest.mock import MagicMock
from timerecorder.statsProcessor import StatsProcessor
from timerecorder.receiver import Receiver
from tests.test_base import TestBase

SIXTY_SIX_FIELDS = b'\xe9}\xb9A\x00\x00\x00\x00\x00\xf1 \xc0\x00\x00\x00\x00L\xdb(E\xcc\xde\x07D\xd1F\x87\xc5\xeep\x03<\x11\xe8\xf9\xbas\x94\xd7\xba\x0c\x99\xf9;\xeb\xe0F\xbe\xc8\nF<:\x1b{\xbfz\xd4z\xbfdfP\xbd\x88\x04F>\x99\xdd\x19@lh!?\xe9\x17f@U\x98V@\xda\xf7\x0f\xc2=\x89\x07\xc2\x86\xe6\x15\xc2D{\x0c\xc2\x00\x00\x00\x00\x00\x00\x00\x003\xb4\xb5;\x0c\x8a\xdd;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x871<,\xd3`:\x00\x00\x00\x00+b\xe6B\x00\x00\x80?\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\xe1\x02\xa4E\x00\x00\x00\x00`\x00iD+b\xe6B\x00\x00\xc0@'

class TestReceiver(TestBase):

    def __init__(self, methodName):
        TestBase.__init__(self, methodName, 'test-files')
        self.update_resources_function = StatsProcessor._updateResources

    def setUp(self):
        StatsProcessor._updateResources = MagicMock()
        self.thing = Receiver('test-files')

    def tearDown(self):
        StatsProcessor._updateResources = self.update_resources_function
        try:
            self.thing.close()
        except:
            raise

    def testHandleReadCallsParse(self):
        self.thing.reconnect()

        self.thing.parse = MagicMock()

        self.thing.recv = MagicMock(return_value=SIXTY_SIX_FIELDS)

        self.thing.handle_read()

        self.assertTrue(self.thing.parse.called, 'Never called parse')

    def testReRaiseErrorOnRead(self):
        self.thing.reconnect()
        self.thing.handle_close = MagicMock()

        self.thing.parse = MagicMock(side_effect=IOError)

        with self.assertRaises(OSError):
            asyncore.read(self.thing)

        self.thing.handle_close.assert_called_once()

    def testReRaiseException(self):
        self.thing.reconnect()
        self.thing.handle_close = MagicMock()

        with self.assertRaises(OSError):
            self.thing.handle_expt()

        self.thing.handle_close.assert_called_once()

if __name__ == "__main__":
    unittest.main()

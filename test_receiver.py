import unittest

from unittest.mock import MagicMock
from receiver import Receiver
from database import Database

class TestReceiver(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        self.DatabaseSetupFunction = Database.setup
    
    def setUp(self):
        Database.setup = MagicMock()
        self.thing = Receiver(('localhost', 1024), 'kmh', 'testroot')
        self.thing.parse = MagicMock();

    def tearDown(self):
        # TODO This restoration should be used throughout the test base
        Database.setup = self.DatabaseSetupFunction

    # TODO Build integration test from here
    def testHandleRead(self):
        sixtySixFields = b'\xe9}\xb9A\x00\x00\x00\x00\x00\xf1 \xc0\x00\x00\x00\x00L\xdb(E\xcc\xde\x07D\xd1F\x87\xc5\xeep\x03<\x11\xe8\xf9\xbas\x94\xd7\xba\x0c\x99\xf9;\xeb\xe0F\xbe\xc8\nF<:\x1b{\xbfz\xd4z\xbfdfP\xbd\x88\x04F>\x99\xdd\x19@lh!?\xe9\x17f@U\x98V@\xda\xf7\x0f\xc2=\x89\x07\xc2\x86\xe6\x15\xc2D{\x0c\xc2\x00\x00\x00\x00\x00\x00\x00\x003\xb4\xb5;\x0c\x8a\xdd;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x871<,\xd3`:\x00\x00\x00\x00+b\xe6B\x00\x00\x80?\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\xc4\xf8\xed\xc2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\xe1\x02\xa4E\x00\x00\x00\x00`\x00iD+b\xe6B\x00\x00\xc0@'
        self.thing.recv = MagicMock(return_value=sixtySixFields)
        self.thing.handle_read()
        
        self.assertTrue(self.thing.parse.called, 'Never called parse')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestReceiver.testHandleRead']
    unittest.main()
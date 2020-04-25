import unittest
from unittest.mock import MagicMock
from tests.test_base import TestBase
from timerecorder import timerecord
from timerecorder.receiver import Receiver

class TestTimeRecord(TestBase):

    def __init__(self, methodName):
        TestBase.__init__(self, methodName, 'test-files')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCloseGracefullyOnError(self):
        Receiver.reconnect = MagicMock(side_effect=IOError)
        
        timerecord.informUser = MagicMock()
        
        timerecord.main('logfile')
        
        self.assertTrue(timerecord.informUser.called)  # @UndefinedVariable, PyDev restriction

if __name__ == "__main__":
    unittest.main()

import os
import unittest

from timerecorder import config, log

class TestBase(unittest.TestCase):

    def mockAwaySideEffects(self):
        pass

    def __init__(self, methodName, testroot):
        unittest.TestCase.__init__(self, methodName)
        if not os.path.exists(testroot):
            os.mkdir(testroot)

        testLog = testroot + '/tests.log'
        log.init(testLog)

        config.init(testroot + '/config.yml')

        self.mockAwaySideEffects()

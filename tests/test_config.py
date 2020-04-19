import unittest

from tests.test_base import TestBase
from timerecorder.config import Config
import os

testroot = 'test-files'

class TestConfig(TestBase):

    def __init__(self, methodName):
        TestBase.__init__(self, methodName, testroot)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFreshConfigIsCreated(self):
        configFile = 'newconfig.yml'
        configPath = testroot + '/' + configFile

        if os.path.exists(configPath):
            os.remove(configPath)

        config = Config(configPath)
        config.load()

        self.assertEqual(3, len(config.keys()))
        self.assertEqual(3, len(config.values()))
        self.assertEqual(config['speed_unit'], 'kph')

    def testExistingValuesAreKept(self):
        configFile = 'existingconfig.yml'
        configPath = testroot + '/' + configFile

        if os.path.exists(configPath):
            os.remove(configPath)

        with open(file=configPath, mode='w', encoding='utf-8', newline='\n') as f:
            f.write(('heuristics_mode: 0\n'
                     'speed_unit: kph\n'
                     'telemetry_server:\n'
                     '  port: 12345'))

        config = Config(configPath)
        config.load()

        self.assertEqual(3, len(config.keys()))
        self.assertEqual(3, len(config.values()))
        self.assertEqual(config['speed_unit'], 'kph')
        self.assertEqual(config['telemetry_server']['port'], 12345)

    def testExistingConfigIsMigrated(self):
        configFile = 'existingconfig.yml'
        configPath = testroot + '/' + configFile

        if os.path.exists(configPath):
            os.remove(configPath)

        with open(file=configPath, mode='w', encoding='utf-8', newline='\n') as f:
            f.write('ignored_user_entry: 123')

        config = Config(configPath)
        config.load()

        self.assertEqual(4, len(config.keys()))
        self.assertEqual(4, len(config.values()))
        self.assertEqual(config['speed_unit'], 'kph')

    def testCorruptConfigIsReported(self):
        configFile = 'existingconfig.yml'
        configPath = testroot + '/' + configFile

        if os.path.exists(configPath):
            os.remove(configPath)

        with open(file=configPath, mode='w', encoding='utf-8', newline='\n') as f:
            f.write('br0ken')

        with self.assertRaisesRegex(IOError, '\S+ seems to be corrupt, please check or delete file\.'):
            config = Config(configPath)
            config.load()

    def testCorruptValueIsReported(self):
        configFile = 'existingconfig.yml'
        configPath = testroot + '/' + configFile

        if os.path.exists(configPath):
            os.remove(configPath)

        with open(file=configPath, mode='w', encoding='utf-8', newline='\n') as f:
            f.write('heuristics_mode: \'ON\'')

        with self.assertRaisesRegex(IOError, '\S+ seems to be corrupt, please check or delete file\.'):
            config = Config(configPath)
            config.load()

if __name__ == "__main__":
    unittest.main()

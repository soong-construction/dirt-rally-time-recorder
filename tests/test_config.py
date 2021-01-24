import unittest
import os

from tests.test_base import TestBase
from timerecorder.config import Config, readVersion

TESTROOT = 'test-files'
DEFAULT_CONFIG_COUNT = 5

class TestConfig(TestBase):

    def __init__(self, methodName):
        TestBase.__init__(self, methodName, TESTROOT)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFreshConfigIsCreated(self):
        configPath = TESTROOT + '/newconfig.yml'

        if os.path.exists(configPath):
            os.remove(configPath)

        config = Config(configPath)
        config.load()

        self.assertEqual(DEFAULT_CONFIG_COUNT, len(config.keys()))
        self.assertEqual(DEFAULT_CONFIG_COUNT, len(config.values()))
        self.assertEqual(config['speed_unit'], 'kph')

    def testExistingValuesAreKeptOrExtended(self):
        configPath = TESTROOT + '/existingconfig.yml'
        self.writeFile(configPath,
                    ('speed_unit: kph\n'
                     'telemetry_server:\n'
                     '  port: 12345'))

        config = Config(configPath)
        config.load()

        self.assertEqual(DEFAULT_CONFIG_COUNT, len(config.keys()))
        self.assertEqual(DEFAULT_CONFIG_COUNT, len(config.values()))
        self.assertEqual(config['speed_unit'], 'kph')
        self.assertEqual(config['telemetry_server']['port'], 12345)
        self.assertEqual(config['telemetry_server']['host'], '127.0.0.1')
        self.assertEqual(config['heuristics']['activate'], 0)

    def testExistingConfigIsMigrated(self):
        configPath = TESTROOT + '/existingconfig.yml'
        self.writeFile(configPath, 'ignored_user_entry: 123')

        config = Config(configPath)
        config.load()

        self.assertEqual(DEFAULT_CONFIG_COUNT + 1, len(config.keys()))
        self.assertEqual(DEFAULT_CONFIG_COUNT + 1, len(config.values()))
        self.assertEqual(config['speed_unit'], 'kph')

    def testCorruptConfigIsReported(self):
        configPath = TESTROOT + '/existingconfig.yml'
        self.writeFile(configPath, 'br0ken')

        with self.assertRaisesRegex(IOError, r'\S+ seems to be corrupt, please check or delete file\.'):
            config = Config(configPath)
            config.load()

    def testCorruptValueIsReported(self):
        configPath = TESTROOT + '/existingconfig.yml'
        self.writeFile(configPath,
                       ('heuristics:\n'
                        '  activate: bla\n'))

        with self.assertRaisesRegex(IOError, r'\S+ seems to be corrupt, please check or delete file\.'):
            config = Config(configPath)
            config.load()

    def testMapsStringsToBool(self):
        configPath = TESTROOT + '/existingconfig.yml'
        self.writeFile(configPath,
                       ('heuristics:\n'
                        '  activate: ON\n'
                        '  authentic_shifting: False\n'))

        config = Config(configPath)
        config.load()

        self.assertTrue(config.heuristics_activated)
        self.assertFalse(config.authentic_shifting)

    def testReadsVersionFile(self):
        self.writeFile(TESTROOT + '/VERSION', '1.2.34')

        version = readVersion(TESTROOT)
        self.assertEqual(version, '1.2.34')

    def writeFile(self, configPath, content):
        if os.path.exists(configPath):
            os.remove(configPath)
        with open(file=configPath, mode='w', encoding='utf-8', newline='\n') as file:
            file.write(content)

    def testValuesCanBeReadAsBool(self):
        configPath = TESTROOT + '/valuetest.yml'

        if os.path.exists(configPath):
            os.remove(configPath)

        config = Config(configPath)
        config.load()
        config.clear()

        config['val0'] = 0
        config['valFalse'] = False
        config['val1'] = 1
        config['valTrue'] = True

        self.assertFalse(config['val0'])
        self.assertFalse(config['valFalse'])
        self.assertTrue(config['val1'])
        self.assertTrue(config['valTrue'])

if __name__ == "__main__":
    unittest.main()

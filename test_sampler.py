import unittest
from sampler import Sampler
import os

class TestSampler(unittest.TestCase):
    
    testFolder = 'test-files'
    dict = '/rpm-samples_test'

    def setUp(self):
        os.makedirs(self.testFolder, exist_ok=True)
        self.sampler = Sampler('test-files' + self.dict)

    def tearDown(self):
        os.remove(self.testFolder + self.dict + '.dat')
        pass

    def testNotExistsForFirstValue(self):
        found = self.sampler.sample(100)
        self.assertFalse(found, 'Must not find anything in empty dir')

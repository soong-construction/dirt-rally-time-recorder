import os
import shelve
import unittest

from sampler import Sampler


class TestSampler(unittest.TestCase):
    
    testFolder = 'test-files'
    dict = '/rpm-samples_test'

    def setUp(self):
        os.makedirs(self.testFolder, exist_ok=True)
        self.sampler = Sampler('test-files' + self.dict)

    def tearDown(self):
        d = shelve.open(self.testFolder + self.dict)
        d.clear()
        d.close()

    def testNotExistsForFirstValue(self):
        found = self.sampler.sample(100)
        self.assertFalse(found, 'Must not find anything in empty dir')

import os
import shelve
import unittest

from sampler import Sampler


class TestSampler(unittest.TestCase):
    
    testFolder = 'test-files'
    dict = '/rpm-samples_test'

    def setUp(self):
        os.makedirs(self.testFolder, exist_ok=True)
        self.sampler = Sampler(self.testFolder + self.dict)


    def overwriteShelveEmpty(self):
        return shelve.open(self.testFolder + self.dict, flag='n', writeback=True).close()

    def tearDown(self):
        self.sampler.test()
        self.sampler.close()
        
        self.overwriteShelveEmpty()

    def testNotExistsForFirstValue(self):
        found = self.sampler.sample(100.5, 600.0)
        self.assertFalse(found, 'Must not find anything in empty dir')

    def testExistsForSameValues(self):
        found = self.sampler.sample(100.5, 600.0)
        self.assertFalse(found, 'Must not find anything in empty dir')
        
        found = self.sampler.sample(100.5, 600.0)
        self.assertTrue(found, 'Must find same value on second sample')
        
    def testNotExistsForSameFirstValue(self):
        found = self.sampler.sample(100.5, 600.0)
        self.assertFalse(found, 'Must not find anything in empty dir')
        
        found = self.sampler.sample(100.5, 400.0)
        self.assertFalse(found, 'Must not find different value')
        
    def testNotExistsForSameSecondValue(self):
        found = self.sampler.sample(100.5, 600.0)
        self.assertFalse(found, 'Must not find anything in empty dir')
        
        found = self.sampler.sample(150.5, 600.0)
        self.assertFalse(found, 'Must not find different value')
        
    def testNotExistsForCompletelyDifferentValues(self):
        found = self.sampler.sample(100.5, 600.0)
        self.assertFalse(found, 'Must not find anything in empty dir')
        
        found = self.sampler.sample(200.0, 700.5)
        self.assertFalse(found, 'Must not find different value')
        

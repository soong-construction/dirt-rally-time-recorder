from datetime import datetime, timezone
import time
import unittest
from unittest.mock import MagicMock, ANY

from tests.test_base import TestBase
from timerecorder import config
from timerecorder.ambiguousResultHandler import AmbiguousResultHandler

class TestAmbiguousResultHandler(TestBase):

    def __init__(self, methodName):
        TestBase.__init__(self, methodName, 'test-files')

    def setUp(self):
        self.now = datetime(2019, 10, 20, tzinfo=timezone.utc)
        self.database_access = MagicMock()
        self.gear_tracker = MagicMock()
        self.input_tracker = MagicMock()
        self.thing = AmbiguousResultHandler(self.database_access, 'test-files')

    def tearDown(self):
        pass

    def testHandleResultsWithUnambiguousCars(self):
        car = 100
        track = 1000

        self.thing._applyHeuristics = MagicMock(return_value=None)

        timestamp = time.time()
        result = self.thing.handleAmbiguousCars(timestamp, car, track, self.gear_tracker, self.input_tracker)

        self.thing._applyHeuristics.assert_not_called()
        self.thing.database_access.handleCarUpdates.assert_not_called()
        self.assertEqual(result, car)

    def testHandleResultsWithAmbiguousCarsAndNoHeuristics(self):
        config.GET.heuristics_activated = 1
        car = [100, 200]
        track = 1000

        self.thing._applyHeuristics = MagicMock(return_value=None)
        self.thing.database_access.handleCarUpdates = MagicMock()

        timestamp = time.time()
        result = self.thing.handleAmbiguousCars(timestamp, car, track, self.gear_tracker, self.input_tracker)

        self.thing._applyHeuristics.assert_called_once_with(car, self.gear_tracker, self.input_tracker)
        self.thing.database_access.handleCarUpdates.assert_called_once_with(car, timestamp, 1000, ANY)
        self.assertEqual(result, car)

    def testHandleResultsWithNoCarCandidatesShouldSkipHeuristics(self):
        config.GET.heuristics_activated = 1
        car = []
        track = 1000

        self.thing._applyHeuristics = MagicMock(return_value=200)
        self.thing.database_access.handleCarUpdates = MagicMock()
        self.thing._logFailedRecognition = MagicMock()

        timestamp = time.time()
        result = self.thing.handleAmbiguousCars(timestamp, car, track, self.gear_tracker, self.input_tracker)

        self.thing._applyHeuristics.assert_not_called()
        self.thing.database_access.handleCarUpdates.assert_not_called()
        self.thing._logFailedRecognition.assert_called_once_with(f'UPDATE laptimes SET Car=??? WHERE Timestamp="{timestamp}";', ANY)
        self.assertEqual(result, [])

    def testHandleResultsWithAmbiguousCarsAndLuckyGuess(self):
        config.GET.heuristics_activated = 1
        car = [100, 200]
        track = 1000

        self.thing._applyHeuristics = MagicMock(return_value=200)
        self.thing.database_access.handleCarUpdates = MagicMock()

        timestamp = time.time()
        result = self.thing.handleAmbiguousCars(timestamp, car, track, self.gear_tracker, self.input_tracker)

        self.thing._applyHeuristics.assert_called_once_with(car, self.gear_tracker, self.input_tracker)
        self.thing.database_access.handleCarUpdates.assert_called_once_with([100], timestamp, 1000, ANY)
        self.assertEqual(result, 200)

    def testHeuristicsAreOnlyAppliedIfConfigured(self):
        config.GET.heuristics_activated = 0
        car = [100, 200]
        track = 1000

        self.thing._applyHeuristics = MagicMock(return_value=None)

        timestamp = time.time()
        result = self.thing.handleAmbiguousCars(timestamp, car, track, self.gear_tracker, self.input_tracker)

        self.thing._applyHeuristics.assert_not_called()
        self.thing.database_access.handleCarUpdates.assert_called_once_with([100, 200], timestamp, 1000, ANY)
        self.assertEqual(result, car)

    def testHandleResultsWithUnambiguousTracks(self):
        car = 100
        track = 1000

        timestamp = time.time()
        result = self.thing.handleAmbiguousTracks(timestamp, car, track)

        self.thing.database_access.handleTrackUpdates.assert_not_called()
        self.assertEqual(result, track)

    def testHandleAmbiguousTracks(self):
        car = 100
        track = [1000, 1002]

        timestamp = time.time()
        result = self.thing.handleAmbiguousTracks(timestamp, car, track)

        self.thing.database_access.handleTrackUpdates.assert_called_once_with(track, timestamp, 100, ANY)
        self.assertEqual(result, track)

    def testHandleNoTracks(self):
        car = 100
        track = []

        self.thing._logFailedRecognition = MagicMock()

        timestamp = time.time()
        result = self.thing.handleAmbiguousTracks(timestamp, car, track)

        self.thing.database_access.handleTrackUpdates.assert_not_called()
        self.thing._logFailedRecognition.assert_called_once_with(f'UPDATE laptimes SET Track=??? WHERE Timestamp="{timestamp}";', ANY)
        self.assertEqual(result, [])

    def testSeedIsRandomized(self):
        instance = lambda _: AmbiguousResultHandler(MagicMock(), 'test-files')
        seed = lambda instance: instance.seed

        manyInstances = map(instance, range(0, 100))
        seeds = list(map(seed, manyInstances))
        anySeed = seeds[0]

        self.assertNotEqual(seeds.count(anySeed), len(seeds), 'Seeds should be random')

if __name__ == "__main__":
    unittest.main()

from datetime import datetime, timezone
import unittest
from ambiguousResultHandler import AmbiguousResultHandler

class TestAmbiguousResultHandler(unittest.TestCase):

    def setUp(self):
        self.some_time = datetime(2019, 10, 14, tzinfo=timezone.utc)
        self.thing = AmbiguousResultHandler('db')

    def tearDown(self):
        pass

    def testBuildFileName(self):
        result = self.thing.buildFileName('Flugzeugring Reverse', 'Audi Quattro', self.some_time.timestamp())
        self.assertEqual(result, '1571011200_FlugzeugringReverse_AudiQuattro.bat', 'did not build file name correctly')


if __name__ == "__main__":
    unittest.main()

from datetime import datetime, timezone
import unittest
from unittest.mock import MagicMock
from timerecorder.ambiguousResultHandler import AmbiguousResultHandler

class TestAmbiguousResultHandler(unittest.TestCase):

    def setUp(self):
        self.now = datetime(2019, 10, 20, tzinfo=timezone.utc)
        self.thing = AmbiguousResultHandler('db')

    def tearDown(self):
        pass

    def testBuildFileName(self):
        result = self.thing.buildFileName('Flugzeugring Reverse', 'Audi Quattro', self.now.timestamp())
        self.assertEqual(result, '1571529600_FlugzeugringReverse_AudiQuattro.bat', 'did not build file name correctly')

    def testFindsOldUpdateScripts(self):
        scripts = ['1570011200_ElRodeo_AudiQuattro.bat', '1571511200_ElRodeo_PoloGTIR5.bat']
        self.thing.listUpdateScripts = MagicMock(return_value = scripts)

        result = self.thing.listOldUpdateScripts(self.now, 'test')

        self.assertEqual(result, scripts[:1])

    def testNoMatchForNewUpdateScripts(self):
        scripts = ['1586335179_ElRodeo_AudiQuattro.bat', '1586335180_ElRodeo_PoloGTIR5.bat']
        self.thing.listUpdateScripts = MagicMock(return_value = scripts)

        result = self.thing.listOldUpdateScripts(self.now, 'test')
        self.assertEqual(result, [])

    def testNoMatchForEmptyUpdateScripts(self):
        scripts = []
        self.thing.listUpdateScripts = MagicMock(return_value = scripts)

        result = self.thing.listOldUpdateScripts(self.now, 'test')
        self.assertEqual(result, [])

    def testCleanUp(self):
        directory = MagicMock()

        self.thing.delete = MagicMock()

        self.thing.listOldUpdateScripts = MagicMock(return_value = ['file'])

        self.thing.cleanUp(directory)

        self.thing.delete.assert_called_with('file')

if __name__ == "__main__":
    unittest.main()

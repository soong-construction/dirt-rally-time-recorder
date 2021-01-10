from datetime import datetime, timezone
import unittest
from unittest.mock import MagicMock
from timerecorder.updateScriptHandler import UpdateScriptHandler, isUpdateScript
from timerecorder import config
from tests.test_base import TestBase

class TestUpdateScriptHandler(TestBase):

    def __init__(self, methodName):
        TestBase.__init__(self, methodName, 'test-files')

    def setUp(self):
        self.now = datetime(2019, 10, 20, tzinfo=timezone.utc)
        self.thing = UpdateScriptHandler('db')

    def tearDown(self):
        pass
    
    def testBuildSqlite3Call(self):
        result = self.thing.buildScript("update table set x=1")
        self.assertNotIn("{}", result, "Failed to insert all placeholders")

    def testBuildFileName(self):
        result = self.thing.buildFileName('Flugzeugring Reverse', 'Audi Quattro', self.now.timestamp())
        self.assertEqual(result, '1571529600_FlugzeugringReverse_AudiQuattro.bat', 'did not build file name correctly')

    def testIsUpdateScript(self):
        self.assertTrue(isUpdateScript("1570011200_ElRodeo_AudiQuattro.bat"))
        self.assertTrue(isUpdateScript("2000010400_UNKNOWN_AudiQuattro.bat"))

        self.assertFalse(isUpdateScript("ElRodeo_AudiQuattro.bat"))
        self.assertFalse(isUpdateScript("1570011200_some_important.dll"))
        self.assertFalse(isUpdateScript("list-laptimes.bat"))

    def testFindsOldUpdateScripts(self):
        scripts = ['1570011200_ElRodeo_AudiQuattro.bat', '1571511200_ElRodeo_PoloGTIR5.bat']
        self.thing.listUpdateScripts = MagicMock(return_value = scripts)

        result = self.thing.listOldUpdateScripts(self.now, 'test')

        self.assertEqual(result, scripts[:1])

    def testFindsOldUpdateScriptsForUserConfiguredRetentionTime(self):
        scripts = ['1570011200_ElRodeo_AudiQuattro.bat', '1571511200_ElRodeo_PoloGTIR5.bat']
        config.get.keep_update_scripts_days = 0
        self.thing.listUpdateScripts = MagicMock(return_value = scripts)
        self.thing.warnShortRetentionTime = MagicMock()

        result = self.thing.listOldUpdateScripts(self.now, 'test')

        self.assertEqual(result, scripts)
        self.thing.warnShortRetentionTime.assert_called_once()

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

        self.thing.listOldUpdateScripts = MagicMock(return_value = ['dir/file'])

        self.thing.cleanUp(directory)

        self.thing.delete.assert_called_with('dir/file')

if __name__ == "__main__":
    unittest.main()

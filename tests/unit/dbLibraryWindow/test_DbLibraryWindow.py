from unittest import TestCase
from unittest.mock import Mock, patch

from PySide2.QtCore import Qt

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.dbLibraryWindow import DbLibraryWindow            # noqa: E402


class TestDbLibraryWindow(TestCase):
    """
    DbLibraryWindow class test cases.
    """
    def setUp(self) -> None:
        """
        Test cases setup.
        """
        self.QMainWindow = \
            'pkgs.dbLibraryWindow.dbLibraryWindow.qtw.QMainWindow.__init__'
        self.DbLibrary = 'pkgs.dbLibraryWindow.dbLibraryWindow.DbLibrary'
        self.loggingMod = 'pkgs.dbLibraryWindow.dbLibraryWindow.logging'
        self.mockedLogger = Mock()
        self.mockedDbLib = Mock()
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(DbLibraryWindow, 'setupUi'), \
                patch.object(DbLibraryWindow, '_setupUi'), \
                patch.object(DbLibraryWindow, '_populateUi'):
            mockedLogMod.getLogger.return_value = self.mockedLogger
            self.dut = DbLibraryWindow(self.mockedDbLib)

    def test_constructorGetLogger(self) -> None:
        """
        The constructor must the get the appropriate logger.
        """
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(DbLibraryWindow, 'setupUi'), \
                patch.object(DbLibraryWindow, '_setupUi'), \
                patch.object(DbLibraryWindow, '_populateUi'):
            DbLibraryWindow(self.mockedDbLib)
            mockedLogMod.getLogger \
                .assert_called_once_with('app.windows.dbLibrary')

    def test_constructorSetupUi(self) -> None:
        """
        The constructor must setup the window UI.
        """
        with patch(self.QMainWindow), patch(self.loggingMod), \
                patch.object(DbLibraryWindow, 'setupUi') as mockedWinSetupUi, \
                patch.object(DbLibraryWindow, '_setupUi') as mockedSetupUi, \
                patch.object(DbLibraryWindow, '_populateUi') as mockedPopUi:
            dut = DbLibraryWindow(self.mockedDbLib)
            mockedWinSetupUi.assert_called_once_with(dut)
            mockedSetupUi.assert_called_once()
            mockedPopUi.assert_called_once()

    def test_setupUiSetupGroupBox(self) -> None:
        """
        The _setupUi must setup all the group boxes UI.
        """
        with patch.object(self.dut, '_setupVerUi') as mockedSetupVer, \
                patch.object(self.dut, '_setupLibInfoUi') \
                as mockedSetupLibInfo, \
                patch.object(self.dut, '_setupConnUi') as mockedSetupConn, \
                patch.object(self.dut, '_setupFileInfoUi') \
                as mockedSetupFileInfo:
            self.dut._setupUi()
            mockedSetupVer.assert_called_once()
            mockedSetupLibInfo.assert_called_once()
            mockedSetupConn.assert_called_once()
            mockedSetupFileInfo.assert_called_once()

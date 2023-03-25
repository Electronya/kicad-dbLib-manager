from unittest import TestCase
from unittest.mock import Mock, patch

from PySide2.QtCore import Qt

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.mainWindow import MainWindow          # noqa: E402


class TestMainWindow(TestCase):
    """
    MainWindow class test cases.
    """
    def setUp(self) -> None:
        """
        Test cases setup.
        """
        self.QMainWindow = \
            'pkgs.mainWindow.mainWindow.qtw.QMainWindow.__init__'
        self.loggingMod = 'pkgs.mainWindow.mainWindow.logging'
        self.mockedLogger = Mock()
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(MainWindow, 'setupUi'), \
                patch.object(MainWindow, 'setWindowState'), \
                patch.object(MainWindow, '_setupActions'):
            mockedLogMod.getLogger.return_value = self.mockedLogger
            self.dut = MainWindow()
        self._setupMockedActions()

    def _setupMockedActions(self) -> None:
        """
        Setup the mocked actions.
        """
        self.dut.actionAbout = Mock()
        self.dut.actionEditDbLib = Mock()
        self.dut.actionNewDbLib = Mock()
        self.dut.actionOpenDbLib = Mock()

    def test_constructorLogger(self) -> None:
        """
        The constructor must get the main window logger.
        """
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(MainWindow, 'setupUi'), \
                patch.object(MainWindow, 'setWindowState'), \
                patch.object(MainWindow, '_setupActions'):
            MainWindow()
            mockedLogMod.getLogger.assert_called_once_with('app.windows.main')

    def test_constructorSetupUi(self) -> None:
        """
        The constructor must setup the main window UI.
        """
        with patch(self.QMainWindow), patch(self.loggingMod), \
                patch.object(MainWindow, 'setupUi') as mockedSetupUi, \
                patch.object(MainWindow, 'setWindowState'), \
                patch.object(MainWindow, '_setupActions'):
            dut = MainWindow()
            mockedSetupUi.assert_called_once_with(dut)

    def test_constructorMaximize(self) -> None:
        """
        The constructor must maximize the main window.
        """
        with patch(self.QMainWindow), patch(self.loggingMod), \
                patch.object(MainWindow, 'setupUi'), \
                patch.object(MainWindow, '_setupActions'), \
                patch.object(MainWindow, 'setWindowState') as mockedSetWinState:    # noqa: E501
            MainWindow()
            mockedSetWinState.assert_called_once_with(Qt.WindowMaximized)

    def test_constructorSetupActions(self) -> None:
        """
        The constructor must setup the main window actions.
        """
        with patch(self.QMainWindow), patch(self.loggingMod), \
                patch.object(MainWindow, 'setupUi'), \
                patch.object(MainWindow, 'setWindowState'), \
                patch.object(MainWindow, '_setupActions') as mockedSetupActions:    # noqa: E501
            MainWindow()
            mockedSetupActions.assert_called_once()

    def test_setupActions(self) -> None:
        """
        The _setupActions method must connect all the main window actions.
        """
        self.dut._setupActions()
        self.dut.actionAbout.triggered.connect.assert_called_once()
        self.dut.actionNewDbLib.triggered.connect \
            .assert_called_once_with(self.dut._newDbLibFile)
        self.dut.actionOpenDbLib.triggered.connect \
            .assert_called_once_with(self.dut._openDbLibFile)
        self.dut.actionEditDbLib.triggered.connect.assert_called_once()

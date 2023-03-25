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
                patch.object(MainWindow, 'setWindowState'):
            mockedLogMod.getLogger.return_value = self.mockedLogger
            self.dut = MainWindow()

    def test_constructorLogger(self) -> None:
        """
        The constructor must get the main window logger.
        """
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(MainWindow, 'setupUi'), \
                patch.object(MainWindow, 'setWindowState'):
            MainWindow()
            mockedLogMod.getLogger.assert_called_once_with('app.windows.main')

    def test_constructorSetupUi(self) -> None:
        """
        The constructor must setup the main window UI.
        """
        with patch(self.QMainWindow), patch(self.loggingMod), \
                patch.object(MainWindow, 'setupUi') as mockedSetupUi, \
                patch.object(MainWindow, 'setWindowState'):
            dut = MainWindow()
            mockedSetupUi.assert_called_once_with(dut)

    def test_constructorMaximize(self) -> None:
        """
        The constructor must maximize the main window.
        """
        with patch(self.QMainWindow), patch(self.loggingMod), \
                patch.object(MainWindow, 'setupUi'), \
                patch.object(MainWindow, 'setWindowState') as mockedSetWinState:    # noqa: E501
            MainWindow()
            mockedSetWinState.assert_called_once_with(Qt.WindowMaximized)

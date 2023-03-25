from unittest import TestCase
from unittest.mock import Mock, patch

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
                patch.object(MainWindow, 'setupUi'):
            mockedLogMod.getLogger.return_value = self.mockedLogger
            self.dut = MainWindow()

    def test_constructorLogger(self) -> None:
        """
        The constructor must get the main window logger.
        """
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(MainWindow, 'setupUi'):
            MainWindow()
            mockedLogMod.getLogger.assert_called_once_with('app.windows.main')

    def test_constructorSetupUi(self) -> None:
        """
        The constructor must setup the main window UI.
        """
        with patch(self.QMainWindow), patch(self.loggingMod), \
                patch.object(MainWindow, 'setupUi') as mockedSetupUi:
            dut = MainWindow()
            mockedSetupUi.assert_called_once_with(dut)

from unittest import TestCase
from unittest.mock import Mock, patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.appComposer import AppComposer      # noqa: E402


class TestAppComposer(TestCase):
    """
    AppComposer class test cases.
    """
    def setUp(self) -> None:
        self.QAppClass = 'pkgs.appComposer.appComposer.QApplication'
        self.MainWindowClass = 'pkgs.appComposer.appComposer.MainWindow'
        self.sys = 'pkgs.appComposer.appComposer.sys'
        self.loggingMod = 'pkgs.appComposer.appComposer.logging'
        self.mockedLogger = Mock()
        self.QApplication = Mock()
        self.AppWindow = Mock()
        with patch(self.loggingMod) as mockedLoggingMod, \
                patch(self.QAppClass) as mockedQApplication, \
                patch(self.MainWindowClass) as mockedAppWindow:
            mockedLoggingMod.getLogger.return_value = self.mockedLogger
            mockedQApplication.return_value = self.QApplication
            mockedAppWindow.return_value = self.AppWindow
            self.testAppComposer = AppComposer()

    def tearDown(self) -> None:
        self.mockedLogger.reset_mock()
        self.QApplication.reset_mock()
        self.AppWindow.reset_mock()

    def test_constructorGetLogger(self):
        """
        The constructor must get the class logger.
        """
        self.mockedLogger.reset_mock()
        with patch(self.loggingMod) as mockedLoggingMod, \
                patch(self.QAppClass), patch(self.MainWindowClass):
            AppComposer()
            mockedLoggingMod.getLogger.assert_called_once_with('app.composer')

    def test_constructorQApplication(self):
        """
        The constructor must create the QApplication.
        """
        with patch(self.loggingMod), \
                patch(self.QAppClass) as mockedQApplication, \
                patch(self.MainWindowClass):
            AppComposer()
            mockedQApplication.assert_called_once()

    def test_constructorAppWindow(self):
        """
        The constructor must create the AppWindow.
        """
        with patch(self.loggingMod), patch(self.QAppClass), \
                patch(self.MainWindowClass) as mockedAppWindow:
            AppComposer()
            mockedAppWindow.assert_called_once_with()

    def test_run(self):
        """
        The run method must show the AppWindow and
        run the QApplication exec_ method.
        """
        with patch(self.sys) as mockedSys:
            execReturn = 0
            self.QApplication.exec_.return_value = execReturn
            self.testAppComposer.run()
            self.AppWindow.show.assert_called_once()
            self.QApplication.exec_.assert_called_once()
            mockedSys.exit.assert_called_once_with(execReturn)

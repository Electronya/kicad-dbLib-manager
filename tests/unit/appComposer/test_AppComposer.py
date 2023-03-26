from unittest import TestCase
from unittest.mock import Mock, patch

from PySide2.QtWidgets import QMessageBox

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
        self.QMsgBox = 'pkgs.appComposer.appComposer.QMessageBox'
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
            self.dut = AppComposer()

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

    def test_constructorMainWindow(self):
        """
        The constructor must create the main window and connect to its signals.
        """
        mockedMainWindow = Mock()
        with patch(self.loggingMod), patch(self.QAppClass), \
                patch(self.MainWindowClass) as mockedMainWindowCls:
            mockedMainWindowCls.return_value = mockedMainWindow
            dut = AppComposer()
            mockedMainWindowCls.assert_called_once_with()
            mockedMainWindow.errSig.connect \
                .assert_called_once_with(dut._createErrorMsgBox)
            mockedMainWindow.dbLibSig.connect \
                .assert_called_once_with(dut._openDbLibEditor)

    def test_run(self):
        """
        The run method must show the AppWindow and
        run the QApplication exec_ method.
        """
        with patch(self.sys) as mockedSys:
            execReturn = 0
            self.QApplication.exec_.return_value = execReturn
            self.dut.run()
            self.AppWindow.show.assert_called_once()
            self.QApplication.exec_.assert_called_once()
            mockedSys.exit.assert_called_once_with(execReturn)

    def test_createErrorMsgBoxLogErr(self) -> None:
        """
        The _createErrorMsgBox method must log the error received.
        """
        errMsg = 'test error'
        with patch(self.QMsgBox):
            self.dut._createErrorMsgBox(QMessageBox.Warning, OSError(errMsg))
            self.mockedLogger.error.assert_called_once_with(f"{errMsg}")

    def test_createErrorMsgBoxMsgBox(self) -> None:
        """
        The _createErrorMsgBox must create, configure and show the error
        message box and close the application when the error level is critical.
        """
        mockedMsgBox = Mock()
        errMsg = 'test error'
        icons = [QMessageBox.Warning, QMessageBox.Critical]
        for icon in icons:
            mockedMsgBox.reset_mock()
            with patch(self.QMsgBox) as mockedMsgBoxCls:
                mockedMsgBoxCls.Warning = QMessageBox.Warning
                mockedMsgBoxCls.Critical = QMessageBox.Critical
                mockedMsgBoxCls.return_value = mockedMsgBox
                self.dut._createErrorMsgBox(icon, OSError(errMsg))
                mockedMsgBoxCls.assert_called_once()
                mockedMsgBox.setWindowTitle.assert_called_once_with('Error!!')
                mockedMsgBox.setText.assert_called_once_with(errMsg)
                mockedMsgBox.setIcon.assert_called_once_with(icon)
                if icon == QMessageBox.Critical:
                    mockedMsgBox.buttonClicked.connect.assert_called_once()
                mockedMsgBox.exec_.assert_called_once()

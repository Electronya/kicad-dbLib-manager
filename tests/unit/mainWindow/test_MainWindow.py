from unittest import TestCase
from unittest.mock import Mock, patch

from PySide2.QtCore import Qt, QDir

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
        self.QFileDialog = 'pkgs.mainWindow.mainWindow.qtw.QFileDialog'
        self.DbLibrary = 'pkgs.mainWindow.mainWindow.DbLibrary'
        self.loggingMod = 'pkgs.mainWindow.mainWindow.logging'
        self.mockedLogger = Mock()
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(MainWindow, 'setupUi'), \
                patch.object(MainWindow, 'setWindowState'), \
                patch.object(MainWindow, '_setupActions'):
            mockedLogMod.getLogger.return_value = self.mockedLogger
            self.dut = MainWindow()
        self._setupMockedSignals()
        self._setupMockedActions()

    def _setupMockedSignals(self) -> None:
        """
        Setup the mocked signals.
        """
        self.dut.errSig = Mock()
        self.dut.aboutSig = Mock()
        self.dut.dbLibSig = Mock()

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
        self.dut.actionEditDbLib.triggered.connect \
            .assert_called_once_with(self.dut._editDbLibFile)

    def test_newDbLibFileSaveDialog(self) -> None:
        """
        The _newDbLibFile method must open a save file dialog box.
        """
        with patch(self.QFileDialog) as mockedFileDialog, \
                patch(self.DbLibrary):
            self.dut._newDbLibFile()
            mockedFileDialog.getSaveFileName \
                .assert_called_once_with(self.dut, caption='New DB Library',
                                         dir=QDir.homePath(),
                                         filter='DB Library (*.kicad_dbl)')

    def test_newDbLibFileCreateLibInst(self) -> None:
        """
        The _newDbLibFile method must create a new DB library instance with
        the path given by the user.
        """
        testFileInfo = ('/home/jbacon/test', 'DB Library (*.kicad_dbl)')
        with patch(self.QFileDialog) as mockedFileDialog, \
                patch(self.DbLibrary) as mockedDbLib:
            mockedFileDialog.getSaveFileName.return_value = testFileInfo
            self.dut._newDbLibFile()
            mockedDbLib.assert_called_once_with(testFileInfo[0], isNew=True)

    def test_newDbLibFileEmitSig(self) -> None:
        """
        The _newDbLibFile method must emit the DB library signal with
        the new instance.
        """
        testLib = Mock()
        with patch(self.QFileDialog), patch(self.DbLibrary) as mockedDbLib:
            mockedDbLib.return_value = testLib
            self.dut._newDbLibFile()
            self.dut.dbLibSig.emit.assert_called_once_with(testLib)

    def test_openDbLibFileOpenDialog(self) -> None:
        """
        The _openDbLibFile method must open an open file dialog box.
        """
        with patch(self.QFileDialog) as mockedFileDialog, \
                patch(self.DbLibrary):
            self.dut._openDbLibFile()
            mockedFileDialog.getOpenFileName \
                .assert_called_once_with(self.dut, caption='Open DB Library',
                                         dir=QDir.homePath(),
                                         filter='DB Library (*.kicad_dbl)')

    def test_openDbLibFileNewInst(self) -> None:
        """
        The _openDbLibFile method must create a new DB library instance with
        the path given by the user.
        """
        testFileInfo = ('/home/jbacon/test', 'DB Library (*.kicad_dbl)')
        with patch(self.QFileDialog) as mockedFileDialog, \
                patch(self.DbLibrary) as mockedDbLib:
            mockedFileDialog.getOpenFileName.return_value = testFileInfo
            self.dut._openDbLibFile()
            mockedDbLib.assert_called_once_with(testFileInfo[0])

    def test_openDbLibFileEnableEdit(self) -> None:
        """
        The _openDbLibFile method must enable the DB library edit action.
        """
        with patch(self.QFileDialog), patch(self.DbLibrary):
            self.dut._openDbLibFile()
            self.dut.actionEditDbLib.setEnabled.assert_called_once_with(True)

    def test_editDbLibFileEmitSig(self) -> None:
        """
        The _editDbLibFile method must emit the DB library signal only when
        a DB library is open.
        """
        dbLibs = (None, Mock())
        for dbLib in dbLibs:
            self.dut._dbLib = dbLib
            self.dut._editDbLibFile()
        self.dut.dbLibSig.emit.assert_called_once_with(dbLibs[1])

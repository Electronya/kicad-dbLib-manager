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
        self._setUpMockedWidget()

    def _setUpMockedWidget(self) -> None:
        """
        Setup the mocked widgets.
        """
        self.dut.ver0Rbtn = Mock()
        self.dut.ver1Rbtn = Mock()
        self.dut.libNameLedit = Mock()
        self.dut.libDescLedit = Mock()
        self.dut.dsnRbtn = Mock()
        self.dut.connStrRbtn = Mock()
        self.dut.dsnCbox = Mock()
        self.dut.dsnUsrLedit = Mock()
        self.dut.dsnPasswordLedit = Mock()
        self.dut.connStrLedit = Mock()
        self.dut.timeoutSbox = Mock()
        self.dut.connTestPbtn = Mock()
        self.dut.fileSavePbtn = Mock()
        self.dut.saveAsPbtn = Mock()
        self.dut.closePbtn = Mock()

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
        The _setupUi method must setup all the group boxes UI.
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

    def test_setupUiCloseBtn(self) -> None:
        """
        The _setupUi method must connect the close button clicked signal.
        """
        with patch.object(self.dut, '_setupVerUi'), \
                patch.object(self.dut, '_setupLibInfoUi'), \
                patch.object(self.dut, '_setupConnUi'), \
                patch.object(self.dut, '_setupFileInfoUi'):
            self.dut._setupUi()
            self.dut.closePbtn.clicked.connect \
                .assert_called_once_with(self.dut._close)

    def test_setupVerUi(self) -> None:
        """
        The _setupVerUi method must connect the version radio buttons toggle
        signals.
        """
        self.dut.ver0Rbtn.text.return_value = 'Version 0'
        self.dut.ver1Rbtn.text.return_value = 'Version 1'
        self.dut._setupVerUi()
        self.dut.ver0Rbtn.toggled.connect.assert_called_once()
        self.dut.ver1Rbtn.toggled.connect.assert_called_once()

    def test_setupLibInfoUi(self) -> None:
        """
        The _setupLibInfoUi method must connect the library name and
        description line edit editing finished signal.
        """
        self.dut._setupLibInfoUi()
        self.dut.libNameLedit.editingFinished.connect.assert_called_once()
        self.dut.libDescLedit.editingFinished.connect.assert_called_once()

    def test_setupConnUiTypeRadioBtn(self) -> None:
        """
        The _setupConnUi method must connect the connection type radio button
        toggled signals.
        """
        self.dut._setupConnUi()
        self.dut.dsnRbtn.toggled.connect.assert_called_once()
        self.dut.connStrRbtn.toggled.connect.assert_called_once()

    def test_setupConnUiLineEdit(self) -> None:
        """
        The _setupConnUi method must connect the line edits of the UI section
        editing finished signals.
        """
        self.dut._setupConnUi()
        self.dut.dsnUsrLedit.editingFinished.connect.assert_called_once()
        self.dut.dsnPasswordLedit.editingFinished.connect.assert_called_once()
        self.dut.connStrLedit.editingFinished.connect.assert_called_once()

    def test_setupConnUiDsnComboBox(self) -> None:
        """
        The _setupConnUi method must connect the DSN combo box current text
        changed signal.
        """
        self.dut._setupConnUi()
        self.dut.dsnCbox.currentTextChanged.connect.assert_called_once()

    def test_setupConnTimeout(self) -> None:
        """
        The _setupConnUi method must connect the timeout spin box value changed
        signal.
        """
        self.dut._setupConnUi()
        self.dut.timeoutSbox.valueChanged.connect.assert_called_once()

    def test_setupConnUiTestBtn(self) -> None:
        """
        The _SetupConnUi method must connect the test button clicked signal and
        connect to the DB library connection test signal.
        """
        self.dut._setupConnUi()
        self.dut.connTestPbtn.clicked.connect.assert_called_once()
        self.dut._dbLib.connTestSig.connect \
            .assert_called_once_with(self.dut._showConnTestResult)

    def test_setupFileInfoUiBtn(self) -> None:
        """
        The _setupFileInfoUi method must connect the save and save as button
        clocked signals.
        """
        self.dut._setupFileInfoUi()
        self.dut.fileSavePbtn.clicked.connect.assert_called_once()
        self.dut.saveAsPbtn.clicked.connect \
            .assert_called_once_with(self.dut._saveLibAs)

from unittest import TestCase
from unittest.mock import call, Mock, patch

from PySide2.QtCore import Qt
import PySide2.QtWidgets as qtw

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
        self.QMessageBox = \
            'pkgs.dbLibraryWindow.dbLibraryWindow.qtw.QMessageBox'
        self.QFileDialog = \
            'pkgs.dbLibraryWindow.dbLibraryWindow.qtw.QFileDialog'
        self.DbLibrary = 'pkgs.dbLibraryWindow.dbLibraryWindow.DbLibrary'
        self.loggingMod = 'pkgs.dbLibraryWindow.dbLibraryWindow.logging'
        self.mockedLogger = Mock()
        self.mockedDbLib = Mock()
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(DbLibraryWindow, 'setupUi'), \
                patch.object(DbLibraryWindow, '_setupUi'), \
                patch.object(DbLibraryWindow, '_populateUi'), \
                patch.object(DbLibraryWindow, 'installEventFilter'):
            mockedLogMod.getLogger.return_value = self.mockedLogger
            self.dut = DbLibraryWindow(self.mockedDbLib)
        self._setUpMockedWidget()
        self.dut.errSig = Mock()

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
        self.dut.filePathLedit = Mock()

    def test_constructorGetLogger(self) -> None:
        """
        The constructor must the get the appropriate logger.
        """
        with patch(self.QMainWindow), patch(self.loggingMod) as mockedLogMod, \
                patch.object(DbLibraryWindow, 'setupUi'), \
                patch.object(DbLibraryWindow, '_setupUi'), \
                patch.object(DbLibraryWindow, '_populateUi'), \
                patch.object(DbLibraryWindow, 'installEventFilter'):
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
                patch.object(DbLibraryWindow, '_populateUi') as mockedPopUi, \
                patch.object(DbLibraryWindow, 'installEventFilter'):
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
                .assert_called_once_with(self.dut.close)

    def test_setupVerUi(self) -> None:
        """
        The _setupVerUi method must connect the version radio buttons clicked
        signals.
        """
        self.dut.ver0Rbtn.text.return_value = 'Version 0'
        self.dut.ver1Rbtn.text.return_value = 'Version 1'
        self.dut._setupVerUi()
        self.dut.ver0Rbtn.clicked.connect.assert_called_once()
        self.dut.ver1Rbtn.clicked.connect.assert_called_once()

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
        clicked signals.
        """
        self.dut._setupConnUi()
        self.dut.dsnRbtn.clicked.connect.assert_called_once()
        self.dut.connStrRbtn.clicked.connect.assert_called_once()

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

    def test_populateUi(self) -> None:
        """
        The _populateUi method must populate all the UI sections.
        """
        with patch.object(self.dut, '_populateVerUi') as mockedVerUi, \
                patch.object(self.dut, '_populateLibInfoUi') as mockedLibUi, \
                patch.object(self.dut, '_populateConnUi') as mockedConnUi, \
                patch.object(self.dut, '_populateFileInfoUi') as mockedFileUi:
            self.dut._populateUi()
            mockedVerUi.assert_called_once()
            mockedLibUi.assert_called_once()
            mockedConnUi.assert_called_once()
            mockedFileUi.assert_called_once()

    def test_populateVerUi(self) -> None:
        """
        The _populateVerUi method must select the DB library version radio
        button.
        """
        versions = (0, 1)
        radioBtns = (self.dut.ver0Rbtn, self.dut.ver1Rbtn)
        for version in versions:
            self.dut._dbLib.getVersion.return_value = version
            self.dut._populateVerUi()
            radioBtns[version].setChecked.assert_called_once_with(True)

    def test_populateLibInfoUi(self) -> None:
        """
        The _populateLibInfoUi method must populate the library name
        and description line edit.
        """
        name = 'test name'
        description = 'test description'
        self.dut._dbLib.getName.return_value = name
        self.dut._dbLib.getDescription.return_value = description
        self.dut._populateLibInfoUi()
        self.dut.libNameLedit.setText.assert_called_once_with(name)
        self.dut.libDescLedit.setText.assert_called_once_with(description)

    def test_populateConnUi(self) -> None:
        """
        The _populateConnUi method must select the right connection type
        based on the connection string and than populate the connection section
        based from the library connection data.
        """
        dsnList = ('dsn 1', 'dsn 2', 'dsn 3')
        dsn = dsnList[1]
        dsnUser = 'test user'
        dsnPsw = 'test password'
        connStrings = ('', 'test connection string')
        timeout = 32
        dsnIdxes = (-1, 1)
        with patch.object(self.dut, '_updateConnectionUi') as mockedUpdateUi:
            for idx, connStr in enumerate(connStrings):
                mockedUpdateUi.reset_mock()
                self.dut.dsnCbox.reset_mock()
                self.dut.dsnUsrLedit.reset_mock()
                self.dut.dsnPasswordLedit.reset_mock()
                self.dut.connStrLedit.reset_mock()
                self.dut.timeoutSbox.reset_mock()
                self.dut._dbLib.getOdbcDsnList.return_value = dsnList
                self.dut._dbLib.getSourceDsn.return_value = dsn
                self.dut._dbLib.getSourceUsername.return_value = dsnUser
                self.dut._dbLib.getSourcePassword.return_value = dsnPsw
                self.dut._dbLib.getSourceConnStr.return_value = connStr
                self.dut._dbLib.getSourceTimeout.return_value = timeout
                self.dut.dsnCbox.findText.return_value = dsnIdxes[idx]
                self.dut._populateConnUi()
                if not connStr:
                    self.dut.dsnRbtn.setChecked.assert_called_once_with(True)
                    mockedUpdateUi.asser_called_once_with(True)
                else:
                    self.dut.connStrRbtn.setChecked \
                        .assert_called_once_with(True)
                    mockedUpdateUi.assert_called_once_with(False)
                self.dut.dsnCbox.addItems.assert_called_once_with(dsnList)
                if dsnIdxes[idx] > 0:
                    self.dut.dsnCbox.setCurrentIndex \
                        .assert_called_once_with(dsnIdxes[idx])
                self.dut.dsnUsrLedit.setText.assert_called_once_with(dsnUser)
                self.dut.dsnPasswordLedit.setText \
                    .assert_called_once_with(dsnPsw)
                self.dut.connStrLedit.setText.assert_called_once_with(connStr)
                self.dut.timeoutSbox.setValue.assert_called_once_with(timeout)

    def test_populateFileInfoUi(self) -> None:
        """
        The _populateFileInfoUi method must populate the file path
        line edit.
        """
        path = './test/path/lib.kicad.dbl'
        self.dut._dbLib.getPath.return_value = path
        self.dut._populateFileInfoUi()
        self.dut.filePathLedit.setText.assert_called_once_with(path)

    def test_updateConnectionUi(self) -> None:
        """
        The _updateConnectionUi method must disable all widgets of the not used
        connection type.
        """
        widgetStates = ((True, False), (False, True))
        connTypes = (True, False)
        for idx, connType in enumerate(connTypes):
            self.dut.dsnCbox.reset_mock()
            self.dut.dsnUsrLedit.reset_mock()
            self.dut.dsnPasswordLedit.reset_mock()
            self.dut.connStrLedit.reset_mock()
            self.dut._updateConnectionUi(connType)
            self.dut.dsnCbox.setEnabled \
                .assert_called_once_with(widgetStates[idx][0])
            self.dut.dsnUsrLedit.setEnabled \
                .assert_called_once_with(widgetStates[idx][0])
            self.dut.dsnPasswordLedit.setEnabled \
                .assert_called_once_with(widgetStates[idx][0])
            self.dut.connStrLedit.setEnabled \
                .assert_called_once_with(widgetStates[idx][1])

    def test_showConnTestResultMessageBox(self) -> None:
        """
        The _showConnTestResult method must open a message box with the given
        icon and message.
        """
        icons = (qtw.QMessageBox.Warning, qtw.QMessageBox.Information)
        messages = ('Unable to connect to database.',
                    'Connection successful.')
        mockedMsgBox = Mock()
        for idx, icon in enumerate(icons):
            mockedMsgBox.reset_mock()
            with patch(self.QMessageBox) as mockedMsgBoxCls:
                mockedMsgBoxCls.return_value = mockedMsgBox
                self.dut._showConnTestResult(icon, messages[idx])
                mockedMsgBoxCls.assert_called_once()
                mockedMsgBox.setWindowTitle \
                    .assert_called_once_with('Test Result')
                mockedMsgBox.setText.assert_called_once_with(messages[idx])
                mockedMsgBox.setIcon.assert_called_once_with(icon)

    def test_saveLibError(self) -> None:
        """
        The _saveLib method must catch any exception from the save operation
        and signal the error.
        """
        errMsg = 'test error'
        self.dut._dbLib.save.side_effect = OSError(errMsg)
        self.dut._saveLib()
        self.dut.errSig.emit.assert_called_once_with(qtw.QMessageBox.Warning,
                                                     errMsg)

    def test_saveLib(self) -> None:
        """
        The _saveLib method must save the library.
        """
        self.dut._saveLib()
        self.dut._dbLib.save.assert_called_once()

    def test_saveLibAsError(self) -> None:
        """
        The _saveLibAS method must catch any exception from the save operation
        and signal the error.
        """
        errMsg = 'test error'
        baseLibPath = 'path/to/library.kicad_dbl'
        newLibPath = 'new/path/library'
        self.mockedDbLib.getPath.return_value = baseLibPath
        self.mockedDbLib.save.side_effect = OSError(errMsg)
        with patch(self.QFileDialog) as mockedFileDialog:
            mockedFileDialog.getSaveFileName.return_value = (newLibPath, '')
            self.dut._saveLibAs()
            self.dut.errSig.emit \
                .assert_called_once_with(qtw.QMessageBox.Warning, errMsg)

    def test_saveLibAsCancel(self) -> None:
        """
        The _saveLibAs method must do nothing else if the user cancel the
        operation.
        """
        baseLibPath = 'path/to/library.kicad_dbl'
        self.mockedDbLib.getPath.return_value = baseLibPath
        with patch(self.QFileDialog) as mockedFileDialog:
            mockedFileDialog.getSaveFileName.return_value = ('', '')
            self.dut._saveLibAs()
            mockedFileDialog.getSaveFileName \
                .assert_called_once_with(self.dut, caption='Save Library As',
                                         dir=baseLibPath,
                                         filter='DB Library (*.kicad_dbl)')
            self.dut._dbLib.save.assert_not_called()

    def test_saveLibAs(self) -> None:
        """
        The _saveLibAs method must open a save dialog window that allow
        the user to save as the current library.
        """
        baseLibPath = 'path/to/library.kicad_dbl'
        newLibPath = 'new/path/library'
        self.mockedDbLib.getPath.return_value = baseLibPath
        with patch(self.QFileDialog) as mockedFileDialog:
            mockedFileDialog.getSaveFileName.return_value = (newLibPath, '')
            self.dut._saveLibAs()
            mockedFileDialog.getSaveFileName \
                .assert_called_once_with(self.dut, caption='Save Library As',
                                         dir=baseLibPath,
                                         filter='DB Library (*.kicad_dbl)')
            self.dut._dbLib.save \
                .assert_called_once_with(path=f"{newLibPath}.kicad_dbl")

    def test_closeEventChangeNotSaved(self) -> None:
        """
        The closeEvent method must notify the user that changes have not been
        saved and ask them to either discard or save the changes
        or cancel the close operation.
        """
        question = 'Unsaved changes detected.\nDou you wish to:\nDiscard, '
        'save or cancel?'
        mockedEvent = Mock()
        self.dut._dbLib.isSaved.return_value = False
        with patch(self.QMessageBox) as mockedMsgBox:
            self.dut.closeEvent(mockedEvent)
            mockedMsgBox.question \
                .assert_called_once_with(self.dut,
                                         'Changed not saved', question,
                                         buttons=(mockedMsgBox.Discard |
                                                  mockedMsgBox.Save |
                                                  mockedMsgBox.Cancel))

    def test_closeEventDiscardChanges(self) -> None:
        """
        The closeEvent method must discard any and all unsaved changes and
        accept the close event when the user choose to do so.
        """
        mockedEvent = Mock()
        self.dut._dbLib.isSaved.return_value = False
        with patch(self.QMessageBox) as mockedMsgBox:
            mockedMsgBox.question.return_value = mockedMsgBox.Discard
            self.dut.closeEvent(mockedEvent)
            self.dut._dbLib.discardChanges.assert_called_once()
            mockedEvent.accept.assert_called_once()

    def test_closeEventSaveChangesError(self) -> None:
        """
        The closeEvent method must catch any exception raise byt the save
        operation when the user choose to save the library.
        """
        errMsg = 'test error'
        mockedEvent = Mock()
        self.dut._dbLib.isSaved.return_value = False
        self.dut._dbLib.save.side_effect = OSError(errMsg)
        with patch(self.QMessageBox) as mockedMsgBox:
            mockedMsgBox.question.return_value = mockedMsgBox.Save
            self.dut.closeEvent(mockedEvent)
            self.dut.errSig.emit \
                .assert_called_once_with(qtw.QMessageBox.Warning, errMsg)

    def test_closeEventSaveChanges(self) -> None:
        """
        The closeEvent method must save any and all unsaved changes and
        accept the close event when the user choose to do so.
        """
        mockedEvent = Mock()
        self.dut._dbLib.isSaved.return_value = False
        with patch(self.QMessageBox) as mockedMsgBox:
            mockedMsgBox.question.return_value = mockedMsgBox.Save
            self.dut.closeEvent(mockedEvent)
            self.dut._dbLib.save.assert_called_once()
            mockedEvent.accept.assert_called_once()

    def test_closeEventCancel(self) -> None:
        """
        The closeEvent method must ignore the close event when the user choose
        to do so.
        """
        mockedEvent = Mock()
        self.dut._dbLib.isSaved.return_value = False
        with patch(self.QMessageBox) as mockedMsgBox:
            mockedMsgBox.question.return_value = mockedMsgBox.Cancel
            self.dut.closeEvent(mockedEvent)
            mockedEvent.ignore.assert_called_once()

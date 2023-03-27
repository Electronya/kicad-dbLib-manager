import logging

import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

from .dbLibraryWindow_auto import Ui_dbLibWindow
from ..dbLibrary import DbLibrary


class DbLibraryWindow(qtw.QMainWindow, Ui_dbLibWindow):
    """
    The DB Library editing window.
    """
    errSig = qtc.Signal(qtw.QMessageBox.Icon, Exception)

    def __init__(self, dbLib: DbLibrary) -> None:
        super(DbLibraryWindow, self).__init__()
        self._logger = logging.getLogger('app.windows.dbLibrary')
        self._logger.info('loading UI...')
        self._dbLib = dbLib
        self.setupUi(self)
        self._setupUi()
        self._populateUi()
        self._logger.info('UI loaded')

    def _setupUi(self) -> None:
        """
        Finalize the UI setup.
        """
        self._setupVerUi()
        self._setupLibInfoUi()
        self._setupConnUi()
        self._setupFileInfoUi()
        self.closePbtn.clicked.connect(self._close)

    def _setupVerUi(self) -> None:
        """
        Setup the version UI.
        """
        ver0 = int(self.ver0Rbtn.text().split()[-1])
        ver1 = int(self.ver1Rbtn.text().split()[-1])
        self.ver0Rbtn.toggled.connect(lambda: self._dbLib.setVersion(ver0))
        self.ver1Rbtn.toggled.connect(lambda: self._dbLib.setVersion(ver1))

    def _setupLibInfoUi(self) -> None:
        """
        Setup the library info UI.
        """
        self.libNameLedit.editingFinished \
            .connect(lambda: self._dbLib.setName(self.libNameLedit.text()))
        self.libDescLedit.editingFinished \
            .connect(lambda: self._dbLib.setNam(self.libDescLedit.text()))

    def _setupConnUi(self) -> None:
        """
        Setup the connection UI.
        """
        dsnType = 'dsn'
        connStrType = 'connStr'
        self.dsnRbtn.toggled.connect(lambda: self._updateConnectionUi(dsnType))
        self.connStrRbtn.toggled \
            .connect(lambda: self._updateConnectionUi(connStrType))
        self.dsnUsrLedit.editingFinished \
            .connect(lambda: self._dbLib.setSourceUsername(self.dsnUsrLedit.text()))        # noqa: E501
        self.dsnPasswordLedit.editingFinished \
            .connect(lambda: self._dbLib.setSourcePassword(self.dsnPasswordLedit.text()))   # noqa: E501
        self.connStrLedit.editingFinished \
            .connect(lambda: self._dbLib.setSourcePassword(self.connStrLedit.text()))       # noqa: E501
        self.dsnCbox.currentTextChanged.connect(self._dbLib.setSourceDsn)
        self.timeoutSbox.valueChanged \
            .connect(lambda: self._dbLib.setSourceTimeout(int(self.timeoutSbox.value())))   # noqa: E501
        self.connTestPbtn.clicked.connect(self._dbLib.testConnection)
        self._dbLib.connTestSig.connect(self._showConnTestResult)

    def _setupFileInfoUi(self) -> None:
        """
        Setup the file info UI.
        """
        self.fileSavePbtn.clicked.connect(self._dbLib.save)
        self.saveAsPbtn.clicked.connect(self._saveLibAs)

    def _populateUi(self) -> None:
        """
        Populate the UI with the DB library information.
        """
        self._populateVerUi()
        self._populateLibInfoUi()
        self._populateConnUi()
        self._populateFileInfoUi()

    def _populateVerUi(self) -> None:
        """
        Populate the version UI.
        """
        radioBtns = (self.ver0Rbtn, self.ver1Rbtn)
        version = self._dbLib.getVersion()
        self._logger.debug(f"populating UI with version: {version}")
        radioBtns[version].setChecked()

    def _populateLibInfoUi(self) -> None:
        """
        Populate the library info UI.
        """
        name = self._dbLib.getName()
        description = self._dbLib.getDescription()
        self._logger.debug(f"populating UI with name: {name} and "
                           f"{description}")
        self.libNameLedit.setText(name)
        self.libDescLedit.setText(description)

    def _populateConnUi(self) -> None:
        """
        Populate the connection UI.
        """
        dsnList = self._dbLib.getOdbcDsnList()
        dsn = self._dbLib.getSourceDsn()
        user = self._dbLib.getSourceUsername()
        password = self._dbLib.getSourcePassword()
        connStr = self._dbLib.getSourceConnStr()
        timeout = self._dbLib.getSourceTimeout()
        if not connStr:
            self.dsnRbtn.setChecked()
        else:
            self.connStrRbtn.setChecked()
        self.dsnCbox.addItems(dsnList)
        for odbcDsn in dsnList:
            if odbcDsn == dsn:
                item = odbcDsn
        self.dsnCbox.setCurrentItem(item)
        self.dsnUsrLedit.setText(user)
        self.dsnPasswordLedit.setText(password)
        self.connStrLedit.setText(connStr)
        self.timeoutSbox.setValue(timeout)

    def _populateFileInfoUi(self) -> None:
        """
        Populate the file info UI.
        """

    @qtc.Slot(str)
    def _updateConnectionUi(self, connType: str) -> None:
        """
        Update the connection UI base on the type selected.

        Params:
            connType:   The connection type selected.
        """

    @qtc.Slot(qtw.QMessageBox.Icon, str)
    def _showConnTestResult(self, icon: qtw.QMessageBox.Icon,
                            resMsg: str) -> None:
        """
        Show the connection tst result message box.

        Params:
            icon:       The connection test icon.
            resMsg:     The connection test result message.
        """

    @qtc.Slot()
    def _saveLibAs(self) -> None:
        """
        Save the DB library as.
        """

    @qtc.Slot()
    def _close(self) -> None:
        """
        Do the checks before closing.
        """

    def eventFilter(self, watched: qtc.QObject, event: qtc.QEvent) -> bool:
        """
        DB library window event filter.

        Params:
            watched:        The event target.
            event:          The event.

        Return
            True if event was handled, False otherwise.
        """
        if event.type() == qtc.QEvent.Close:
            self._logger.info('closing')
            return True
        return False

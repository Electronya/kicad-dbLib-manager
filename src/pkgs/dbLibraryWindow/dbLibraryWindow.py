import logging

import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

from .dbLibraryWindow_auto import Ui_dbLibWindow


class DbLibraryWindow(qtw.QMainWindow, Ui_dbLibWindow):
    """
    The DB Library editing window.
    """
    errSig = qtc.Signal(qtw.QMessageBox.Icon, Exception)

    def __init__(self, dbLib) -> None:
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

    def _setupVerUi(self) -> None:
        """
        Setup the version UI.
        """

    def _setupLibInfoUi(self) -> None:
        """
        Setup the library info UI.
        """

    def _setupConnUi(self) -> None:
        """
        Setup the connection UI.
        """

    def _setupFileInfoUi(self) -> None:
        """
        Setup the file info UI.
        """

    def _populateUi(self) -> None:
        """
        Populate the UI with the DB library information.
        """

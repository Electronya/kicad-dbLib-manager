import logging
import sys

from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import QApplication, QMessageBox

from ..dbLibrary import DbLibrary
from ..dbLibraryWindow import DbLibraryWindow
from ..mainWindow import MainWindow


class AppComposer:
    """
    Application Composer.
    """
    def __init__(self) -> None:
        """
        Constructor.
        """
        self._logger = logging.getLogger('app.composer')
        self._logger.info('creating Qt app')
        self._app = QApplication(sys.argv)
        self._logger.debug('creating UI')
        self._mainWindow = MainWindow()
        self._mainWindow.errSig.connect(self._createErrorMsgBox)
        self._mainWindow.dbLibSig.connect(self._openDbLibEditor)

    def run(self):
        """
        Run the application.
        """
        self._mainWindow.show()
        sys.exit(self._app.exec_())

    @Slot(DbLibrary)
    def _openDbLibEditor(self, dbLib: DbLibrary) -> None:
        """
        Open the DB library editor.
        """
        self._logger.info('opening DB library editor')
        self._dbLibEditor = DbLibraryWindow(dbLib)
        self._dbLibEditor.errSig.connect(self._createErrorMsgBox)
        self._dbLibEditor.setWindowModality(Qt.ApplicationModal)
        self._dbLibEditor.show()

    @Slot(QMessageBox.Icon, Exception)
    def _createErrorMsgBox(self, lvl: QMessageBox.Icon,
                           error: Exception) -> None:
        """
        Create a error message box.
        """
        self._logger.error(str(error))
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Error!!')
        msgBox.setText(str(error))
        msgBox.setIcon(lvl)
        if lvl == QMessageBox.Critical:
            self._logger.debug('connecting to button clicked for critical')
            msgBox.buttonClicked.connect(lambda: sys.exit(1))
        msgBox.exec_()

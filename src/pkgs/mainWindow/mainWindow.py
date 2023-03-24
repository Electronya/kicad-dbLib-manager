import logging
import sys

import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

from .mainWindow_auto import Ui_mainWindow


class MainWindow(qtw.QMainWindow, Ui_mainWindow):
    """
    The application main window.
    """
    def __init__(self) -> None:
        """
        Constructor.
        """
        super(MainWindow, self).__init__()
        self._logger = logging.getLogger('app.windows.main')
        self._logger.info('loading UI...')
        self.setupUi(self)

    @qtc.Slot(qtw.QMessageBox.Icon, Exception)
    def _createErrorMsgBox(self, lvl: qtw.QMessageBox.Icon,
                           error: Exception) -> None:
        """
        Create a error message box.
        """
        self._logger.error(f"error: {str(error)}")
        msgBox = qtw.QMessageBox(self)
        msgBox.setWindowTitle('Error!!')
        msgBox.setText(str(error))
        msgBox.setIcon(lvl)
        if lvl == qtw.QMessageBox.Critical:
            self._logger.debug('connecting to button clicked for critical')
            msgBox.buttonClicked.connect(lambda i: sys.exit(1))
        msgBox.exec_()

import logging

import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

from .dbLibraryWindow_auto import Ui_dbLibWindow


class DbLibraryWindow(qtw.QMainWindow, Ui_dbLibWindow):
    """
    The DB Library editing window.
    """
    def __init__(self, dbLib) -> None:
        super(DbLibraryWindow, self).__init__()
        self._logger = logging.getLogger('app.windows.dbLibrary')
        self._logger.info('loading UI...')
        self.setupUi(self)
        self._logger.info('UI loaded')

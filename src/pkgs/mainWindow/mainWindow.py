import logging

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

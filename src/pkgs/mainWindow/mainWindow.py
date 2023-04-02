import logging

import PySide2.QtCore as qtc
import PySide2.QtWidgets as qtw

from .mainWindow_auto import Ui_mainWindow

from ..dbLibrary import DbLibrary


class MainWindow(qtw.QMainWindow, Ui_mainWindow):
    """
    The application main window.
    """
    errSig = qtc.Signal(qtw.QMessageBox.Icon, Exception)
    aboutSig = qtc.Signal()
    dbLibSig = qtc.Signal(DbLibrary)

    def __init__(self) -> None:
        """
        Constructor.
        """
        super(MainWindow, self).__init__()
        self._logger = logging.getLogger('app.windows.main')
        self._logger.info('loading UI...')
        self._dbLib = None
        self.setupUi(self)
        self.setWindowState(qtc.Qt.WindowMaximized)
        self._setupActions()
        self._logger.info('UI leaded')

    def _setupActions(self) -> None:
        """
        Setup the UI actions.
        """
        self._logger.debug('setting up actions')
        self.actionAbout.triggered.connect(self.aboutSig.emit)
        self.actionNewDbLib.triggered.connect(self._newDbLibFile)
        self.actionOpenDbLib.triggered.connect(self._openDbLibFile)
        self.actionEditDbLib.triggered.connect(self._editDbLibFile)

    @qtc.Slot()
    def _newDbLibFile(self) -> None:
        """
        Create a new DB library file.
        """
        self._logger.debug('creating a new DB library file')
        fileInfo = qtw.QFileDialog \
            .getSaveFileName(self, caption='New DB Library',
                             dir=qtc.QDir.homePath(),
                             filter='DB Library (*.kicad_dbl)')
        if fileInfo[0]:
            self._dbLib = DbLibrary(f"{fileInfo[0]}.kicad_dbl", isNew=True)
            self.actionEditDbLib.setEnabled(True)
            self.dbLibSig.emit(self._dbLib)

    @qtc.Slot()
    def _openDbLibFile(self) -> None:
        """
        Open a DB library file.
        """
        self._logger.debug('opening an existing DB library file')
        fileInfo = qtw.QFileDialog \
            .getOpenFileName(self, caption='Open DB Library',
                             dir=qtc.QDir.homePath(),
                             filter='DB Library (*.kicad_dbl)')
        if fileInfo[0]:
            self._dbLib = DbLibrary(fileInfo[0])
            self.actionEditDbLib.setEnabled(True)

    @qtc.Slot()
    def _editDbLibFile(self) -> None:
        """
        Edit a DB library file.
        """
        self._logger.debug('editing DB library file')
        if self._dbLib is not None:
            self.dbLibSig.emit(self._dbLib)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ..assets import resources

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/windows/icons/app-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.actionNewDbLib = QAction(mainWindow)
        self.actionNewDbLib.setObjectName(u"actionNewDbLib")
        icon1 = QIcon()
        icon1.addFile(u":/tools/icons/new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewDbLib.setIcon(icon1)
        self.actionOpenDbLib = QAction(mainWindow)
        self.actionOpenDbLib.setObjectName(u"actionOpenDbLib")
        icon2 = QIcon()
        icon2.addFile(u":/tools/icons/open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpenDbLib.setIcon(icon2)
        self.actionEditDbLib = QAction(mainWindow)
        self.actionEditDbLib.setObjectName(u"actionEditDbLib")
        icon3 = QIcon()
        icon3.addFile(u":/tools/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEditDbLib.setIcon(icon3)
        self.actionAbout = QAction(mainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.libListGroupBox = QGroupBox(self.centralwidget)
        self.libListGroupBox.setObjectName(u"libListGroupBox")
        self.gridLayout_2 = QGridLayout(self.libListGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.libDelTbtn = QToolButton(self.libListGroupBox)
        self.libDelTbtn.setObjectName(u"libDelTbtn")
        icon4 = QIcon()
        icon4.addFile(u":/tools/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.libDelTbtn.setIcon(icon4)

        self.gridLayout_2.addWidget(self.libDelTbtn, 1, 2, 1, 1)

        self.libEditTbtn = QToolButton(self.libListGroupBox)
        self.libEditTbtn.setObjectName(u"libEditTbtn")
        self.libEditTbtn.setIcon(icon3)

        self.gridLayout_2.addWidget(self.libEditTbtn, 1, 3, 1, 1)

        self.libAddTbtn = QToolButton(self.libListGroupBox)
        self.libAddTbtn.setObjectName(u"libAddTbtn")
        icon5 = QIcon()
        icon5.addFile(u":/tools/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.libAddTbtn.setIcon(icon5)

        self.gridLayout_2.addWidget(self.libAddTbtn, 1, 1, 1, 1)

        self.listView = QListView(self.libListGroupBox)
        self.listView.setObjectName(u"listView")

        self.gridLayout_2.addWidget(self.listView, 0, 0, 1, 4)


        self.gridLayout.addWidget(self.libListGroupBox, 0, 0, 1, 1)

        self.compListGroupBox = QGroupBox(self.centralwidget)
        self.compListGroupBox.setObjectName(u"compListGroupBox")
        self.gridLayout_3 = QGridLayout(self.compListGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.compDelTbtn = QToolButton(self.compListGroupBox)
        self.compDelTbtn.setObjectName(u"compDelTbtn")
        self.compDelTbtn.setIcon(icon4)

        self.gridLayout_3.addWidget(self.compDelTbtn, 1, 2, 1, 1)

        self.compEditTbtn = QToolButton(self.compListGroupBox)
        self.compEditTbtn.setObjectName(u"compEditTbtn")
        self.compEditTbtn.setIcon(icon3)

        self.gridLayout_3.addWidget(self.compEditTbtn, 1, 3, 1, 1)

        self.compAddTbtn = QToolButton(self.compListGroupBox)
        self.compAddTbtn.setObjectName(u"compAddTbtn")
        self.compAddTbtn.setIcon(icon5)

        self.gridLayout_3.addWidget(self.compAddTbtn, 1, 1, 1, 1)

        self.tableView = QTableView(self.compListGroupBox)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 4)


        self.gridLayout.addWidget(self.compListGroupBox, 0, 1, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDB_Library = QMenu(self.menuFile)
        self.menuDB_Library.setObjectName(u"menuDB_Library")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(mainWindow)
        self.toolBar.setObjectName(u"toolBar")
        mainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuDB_Library.menuAction())
        self.menuDB_Library.addAction(self.actionNewDbLib)
        self.menuDB_Library.addAction(self.actionOpenDbLib)
        self.menuDB_Library.addAction(self.actionEditDbLib)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionNewDbLib)
        self.toolBar.addAction(self.actionOpenDbLib)
        self.toolBar.addAction(self.actionEditDbLib)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"KiCad Part Manager", None))
        self.actionNewDbLib.setText(QCoreApplication.translate("mainWindow", u"New", None))
#if QT_CONFIG(tooltip)
        self.actionNewDbLib.setToolTip(QCoreApplication.translate("mainWindow", u"Create a new DB Library", None))
#endif // QT_CONFIG(tooltip)
        self.actionOpenDbLib.setText(QCoreApplication.translate("mainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpenDbLib.setToolTip(QCoreApplication.translate("mainWindow", u"Open a DB Library", None))
#endif // QT_CONFIG(tooltip)
        self.actionEditDbLib.setText(QCoreApplication.translate("mainWindow", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.actionEditDbLib.setToolTip(QCoreApplication.translate("mainWindow", u"Edit the DB Library", None))
#endif // QT_CONFIG(tooltip)
        self.actionAbout.setText(QCoreApplication.translate("mainWindow", u"About", None))
        self.libListGroupBox.setTitle(QCoreApplication.translate("mainWindow", u"Libraries", None))
        self.libDelTbtn.setText("")
        self.libEditTbtn.setText("")
        self.libAddTbtn.setText("")
        self.compListGroupBox.setTitle(QCoreApplication.translate("mainWindow", u"Components", None))
        self.compDelTbtn.setText("")
        self.compEditTbtn.setText("")
        self.compAddTbtn.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"File", None))
        self.menuDB_Library.setTitle(QCoreApplication.translate("mainWindow", u"DB Library", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("mainWindow", u"toolBar", None))
    # retranslateUi


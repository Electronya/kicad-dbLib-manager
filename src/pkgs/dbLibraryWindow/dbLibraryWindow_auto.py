# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbLibraryWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ..assets import resources

class Ui_dbLibSettingsWindow(object):
    def setupUi(self, dbLibSettingsWindow):
        if not dbLibSettingsWindow.objectName():
            dbLibSettingsWindow.setObjectName(u"dbLibSettingsWindow")
        dbLibSettingsWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/windows/icons/app-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        dbLibSettingsWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(dbLibSettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.libInfoGroupBox = QGroupBox(self.centralwidget)
        self.libInfoGroupBox.setObjectName(u"libInfoGroupBox")
        self.horizontalLayout = QHBoxLayout(self.libInfoGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verGroupBox = QGroupBox(self.libInfoGroupBox)
        self.verGroupBox.setObjectName(u"verGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.verGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ver0Rbtn = QRadioButton(self.verGroupBox)
        self.ver0Rbtn.setObjectName(u"ver0Rbtn")
        self.ver0Rbtn.setEnabled(False)
        self.ver0Rbtn.setChecked(True)

        self.verticalLayout_2.addWidget(self.ver0Rbtn)

        self.ver1Rbtn = QRadioButton(self.verGroupBox)
        self.ver1Rbtn.setObjectName(u"ver1Rbtn")
        self.ver1Rbtn.setEnabled(False)

        self.verticalLayout_2.addWidget(self.ver1Rbtn)


        self.horizontalLayout.addWidget(self.verGroupBox)

        self.infoGroupBox = QGroupBox(self.libInfoGroupBox)
        self.infoGroupBox.setObjectName(u"infoGroupBox")
        self.gridLayout = QGridLayout(self.infoGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.libNameLbl = QLabel(self.infoGroupBox)
        self.libNameLbl.setObjectName(u"libNameLbl")

        self.gridLayout.addWidget(self.libNameLbl, 0, 0, 1, 1)

        self.libDescLbl = QLabel(self.infoGroupBox)
        self.libDescLbl.setObjectName(u"libDescLbl")

        self.gridLayout.addWidget(self.libDescLbl, 1, 0, 1, 1)

        self.libNameLedit = QLineEdit(self.infoGroupBox)
        self.libNameLedit.setObjectName(u"libNameLedit")

        self.gridLayout.addWidget(self.libNameLedit, 0, 1, 1, 1)

        self.libDescLedit = QLineEdit(self.infoGroupBox)
        self.libDescLedit.setObjectName(u"libDescLedit")

        self.gridLayout.addWidget(self.libDescLedit, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.infoGroupBox)


        self.gridLayout_6.addWidget(self.libInfoGroupBox, 0, 0, 1, 2)

        self.closePbtn = QPushButton(self.centralwidget)
        self.closePbtn.setObjectName(u"closePbtn")

        self.gridLayout_6.addWidget(self.closePbtn, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.fileInfoGroupBox = QGroupBox(self.centralwidget)
        self.fileInfoGroupBox.setObjectName(u"fileInfoGroupBox")
        self.gridLayout_5 = QGridLayout(self.fileInfoGroupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.filePathLbl = QLabel(self.fileInfoGroupBox)
        self.filePathLbl.setObjectName(u"filePathLbl")

        self.gridLayout_5.addWidget(self.filePathLbl, 0, 0, 1, 1)

        self.filePathLedit = QLineEdit(self.fileInfoGroupBox)
        self.filePathLedit.setObjectName(u"filePathLedit")
        self.filePathLedit.setEnabled(False)

        self.gridLayout_5.addWidget(self.filePathLedit, 0, 1, 1, 3)

        self.saveAsPbtn = QPushButton(self.fileInfoGroupBox)
        self.saveAsPbtn.setObjectName(u"saveAsPbtn")

        self.gridLayout_5.addWidget(self.saveAsPbtn, 1, 3, 1, 1)

        self.fileSavePbtn = QPushButton(self.fileInfoGroupBox)
        self.fileSavePbtn.setObjectName(u"fileSavePbtn")

        self.gridLayout_5.addWidget(self.fileSavePbtn, 1, 2, 1, 1)

        self.gridLayout_5.setColumnStretch(1, 2)

        self.gridLayout_6.addWidget(self.fileInfoGroupBox, 2, 0, 1, 2)

        self.dbConnInfoGroupBox = QGroupBox(self.centralwidget)
        self.dbConnInfoGroupBox.setObjectName(u"dbConnInfoGroupBox")
        self.gridLayout_4 = QGridLayout(self.dbConnInfoGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.timeoutGroupBox = QGroupBox(self.dbConnInfoGroupBox)
        self.timeoutGroupBox.setObjectName(u"timeoutGroupBox")
        self.gridLayout_7 = QGridLayout(self.timeoutGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.timeoutSbox = QSpinBox(self.timeoutGroupBox)
        self.timeoutSbox.setObjectName(u"timeoutSbox")
        self.timeoutSbox.setValue(2)

        self.gridLayout_7.addWidget(self.timeoutSbox, 1, 0, 1, 1)

        self.timeoutLbl = QLabel(self.timeoutGroupBox)
        self.timeoutLbl.setObjectName(u"timeoutLbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeoutLbl.sizePolicy().hasHeightForWidth())
        self.timeoutLbl.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.timeoutLbl, 1, 1, 1, 1)

        self.timeoutTitleLbl = QLabel(self.timeoutGroupBox)
        self.timeoutTitleLbl.setObjectName(u"timeoutTitleLbl")
        self.timeoutTitleLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.timeoutTitleLbl, 0, 0, 1, 2)


        self.gridLayout_4.addWidget(self.timeoutGroupBox, 0, 2, 1, 1)

        self.connTestPbtn = QPushButton(self.dbConnInfoGroupBox)
        self.connTestPbtn.setObjectName(u"connTestPbtn")

        self.gridLayout_4.addWidget(self.connTestPbtn, 1, 2, 1, 1)

        self.connStrGroupBox = QGroupBox(self.dbConnInfoGroupBox)
        self.connStrGroupBox.setObjectName(u"connStrGroupBox")
        self.gridLayout_2 = QGridLayout(self.connStrGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.connStrRbtn = QRadioButton(self.connStrGroupBox)
        self.connStrRbtn.setObjectName(u"connStrRbtn")
        self.connStrRbtn.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.connStrRbtn, 0, 0, 1, 2)

        self.connStrLedit = QLineEdit(self.connStrGroupBox)
        self.connStrLedit.setObjectName(u"connStrLedit")

        self.gridLayout_2.addWidget(self.connStrLedit, 2, 1, 1, 1)

        self.widget = QWidget(self.connStrGroupBox)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 2)

        self.widget_2 = QWidget(self.connStrGroupBox)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.widget_2, 3, 1, 1, 1)

        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(3, 1)

        self.gridLayout_4.addWidget(self.connStrGroupBox, 0, 1, 1, 1)

        self.dsnGroupBox = QGroupBox(self.dbConnInfoGroupBox)
        self.dsnGroupBox.setObjectName(u"dsnGroupBox")
        self.gridLayout_3 = QGridLayout(self.dsnGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dsnRbtn = QRadioButton(self.dsnGroupBox)
        self.dsnRbtn.setObjectName(u"dsnRbtn")
        self.dsnRbtn.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.dsnRbtn, 0, 0, 1, 1)

        self.dsnUsrLbl = QLabel(self.dsnGroupBox)
        self.dsnUsrLbl.setObjectName(u"dsnUsrLbl")

        self.gridLayout_3.addWidget(self.dsnUsrLbl, 1, 0, 1, 1)

        self.dsnPasswordLbl = QLabel(self.dsnGroupBox)
        self.dsnPasswordLbl.setObjectName(u"dsnPasswordLbl")

        self.gridLayout_3.addWidget(self.dsnPasswordLbl, 2, 0, 1, 1)

        self.dsnPasswordLedit = QLineEdit(self.dsnGroupBox)
        self.dsnPasswordLedit.setObjectName(u"dsnPasswordLedit")

        self.gridLayout_3.addWidget(self.dsnPasswordLedit, 2, 1, 1, 1)

        self.dsnCbox = QComboBox(self.dsnGroupBox)
        self.dsnCbox.setObjectName(u"dsnCbox")

        self.gridLayout_3.addWidget(self.dsnCbox, 0, 1, 1, 1)

        self.dsnUsrLedit = QLineEdit(self.dsnGroupBox)
        self.dsnUsrLedit.setObjectName(u"dsnUsrLedit")

        self.gridLayout_3.addWidget(self.dsnUsrLedit, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.dsnGroupBox, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.dbConnInfoGroupBox, 1, 0, 1, 2)

        dbLibSettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dbLibSettingsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        dbLibSettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dbLibSettingsWindow)
        self.statusbar.setObjectName(u"statusbar")
        dbLibSettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(dbLibSettingsWindow)

        QMetaObject.connectSlotsByName(dbLibSettingsWindow)
    # setupUi

    def retranslateUi(self, dbLibSettingsWindow):
        dbLibSettingsWindow.setWindowTitle(QCoreApplication.translate("dbLibSettingsWindow", u"Database Library Settings", None))
        self.libInfoGroupBox.setTitle(QCoreApplication.translate("dbLibSettingsWindow", u"Library Information", None))
        self.verGroupBox.setTitle(QCoreApplication.translate("dbLibSettingsWindow", u"Version", None))
        self.ver0Rbtn.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Version 0", None))
        self.ver1Rbtn.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Version 1", None))
        self.infoGroupBox.setTitle("")
        self.libNameLbl.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Name:", None))
        self.libDescLbl.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Description:", None))
        self.closePbtn.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Close", None))
        self.fileInfoGroupBox.setTitle(QCoreApplication.translate("dbLibSettingsWindow", u"File Information", None))
        self.filePathLbl.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Path:", None))
        self.saveAsPbtn.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Save As", None))
        self.fileSavePbtn.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Save", None))
        self.dbConnInfoGroupBox.setTitle(QCoreApplication.translate("dbLibSettingsWindow", u"Connection Information", None))
        self.timeoutGroupBox.setTitle("")
        self.timeoutLbl.setText(QCoreApplication.translate("dbLibSettingsWindow", u"seconds", None))
        self.timeoutTitleLbl.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Timeout", None))
        self.connTestPbtn.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Test", None))
        self.connStrGroupBox.setTitle("")
        self.connStrRbtn.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Connection String", None))
        self.dsnGroupBox.setTitle("")
        self.dsnRbtn.setText(QCoreApplication.translate("dbLibSettingsWindow", u"DSN:", None))
        self.dsnUsrLbl.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Username:", None))
        self.dsnPasswordLbl.setText(QCoreApplication.translate("dbLibSettingsWindow", u"Password:", None))
    # retranslateUi


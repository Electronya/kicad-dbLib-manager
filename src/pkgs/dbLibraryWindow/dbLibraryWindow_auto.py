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

class Ui_dbLibWindow(object):
    def setupUi(self, dbLibWindow):
        if not dbLibWindow.objectName():
            dbLibWindow.setObjectName(u"dbLibWindow")
        dbLibWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dbLibWindow.sizePolicy().hasHeightForWidth())
        dbLibWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/windows/icons/app-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        dbLibWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(dbLibWindow)
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
        self.filePathLedit.setEnabled(True)
        self.filePathLedit.setReadOnly(True)

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
        self.ConnTypeGroupBox = QGroupBox(self.dbConnInfoGroupBox)
        self.ConnTypeGroupBox.setObjectName(u"ConnTypeGroupBox")
        self.gridLayout_3 = QGridLayout(self.ConnTypeGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dsnUsrLedit = QLineEdit(self.ConnTypeGroupBox)
        self.dsnUsrLedit.setObjectName(u"dsnUsrLedit")

        self.gridLayout_3.addWidget(self.dsnUsrLedit, 1, 1, 1, 1)

        self.dsnRbtn = QRadioButton(self.ConnTypeGroupBox)
        self.dsnRbtn.setObjectName(u"dsnRbtn")
        self.dsnRbtn.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.dsnRbtn, 0, 0, 1, 1)

        self.dsnPasswordLbl = QLabel(self.ConnTypeGroupBox)
        self.dsnPasswordLbl.setObjectName(u"dsnPasswordLbl")

        self.gridLayout_3.addWidget(self.dsnPasswordLbl, 2, 0, 1, 1)

        self.dsnUsrLbl = QLabel(self.ConnTypeGroupBox)
        self.dsnUsrLbl.setObjectName(u"dsnUsrLbl")

        self.gridLayout_3.addWidget(self.dsnUsrLbl, 1, 0, 1, 1)

        self.dsnCbox = QComboBox(self.ConnTypeGroupBox)
        self.dsnCbox.setObjectName(u"dsnCbox")

        self.gridLayout_3.addWidget(self.dsnCbox, 0, 1, 1, 1)

        self.dsnPasswordLedit = QLineEdit(self.ConnTypeGroupBox)
        self.dsnPasswordLedit.setObjectName(u"dsnPasswordLedit")

        self.gridLayout_3.addWidget(self.dsnPasswordLedit, 2, 1, 1, 1)

        self.connStrRbtn = QRadioButton(self.ConnTypeGroupBox)
        self.connStrRbtn.setObjectName(u"connStrRbtn")
        self.connStrRbtn.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.connStrRbtn, 0, 2, 1, 1)

        self.connStrLedit = QLineEdit(self.ConnTypeGroupBox)
        self.connStrLedit.setObjectName(u"connStrLedit")

        self.gridLayout_3.addWidget(self.connStrLedit, 1, 2, 1, 1)


        self.gridLayout_4.addWidget(self.ConnTypeGroupBox, 0, 0, 1, 1)

        self.timeoutGroupBox = QGroupBox(self.dbConnInfoGroupBox)
        self.timeoutGroupBox.setObjectName(u"timeoutGroupBox")
        self.gridLayout_7 = QGridLayout(self.timeoutGroupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.timeoutSbox = QSpinBox(self.timeoutGroupBox)
        self.timeoutSbox.setObjectName(u"timeoutSbox")
        self.timeoutSbox.setValue(2)

        self.gridLayout_7.addWidget(self.timeoutSbox, 0, 0, 1, 1)

        self.timeoutLbl = QLabel(self.timeoutGroupBox)
        self.timeoutLbl.setObjectName(u"timeoutLbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.timeoutLbl.sizePolicy().hasHeightForWidth())
        self.timeoutLbl.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.timeoutLbl, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.timeoutGroupBox, 0, 1, 1, 1)

        self.connTestPbtn = QPushButton(self.dbConnInfoGroupBox)
        self.connTestPbtn.setObjectName(u"connTestPbtn")

        self.gridLayout_4.addWidget(self.connTestPbtn, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.dbConnInfoGroupBox, 1, 0, 1, 2)

        dbLibWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dbLibWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        dbLibWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dbLibWindow)
        self.statusbar.setObjectName(u"statusbar")
        dbLibWindow.setStatusBar(self.statusbar)

        self.retranslateUi(dbLibWindow)

        QMetaObject.connectSlotsByName(dbLibWindow)
    # setupUi

    def retranslateUi(self, dbLibWindow):
        dbLibWindow.setWindowTitle(QCoreApplication.translate("dbLibWindow", u"Database Library Settings", None))
        self.libInfoGroupBox.setTitle(QCoreApplication.translate("dbLibWindow", u"Library Information", None))
        self.verGroupBox.setTitle(QCoreApplication.translate("dbLibWindow", u"Version", None))
        self.ver0Rbtn.setText(QCoreApplication.translate("dbLibWindow", u"Version 0", None))
        self.ver1Rbtn.setText(QCoreApplication.translate("dbLibWindow", u"Version 1", None))
        self.infoGroupBox.setTitle("")
        self.libNameLbl.setText(QCoreApplication.translate("dbLibWindow", u"Name:", None))
        self.libDescLbl.setText(QCoreApplication.translate("dbLibWindow", u"Description:", None))
        self.closePbtn.setText(QCoreApplication.translate("dbLibWindow", u"Close", None))
        self.fileInfoGroupBox.setTitle(QCoreApplication.translate("dbLibWindow", u"File Information", None))
        self.filePathLbl.setText(QCoreApplication.translate("dbLibWindow", u"Path:", None))
        self.saveAsPbtn.setText(QCoreApplication.translate("dbLibWindow", u"Save As", None))
        self.fileSavePbtn.setText(QCoreApplication.translate("dbLibWindow", u"Save", None))
        self.dbConnInfoGroupBox.setTitle(QCoreApplication.translate("dbLibWindow", u"Connection Information", None))
        self.ConnTypeGroupBox.setTitle(QCoreApplication.translate("dbLibWindow", u"Connection Method", None))
        self.dsnRbtn.setText(QCoreApplication.translate("dbLibWindow", u"DSN:", None))
        self.dsnPasswordLbl.setText(QCoreApplication.translate("dbLibWindow", u"Password:", None))
        self.dsnUsrLbl.setText(QCoreApplication.translate("dbLibWindow", u"Username:", None))
        self.connStrRbtn.setText(QCoreApplication.translate("dbLibWindow", u"Connection String", None))
        self.timeoutGroupBox.setTitle(QCoreApplication.translate("dbLibWindow", u"Connection Timeout", None))
        self.timeoutLbl.setText(QCoreApplication.translate("dbLibWindow", u"seconds", None))
        self.connTestPbtn.setText(QCoreApplication.translate("dbLibWindow", u"Test", None))
    # retranslateUi


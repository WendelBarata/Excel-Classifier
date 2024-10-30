# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'excel_classifier.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 304)
        MainWindow.setMaximumSize(QSize(16777215, 304))
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow {\n"
"	background: rgba(0, 62, 74, 0.2);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.fExcelInputFolder = QFrame(self.centralwidget)
        self.fExcelInputFolder.setObjectName(u"fExcelInputFolder")
        self.fExcelInputFolder.setMaximumSize(QSize(16777215, 50))
        self.fExcelInputFolder.setStyleSheet(u"QFrame#fExcelInputFolder {\n"
"	background: transparent;\n"
"	border: 1px solid rgba(23, 83, 104, 0.3);\n"
"	border-radius: 4px\n"
"}")
        self.fExcelInputFolder.setFrameShape(QFrame.StyledPanel)
        self.fExcelInputFolder.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.fExcelInputFolder)
        self.gridLayout.setObjectName(u"gridLayout")
        self.leExcelInputFolder = QLineEdit(self.fExcelInputFolder)
        self.leExcelInputFolder.setObjectName(u"leExcelInputFolder")
        self.leExcelInputFolder.setMinimumSize(QSize(0, 0))
        self.leExcelInputFolder.setMaximumSize(QSize(16777215, 16777215))
        self.leExcelInputFolder.setStyleSheet(u"	padding: 4px 8px;\n"
"	background: transparent;\n"
"	border: None;\n"
"	color: rgb(197, 254, 254);;\n"
"	font-size: 15px;")

        self.gridLayout.addWidget(self.leExcelInputFolder, 0, 1, 1, 1)

        self.btnExcelInputFolder = QPushButton(self.fExcelInputFolder)
        self.btnExcelInputFolder.setObjectName(u"btnExcelInputFolder")
        self.btnExcelInputFolder.setMinimumSize(QSize(80, 0))
        self.btnExcelInputFolder.setMaximumSize(QSize(80, 100))
        self.btnExcelInputFolder.setStyleSheet(u"QPushButton#btnExcelInputFolder {\n"
"  background: rgb(197, 254, 254);;\n"
"  border-radius: 2px;\n"
"\n"
"  font-style: normal;\n"
"  font-weight: 400;\n"
"  font-size: 14px;\n"
"  color: rgb(23, 83, 104);\n"
"}\n"
"\n"
"QPushButton#btnExcelInputFolder:pressed {\n"
"  background: transparent;\n"
"  border: 1px solid rgb(23, 83, 104);\n"
"  border-radius: 4px;\n"
"  color: rgb(177, 235, 255);\n"
"}")

        self.gridLayout.addWidget(self.btnExcelInputFolder, 0, 3, 1, 1)

        self.label = QLabel(self.fExcelInputFolder)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(145, 0))
        self.label.setMaximumSize(QSize(165, 16777215))
        self.label.setStyleSheet(u"	padding: 4px 8px;\n"
"	background: transparent;\n"
"	border: None;\n"
"	color: rgb(46, 178, 178);\n"
"	font-size: 15px;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.fExcelInputFolder, 1, 0, 1, 3)

        self.fColumnTitle = QFrame(self.centralwidget)
        self.fColumnTitle.setObjectName(u"fColumnTitle")
        self.fColumnTitle.setMinimumSize(QSize(0, 70))
        self.fColumnTitle.setMaximumSize(QSize(16777215, 70))
        self.fColumnTitle.setStyleSheet(u"QFrame#fColumnTitle {\n"
"	background: transparent;\n"
"	border: 1px solid rgba(23, 83, 104, 0.3);\n"
"	border-radius: 4px\n"
"}")
        self.fColumnTitle.setFrameShape(QFrame.StyledPanel)
        self.fColumnTitle.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.fColumnTitle)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.leColumnTitle = QLineEdit(self.fColumnTitle)
        self.leColumnTitle.setObjectName(u"leColumnTitle")
        self.leColumnTitle.setStyleSheet(u"	padding: 4px 8px;\n"
"	background: transparent;\n"
"	border: None;\n"
"	color: rgb(197, 254, 254);\n"
"	font-size: 15px;")

        self.gridLayout_3.addWidget(self.leColumnTitle, 0, 1, 1, 1)

        self.label_11 = QLabel(self.fColumnTitle)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"	background: transparent;\n"
"	border: None;\n"
"	color: rgba(46, 178, 178, 0.5);\n"
"	font-size: 10px;")

        self.gridLayout_3.addWidget(self.label_11, 1, 1, 1, 1)

        self.label_4 = QLabel(self.fColumnTitle)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(145, 0))
        self.label_4.setMaximumSize(QSize(165, 16777215))
        self.label_4.setStyleSheet(u"	padding: 4px 8px;\n"
"	background: transparent;\n"
"	border: None;\n"
"	color: rgb(46, 178, 178);\n"
"	font-size: 15px;")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.cbColumnTitle = QComboBox(self.fColumnTitle)
        self.cbColumnTitle.setObjectName(u"cbColumnTitle")
        self.cbColumnTitle.setMinimumSize(QSize(100, 30))
        self.cbColumnTitle.setStyleSheet(u"QComboBox#cbColumnTitle {\n"
"	background: transparent;\n"
" 	font-size: 18px;\n"
"	color: rgb(197, 254, 254);\n"
"	border: None;\n"
"}")

        self.gridLayout_3.addWidget(self.cbColumnTitle, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.fColumnTitle, 3, 0, 1, 3)

        self.btnSplitExcel = QPushButton(self.centralwidget)
        self.btnSplitExcel.setObjectName(u"btnSplitExcel")
        self.btnSplitExcel.setMinimumSize(QSize(150, 0))
        self.btnSplitExcel.setMaximumSize(QSize(164, 27))
        self.btnSplitExcel.setStyleSheet(u"QPushButton#btnSplitExcel {\n"
"  background: rgb(197, 254, 254);;\n"
"  border-radius: 2px;\n"
"\n"
"  font-style: normal;\n"
"  font-weight: 400;\n"
"  font-size: 20px;\n"
"  color: rgb(23, 83, 104);\n"
"}\n"
"\n"
"QPushButton#btnSplitExcel:pressed {\n"
"  background: transparent;\n"
"  border: 1px solid rgb(23, 83, 104);\n"
"  border-radius: 4px;\n"
"  color: rgb(177, 235, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.btnSplitExcel, 4, 2, 1, 1)

        self.fExcelFolderDest = QFrame(self.centralwidget)
        self.fExcelFolderDest.setObjectName(u"fExcelFolderDest")
        self.fExcelFolderDest.setMaximumSize(QSize(16777215, 50))
        self.fExcelFolderDest.setStyleSheet(u"QFrame#fExcelFolderDest {\n"
"	background: transparent;\n"
"	border: 1px solid rgba(23, 83, 104, 0.3);\n"
"	border-radius: 4px\n"
"}")
        self.fExcelFolderDest.setFrameShape(QFrame.StyledPanel)
        self.fExcelFolderDest.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.fExcelFolderDest)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_2 = QLabel(self.fExcelFolderDest)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(145, 0))
        self.label_2.setMaximumSize(QSize(165, 16777215))
        self.label_2.setStyleSheet(u"	padding: 4px 8px;\n"
"	background: transparent;\n"
"	border: None;\n"
"	color: rgb(46, 178, 178);\n"
"	font-size: 15px;")

        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)

        self.leExcelFolderDest = QLineEdit(self.fExcelFolderDest)
        self.leExcelFolderDest.setObjectName(u"leExcelFolderDest")
        self.leExcelFolderDest.setStyleSheet(u"	padding: 4px 8px;\n"
"	background: transparent;\n"
"	border: None;\n"
"	color: rgb(197, 254, 254);;\n"
"	font-size: 15px;")

        self.gridLayout_8.addWidget(self.leExcelFolderDest, 0, 1, 1, 1)

        self.btnExcelFolderDest = QPushButton(self.fExcelFolderDest)
        self.btnExcelFolderDest.setObjectName(u"btnExcelFolderDest")
        self.btnExcelFolderDest.setMinimumSize(QSize(80, 0))
        self.btnExcelFolderDest.setMaximumSize(QSize(16777215, 100))
        self.btnExcelFolderDest.setStyleSheet(u"QPushButton#btnExcelFolderDest {\n"
"  background: rgb(197, 254, 254);;\n"
"  border-radius: 2px;\n"
"\n"
"  font-style: normal;\n"
"  font-weight: 400;\n"
"  font-size: 14px;\n"
"  color: rgb(23, 83, 104);\n"
"}\n"
"\n"
"QPushButton#btnExcelFolderDest:pressed {\n"
"  background: transparent;\n"
"  border: 1px solid rgb(23, 83, 104);\n"
"  border-radius: 4px;\n"
"  color: rgb(177, 235, 255);\n"
"}")

        self.gridLayout_8.addWidget(self.btnExcelFolderDest, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.fExcelFolderDest, 2, 0, 1, 3)

        self.leStatusBar = QLineEdit(self.centralwidget)
        self.leStatusBar.setObjectName(u"leStatusBar")
        self.leStatusBar.setStyleSheet(u"	padding: 4px 8px;\n"
"	background: transparent;\n"
"	border: None;\n"
"	color: rgb(46, 178, 178);\n"
"	font-size: 17px;")

        self.gridLayout_7.addWidget(self.leStatusBar, 4, 1, 1, 1)

        self.lbTitle = QLabel(self.centralwidget)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setStyleSheet(u"QLabel#lbTitle {\n"
"	padding: 4px 8px;\n"
"	background: transparent;\n"
"	border: None;\n"
"	color: rgb(197, 254, 254);;\n"
"	font-size: 24px;\n"
"	font-weight: 700\n"
"}")
        self.lbTitle.setFrameShape(QFrame.NoFrame)
        self.lbTitle.setFrameShadow(QFrame.Plain)
        self.lbTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lbTitle, 0, 0, 1, 3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"	background: transparent;\n"
"	border: None;\n"
"	color: rgba(46, 178, 178, 0.5);\n"
"	font-size: 10px;")

        self.gridLayout_7.addWidget(self.label_3, 5, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.leExcelInputFolder, self.leColumnTitle)
        QWidget.setTabOrder(self.leColumnTitle, self.btnExcelInputFolder)
        QWidget.setTabOrder(self.btnExcelInputFolder, self.btnSplitExcel)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.leExcelInputFolder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Folder with the Excel files to be split.", None))
        self.btnExcelInputFolder.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Source Folder", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Type the title of the column into which the files should be divided.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Column Title", None))
        self.btnSplitExcel.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destination Folder", None))
        self.leExcelFolderDest.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Destination folder for the separated files.", None))
        self.btnExcelFolderDest.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindow", u"Excel Classifier", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0 by Wendel Isaias Barata", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kicad_image_layers.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1041, 366)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 190, 941, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.PB_Layer1_Path = QPushButton(self.layoutWidget)
        self.PB_Layer1_Path.setObjectName(u"PB_Layer1_Path")

        self.horizontalLayout.addWidget(self.PB_Layer1_Path)

        self.LE_Layer1_Path = QLineEdit(self.layoutWidget)
        self.LE_Layer1_Path.setObjectName(u"LE_Layer1_Path")

        self.horizontalLayout.addWidget(self.LE_Layer1_Path)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 230, 941, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PB_Layer2_Path = QPushButton(self.layoutWidget1)
        self.PB_Layer2_Path.setObjectName(u"PB_Layer2_Path")

        self.horizontalLayout_2.addWidget(self.PB_Layer2_Path)

        self.LE_Layer2_Path = QLineEdit(self.layoutWidget1)
        self.LE_Layer2_Path.setObjectName(u"LE_Layer2_Path")

        self.horizontalLayout_2.addWidget(self.LE_Layer2_Path)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(60, 270, 941, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PB_Layer3_Path = QPushButton(self.layoutWidget2)
        self.PB_Layer3_Path.setObjectName(u"PB_Layer3_Path")

        self.horizontalLayout_3.addWidget(self.PB_Layer3_Path)

        self.LE_Layer3_Path = QLineEdit(self.layoutWidget2)
        self.LE_Layer3_Path.setObjectName(u"LE_Layer3_Path")

        self.horizontalLayout_3.addWidget(self.LE_Layer3_Path)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(280, 140, 431, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.LB_Layer3_Color = QLabel(self.layoutWidget_2)
        self.LB_Layer3_Color.setObjectName(u"LB_Layer3_Color")

        self.horizontalLayout_6.addWidget(self.LB_Layer3_Color)

        self.LE_Layer3_Color = QLineEdit(self.layoutWidget_2)
        self.LE_Layer3_Color.setObjectName(u"LE_Layer3_Color")

        self.horizontalLayout_6.addWidget(self.LE_Layer3_Color)

        self.CB_Layer3_Color = QComboBox(self.layoutWidget_2)
        self.CB_Layer3_Color.setObjectName(u"CB_Layer3_Color")

        self.horizontalLayout_6.addWidget(self.CB_Layer3_Color)

        self.PB_Layer3_Color = QPushButton(self.layoutWidget_2)
        self.PB_Layer3_Color.setObjectName(u"PB_Layer3_Color")
        icon = QIcon()
        icon.addFile(u"../98191da8/color-picker.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PB_Layer3_Color.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.PB_Layer3_Color)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(280, 80, 431, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.LB_Layer1_Color = QLabel(self.layoutWidget3)
        self.LB_Layer1_Color.setObjectName(u"LB_Layer1_Color")

        self.horizontalLayout_4.addWidget(self.LB_Layer1_Color)

        self.LE_Layer1_Color = QLineEdit(self.layoutWidget3)
        self.LE_Layer1_Color.setObjectName(u"LE_Layer1_Color")

        self.horizontalLayout_4.addWidget(self.LE_Layer1_Color)

        self.CB_Layer1_Color = QComboBox(self.layoutWidget3)
        self.CB_Layer1_Color.setObjectName(u"CB_Layer1_Color")

        self.horizontalLayout_4.addWidget(self.CB_Layer1_Color)

        self.PB_Layer1_Color = QPushButton(self.layoutWidget3)
        self.PB_Layer1_Color.setObjectName(u"PB_Layer1_Color")
        self.PB_Layer1_Color.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.PB_Layer1_Color)

        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(280, 110, 431, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.LB_Layer2_Color = QLabel(self.layoutWidget4)
        self.LB_Layer2_Color.setObjectName(u"LB_Layer2_Color")

        self.horizontalLayout_5.addWidget(self.LB_Layer2_Color)

        self.LE_Layer2_Color = QLineEdit(self.layoutWidget4)
        self.LE_Layer2_Color.setObjectName(u"LE_Layer2_Color")

        self.horizontalLayout_5.addWidget(self.LE_Layer2_Color)

        self.CB_Layer2_Color = QComboBox(self.layoutWidget4)
        self.CB_Layer2_Color.setObjectName(u"CB_Layer2_Color")

        self.horizontalLayout_5.addWidget(self.CB_Layer2_Color)

        self.PB_Layer2_Color = QPushButton(self.layoutWidget4)
        self.PB_Layer2_Color.setObjectName(u"PB_Layer2_Color")
        self.PB_Layer2_Color.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.PB_Layer2_Color)

        self.layoutWidget5 = QWidget(self.centralwidget)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(70, 30, 931, 25))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.PB_PNG_Path = QPushButton(self.layoutWidget5)
        self.PB_PNG_Path.setObjectName(u"PB_PNG_Path")

        self.horizontalLayout_7.addWidget(self.PB_PNG_Path)

        self.LE_PNG_Path = QLineEdit(self.layoutWidget5)
        self.LE_PNG_Path.setObjectName(u"LE_PNG_Path")

        self.horizontalLayout_7.addWidget(self.LE_PNG_Path)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1041, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.PB_Layer1_Path.setText(QCoreApplication.translate("MainWindow", u"LAYER 1 PATH:", None))
        self.PB_Layer2_Path.setText(QCoreApplication.translate("MainWindow", u"LAYER 2 PATH:", None))
        self.PB_Layer3_Path.setText(QCoreApplication.translate("MainWindow", u"LAYER 3 PATH:", None))
        self.LB_Layer3_Color.setText(QCoreApplication.translate("MainWindow", u"LAYER 3 COLOR:", None))
        self.PB_Layer3_Color.setText("")
        self.LB_Layer1_Color.setText(QCoreApplication.translate("MainWindow", u"LAYER 1 COLOR:", None))
        self.PB_Layer1_Color.setText("")
        self.LB_Layer2_Color.setText(QCoreApplication.translate("MainWindow", u"LAYER 2 COLOR:", None))
        self.PB_Layer2_Color.setText("")
        self.PB_PNG_Path.setText(QCoreApplication.translate("MainWindow", u"PNG PATH:", None))
    # retranslateUi


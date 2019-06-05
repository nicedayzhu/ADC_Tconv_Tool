# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adcUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 280)
        MainWindow.setMinimumSize(QtCore.QSize(430, 250))
        MainWindow.setMaximumSize(QtCore.QSize(460, 280))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 379, 135))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_clockPresc = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_clockPresc.setObjectName("lineEdit_clockPresc")
        self.gridLayout.addWidget(self.lineEdit_clockPresc, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_APB2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_APB2.setObjectName("lineEdit_APB2")
        self.gridLayout.addWidget(self.lineEdit_APB2, 0, 1, 1, 1)
        self.lineEdit_sampleTime = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_sampleTime.setObjectName("lineEdit_sampleTime")
        self.gridLayout.addWidget(self.lineEdit_sampleTime, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_Tconv_t = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Tconv_t.setObjectName("lineEdit_Tconv_t")
        self.gridLayout.addWidget(self.lineEdit_Tconv_t, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)
        self.lineEdit_Fconv = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Fconv.setObjectName("lineEdit_Fconv")
        self.gridLayout.addWidget(self.lineEdit_Fconv, 4, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 160, 195, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STM32F4xx ADC Convert Time"))
        self.label.setText(_translate("MainWindow", "APB2 Clock"))
        self.label_7.setText(_translate("MainWindow", "us"))
        self.label_5.setText(_translate("MainWindow", "Cycles"))
        self.label_6.setText(_translate("MainWindow", "Total Convert time"))
        self.label_4.setText(_translate("MainWindow", "Mhz"))
        self.label_2.setText(_translate("MainWindow", "ADC_Clock_Presc"))
        self.label_3.setText(_translate("MainWindow", "Sample Time"))
        self.label_8.setText(_translate("MainWindow", "Convert Speed"))
        self.label_9.setText(_translate("MainWindow", "Mhz"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))

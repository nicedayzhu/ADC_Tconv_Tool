#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 10:41
# @Author  : SeniorZhu1994
# @Email   : SeniorZhu1994@foxmail.com
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from adcUI import Ui_MainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton_2.clicked.connect(self.clearInput)

    def calculate(self):
        try:
            APB2_clk = int(self.lineEdit_APB2.text())
            ADC_clockPresc = int(self.lineEdit_clockPresc.text())
            SampleTime = int(self.lineEdit_sampleTime.text())
            ADC_Clk = APB2_clk / ADC_clockPresc
            Tconv_c = SampleTime + 12
            T_ADC = 1 / ADC_Clk
            Tconv_t = T_ADC * Tconv_c
            self.lineEdit_Tconv_t.setText(str(Tconv_t))
            Freq_conv = 1 / Tconv_t
            self.lineEdit_Fconv.setText(str(Freq_conv))
        except Exception as er:
            pass

    def clearInput(self):
        self.lineEdit_APB2.clear()
        self.lineEdit_clockPresc.clear()
        self.lineEdit_sampleTime.clear()
        self.lineEdit_Tconv_t.clear()
        self.lineEdit_Fconv.clear()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
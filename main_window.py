# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_project\web_wpider\main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_box = QtWidgets.QTextEdit(self.centralwidget)
        self.input_box.setGeometry(QtCore.QRect(210, 100, 361, 87))
        self.input_box.setObjectName("input_box")
        self.output_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_box.setGeometry(QtCore.QRect(210, 240, 361, 101))
        self.output_box.setObjectName("output_box")
        self.btn_translate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_translate.setGeometry(QtCore.QRect(220, 390, 131, 71))
        self.btn_translate.setObjectName("btn_translate")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(430, 390, 131, 71))
        self.btn_reset.setObjectName("btn_reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_translate.setText(_translate("MainWindow", "翻译"))
        self.btn_reset.setText(_translate("MainWindow", "重置"))

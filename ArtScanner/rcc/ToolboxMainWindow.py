# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_dev\toolbox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from rcc.CustomWidgets import DropTextEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        font = QtGui.QFont()
        font.setFamily("HYWenHei-85W")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("HYWenHei-85W")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("HYWenHei-85W")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.textEdit = DropTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setPlaceholderText("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_3.addWidget(self.textEdit_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "「天目」工具箱"))
        self.groupBox_3.setTitle(_translate("MainWindow", "格式选择"))
        self.comboBox.setItemText(0, _translate("MainWindow", "莫娜占卜铺"))
        self.comboBox.setItemText(1, _translate("MainWindow", "原魔计算器"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GOOD"))
        self.label.setText(_translate("MainWindow", "⟹"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "莫娜占卜铺"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "原魔计算器"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "GOOD"))
        self.pushButton_2.setText(_translate("MainWindow", "导入..."))
        self.pushButton.setText(_translate("MainWindow", "转换"))
        self.groupBox.setTitle(_translate("MainWindow", "输入"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "将文件拖至此处"))
        self.groupBox_2.setTitle(_translate("MainWindow", "输出"))
        self.pushButton_3.setText(_translate("MainWindow", "复制"))
        self.pushButton_4.setText(_translate("MainWindow", "导出..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "格式转换器"))

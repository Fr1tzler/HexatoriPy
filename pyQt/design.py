# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HexatoriPy(object):
    def setupUi(self, HexatoriPy):
        HexatoriPy.setObjectName("HexatoriPy")
        HexatoriPy.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HexatoriPy.sizePolicy().hasHeightForWidth())
        HexatoriPy.setSizePolicy(sizePolicy)
        HexatoriPy.setMinimumSize(QtCore.QSize(800, 600))
        HexatoriPy.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(HexatoriPy)
        self.centralwidget.setObjectName("centralwidget")
        self.newGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.newGameButton.setGeometry(QtCore.QRect(640, 40, 120, 119))
        self.newGameButton.setText("")
        self.newGameButton.setObjectName("newGameButton")
        self.hintButton = QtWidgets.QPushButton(self.centralwidget)
        self.hintButton.setGeometry(QtCore.QRect(640, 240, 120, 120))
        self.hintButton.setText("")
        self.hintButton.setObjectName("hintButton")
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton.setGeometry(QtCore.QRect(640, 440, 120, 120))
        self.solveButton.setText("")
        self.solveButton.setObjectName("solveButton")
        HexatoriPy.setCentralWidget(self.centralwidget)

        self.retranslateUi(HexatoriPy)
        QtCore.QMetaObject.connectSlotsByName(HexatoriPy)

    def retranslateUi(self, HexatoriPy):
        _translate = QtCore.QCoreApplication.translate
        HexatoriPy.setWindowTitle(_translate("HexatoriPy", "HexatoriPy"))

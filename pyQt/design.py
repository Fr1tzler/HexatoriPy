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
        self.blackButton = QtWidgets.QPushButton(self.centralwidget)
        self.blackButton.setGeometry(QtCore.QRect(0, 550, 89, 25))
        self.blackButton.setObjectName("blackButton")
        self.whiteButton = QtWidgets.QPushButton(self.centralwidget)
        self.whiteButton.setGeometry(QtCore.QRect(100, 550, 89, 25))
        self.whiteButton.setObjectName("whiteButton")
        HexatoriPy.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(HexatoriPy)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetings = QtWidgets.QMenu(self.menuBar)
        self.menuSetings.setObjectName("menuSetings")
        self.menuHint = QtWidgets.QMenu(self.menuBar)
        self.menuHint.setObjectName("menuHint")
        self.menuDemo = QtWidgets.QMenu(self.menuBar)
        self.menuDemo.setObjectName("menuDemo")
        HexatoriPy.setMenuBar(self.menuBar)
        self.actionSet_size = QtWidgets.QAction(HexatoriPy)
        self.actionSet_size.setObjectName("actionSet_size")
        self.actionEdit_colors = QtWidgets.QAction(HexatoriPy)
        self.actionEdit_colors.setObjectName("actionEdit_colors")
        self.actionUndo = QtWidgets.QAction(HexatoriPy)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(HexatoriPy)
        self.actionRedo.setObjectName("actionRedo")
        self.menuFile.addAction(self.actionSet_size)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUndo)
        self.menuFile.addAction(self.actionRedo)
        self.menuSetings.addAction(self.actionEdit_colors)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSetings.menuAction())
        self.menuBar.addAction(self.menuHint.menuAction())
        self.menuBar.addAction(self.menuDemo.menuAction())

        self.retranslateUi(HexatoriPy)
        QtCore.QMetaObject.connectSlotsByName(HexatoriPy)

    def retranslateUi(self, HexatoriPy):
        _translate = QtCore.QCoreApplication.translate
        HexatoriPy.setWindowTitle(_translate("HexatoriPy", "HexatoriPy"))
        self.blackButton.setText(_translate("HexatoriPy", "black"))
        self.whiteButton.setText(_translate("HexatoriPy", "white"))
        self.menuFile.setTitle(_translate("HexatoriPy", "Game"))
        self.menuSetings.setTitle(_translate("HexatoriPy", "Settings"))
        self.menuHint.setTitle(_translate("HexatoriPy", "Hint"))
        self.menuDemo.setTitle(_translate("HexatoriPy", "Demo"))
        self.actionSet_size.setText(_translate("HexatoriPy", "Set size"))
        self.actionEdit_colors.setText(_translate("HexatoriPy", "Edit colors"))
        self.actionUndo.setText(_translate("HexatoriPy", "Undo"))
        self.actionRedo.setText(_translate("HexatoriPy", "Redo"))

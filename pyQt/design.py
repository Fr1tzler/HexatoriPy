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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(640, 260, 108, 82))
        self.groupBox.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setGeometry(QtCore.QRect(540, 220, 84, 30))
        self.size_label.setMinimumSize(QtCore.QSize(0, 30))
        self.size_label.setObjectName("size_label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(510, 280, 84, 15))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        HexatoriPy.setCentralWidget(self.centralwidget)
        self.actionSet_size = QtWidgets.QAction(HexatoriPy)
        self.actionSet_size.setObjectName("actionSet_size")
        self.actionEdit_colors = QtWidgets.QAction(HexatoriPy)
        self.actionEdit_colors.setObjectName("actionEdit_colors")
        self.actionUndo = QtWidgets.QAction(HexatoriPy)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(HexatoriPy)
        self.actionRedo.setObjectName("actionRedo")

        self.retranslateUi(HexatoriPy)
        QtCore.QMetaObject.connectSlotsByName(HexatoriPy)

    def retranslateUi(self, HexatoriPy):
        _translate = QtCore.QCoreApplication.translate
        HexatoriPy.setWindowTitle(_translate("HexatoriPy", "HexatoriPy"))
        self.blackButton.setText(_translate("HexatoriPy", "black"))
        self.whiteButton.setText(_translate("HexatoriPy", "white"))
        self.size_label.setText(_translate("HexatoriPy", "TextLabel"))
        self.actionSet_size.setText(_translate("HexatoriPy", "Set size"))
        self.actionEdit_colors.setText(_translate("HexatoriPy", "Edit colors"))
        self.actionUndo.setText(_translate("HexatoriPy", "Undo"))
        self.actionRedo.setText(_translate("HexatoriPy", "Redo"))

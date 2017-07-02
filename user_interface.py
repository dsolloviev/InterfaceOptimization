from PyQt5 import QtCore, QtWidgets


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.iterationsLabel = QtWidgets.QLabel(self.frame_2)
        self.iterationsLabel.setText("")
        self.iterationsLabel.setObjectName("iterationsLabel")
        self.horizontalLayout.addWidget(self.iterationsLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.uselessIterationsLabel = QtWidgets.QLabel(self.frame_2)
        self.uselessIterationsLabel.setText("")
        self.uselessIterationsLabel.setObjectName("uselessIterationsLabel")
        self.horizontalLayout_5.addWidget(self.uselessIterationsLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.bestFFLabel = QtWidgets.QLabel(self.frame_2)
        self.bestFFLabel.setText("")
        self.bestFFLabel.setObjectName("bestFFLabel")
        self.horizontalLayout_2.addWidget(self.bestFFLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.currentFFLabel = QtWidgets.QLabel(self.frame_2)
        self.currentFFLabel.setText("")
        self.currentFFLabel.setObjectName("currentFFLabel")
        self.horizontalLayout_3.addWidget(self.currentFFLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.frame_2, 6, 4, 1, 1)
        self.optimizedView = QtWidgets.QGraphicsView(self.centralwidget)
        self.optimizedView.setObjectName("optimizedView")
        self.gridLayout.addWidget(self.optimizedView, 2, 1, 7, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gaRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.gaRadioButton.setEnabled(False)
        self.gaRadioButton.setChecked(True)
        self.gaRadioButton.setObjectName("gaRadioButton")
        self.verticalLayout_2.addWidget(self.gaRadioButton)
        self.beesRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.beesRadioButton.setEnabled(False)
        self.beesRadioButton.setObjectName("beesRadioButton")
        self.verticalLayout_2.addWidget(self.beesRadioButton)
        self.chargesRadioButton = QtWidgets.QRadioButton(self.frame_3)
        self.chargesRadioButton.setEnabled(False)
        self.chargesRadioButton.setObjectName("chargesRadioButton")
        self.verticalLayout_2.addWidget(self.chargesRadioButton)
        self.gridLayout.addWidget(self.frame_3, 4, 4, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pathLabel = QtWidgets.QLabel(self.frame_4)
        self.pathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pathLabel.setObjectName("pathLabel")
        self.verticalLayout_3.addWidget(self.pathLabel)
        self.loadButton = QtWidgets.QPushButton(self.frame_4)
        self.loadButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.loadButton.setObjectName("loadButton")
        self.verticalLayout_3.addWidget(self.loadButton)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.loadButton2 = QtWidgets.QPushButton(self.frame_4)
        self.loadButton2.setObjectName("loadButton2")
        self.verticalLayout_3.addWidget(self.loadButton2)
        self.gridLayout.addWidget(self.frame_4, 2, 4, 1, 1)
        self.initialView = QtWidgets.QGraphicsView(self.centralwidget)
        self.initialView.setObjectName("initialView")
        self.gridLayout.addWidget(self.initialView, 2, 0, 7, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(self.frame)
        self.startButton.setEnabled(False)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.gridLayout.addWidget(self.frame, 8, 4, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.elementsCheckBox = QtWidgets.QCheckBox(self.frame_5)
        self.elementsCheckBox.setEnabled(False)
        self.elementsCheckBox.setChecked(True)
        self.elementsCheckBox.setObjectName("elementsCheckBox")
        self.verticalLayout_5.addWidget(self.elementsCheckBox)
        self.heatmapCheckBox = QtWidgets.QCheckBox(self.frame_5)
        self.heatmapCheckBox.setEnabled(False)
        self.heatmapCheckBox.setChecked(True)
        self.heatmapCheckBox.setObjectName("heatmapCheckBox")
        self.verticalLayout_5.addWidget(self.heatmapCheckBox)
        self.gridLayout.addWidget(self.frame_5, 3, 4, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.showButton = QtWidgets.QPushButton(self.frame_6)
        self.showButton.setEnabled(False)
        self.showButton.setObjectName("showButton")
        self.verticalLayout_6.addWidget(self.showButton)
        self.gridLayout.addWidget(self.frame_6, 7, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interface Optimization"))
        self.label_3.setText(_translate("MainWindow", "Results"))
        self.label_4.setText(_translate("MainWindow", "Total iterations:"))
        self.label_8.setText(_translate("MainWindow", "Useless iterations:"))
        self.label_5.setText(_translate("MainWindow", "Best FF value:"))
        self.label_6.setText(_translate("MainWindow", "Current FF:"))
        self.label.setText(_translate("MainWindow", "Optimization algorithm"))
        self.gaRadioButton.setText(_translate("MainWindow", "Genetic algorithm"))
        self.beesRadioButton.setText(_translate("MainWindow", "Bees algorithm"))
        self.chargesRadioButton.setText(_translate("MainWindow", "Charges algorithm"))
        self.pathLabel.setText(_translate("MainWindow", "Destination interface file"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.label_2.setText(_translate("MainWindow", "Test interface file"))
        self.loadButton2.setText(_translate("MainWindow", "Load"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.elementsCheckBox.setText(_translate("MainWindow", "Show elements\' tree"))
        self.heatmapCheckBox.setText(_translate("MainWindow", "Show heatmap"))
        self.showButton.setText(_translate("MainWindow", "Show best variant"))

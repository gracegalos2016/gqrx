# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gqrx_qtgui.ui'
#
# Created: Tue Nov  9 00:09:56 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 663)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(800, 400))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.sinkLayout = QtGui.QHBoxLayout()
        self.sinkLayout.setObjectName("sinkLayout")
        self.gridLayout.addLayout(self.sinkLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.tuneHorizontalLayout = QtGui.QHBoxLayout()
        self.tuneHorizontalLayout.setObjectName("tuneHorizontalLayout")
        self.tuningSlider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tuningSlider.sizePolicy().hasHeightForWidth())
        self.tuningSlider.setSizePolicy(sizePolicy)
        self.tuningSlider.setMinimum(-125000)
        self.tuningSlider.setMaximum(125000)
        self.tuningSlider.setSingleStep(10)
        self.tuningSlider.setPageStep(100)
        self.tuningSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tuningSlider.setObjectName("tuningSlider")
        self.tuneHorizontalLayout.addWidget(self.tuningSlider)
        self.tuningSpin = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tuningSpin.sizePolicy().hasHeightForWidth())
        self.tuningSpin.setSizePolicy(sizePolicy)
        self.tuningSpin.setMinimum(-125000)
        self.tuningSpin.setMaximum(125000)
        self.tuningSpin.setObjectName("tuningSpin")
        self.tuneHorizontalLayout.addWidget(self.tuningSpin)
        self.verticalLayout.addLayout(self.tuneHorizontalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.freqDownBut2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freqDownBut2.sizePolicy().hasHeightForWidth())
        self.freqDownBut2.setSizePolicy(sizePolicy)
        self.freqDownBut2.setObjectName("freqDownBut2")
        self.gridLayout_2.addWidget(self.freqDownBut2, 0, 0, 1, 1)
        self.freqDownBut1 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freqDownBut1.sizePolicy().hasHeightForWidth())
        self.freqDownBut1.setSizePolicy(sizePolicy)
        self.freqDownBut1.setObjectName("freqDownBut1")
        self.gridLayout_2.addWidget(self.freqDownBut1, 0, 1, 1, 1)
        self.frequencyEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyEdit.sizePolicy().hasHeightForWidth())
        self.frequencyEdit.setSizePolicy(sizePolicy)
        self.frequencyEdit.setMinimumSize(QtCore.QSize(70, 26))
        self.frequencyEdit.setMaxLength(20)
        self.frequencyEdit.setObjectName("frequencyEdit")
        self.gridLayout_2.addWidget(self.frequencyEdit, 0, 2, 1, 1)
        self.freqUpBut1 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freqUpBut1.sizePolicy().hasHeightForWidth())
        self.freqUpBut1.setSizePolicy(sizePolicy)
        self.freqUpBut1.setObjectName("freqUpBut1")
        self.gridLayout_2.addWidget(self.freqUpBut1, 0, 3, 1, 1)
        self.freqUpBut2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freqUpBut2.sizePolicy().hasHeightForWidth())
        self.freqUpBut2.setSizePolicy(sizePolicy)
        self.freqUpBut2.setObjectName("freqUpBut2")
        self.gridLayout_2.addWidget(self.freqUpBut2, 0, 4, 1, 1)
        self.gainLabel = QtGui.QLabel(self.centralwidget)
        self.gainLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gainLabel.setObjectName("gainLabel")
        self.gridLayout_2.addWidget(self.gainLabel, 1, 0, 1, 2)
        self.gainSpin = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gainSpin.sizePolicy().hasHeightForWidth())
        self.gainSpin.setSizePolicy(sizePolicy)
        self.gainSpin.setMaximum(100)
        self.gainSpin.setProperty("value", 50)
        self.gainSpin.setObjectName("gainSpin")
        self.gridLayout_2.addWidget(self.gainSpin, 1, 2, 1, 1)
        self.bandwidthLabel = QtGui.QLabel(self.centralwidget)
        self.bandwidthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bandwidthLabel.setObjectName("bandwidthLabel")
        self.gridLayout_2.addWidget(self.bandwidthLabel, 2, 0, 1, 2)
        self.bandwidthCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandwidthCombo.sizePolicy().hasHeightForWidth())
        self.bandwidthCombo.setSizePolicy(sizePolicy)
        self.bandwidthCombo.setObjectName("bandwidthCombo")
        self.gridLayout_2.addWidget(self.bandwidthCombo, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.filterGridLayout = QtGui.QGridLayout()
        self.filterGridLayout.setObjectName("filterGridLayout")
        self.filterWidthLabel = QtGui.QLabel(self.centralwidget)
        self.filterWidthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filterWidthLabel.setObjectName("filterWidthLabel")
        self.filterGridLayout.addWidget(self.filterWidthLabel, 0, 0, 1, 1)
        self.filterWidthSlider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterWidthSlider.sizePolicy().hasHeightForWidth())
        self.filterWidthSlider.setSizePolicy(sizePolicy)
        self.filterWidthSlider.setMinimum(1000)
        self.filterWidthSlider.setMaximum(15000)
        self.filterWidthSlider.setSingleStep(100)
        self.filterWidthSlider.setPageStep(1000)
        self.filterWidthSlider.setProperty("value", 10000)
        self.filterWidthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.filterWidthSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.filterWidthSlider.setTickInterval(1000)
        self.filterWidthSlider.setObjectName("filterWidthSlider")
        self.filterGridLayout.addWidget(self.filterWidthSlider, 0, 1, 1, 1)
        self.filterWidthSpin = QtGui.QSpinBox(self.centralwidget)
        self.filterWidthSpin.setMinimum(1000)
        self.filterWidthSpin.setMaximum(15000)
        self.filterWidthSpin.setSingleStep(100)
        self.filterWidthSpin.setProperty("value", 10000)
        self.filterWidthSpin.setObjectName("filterWidthSpin")
        self.filterGridLayout.addWidget(self.filterWidthSpin, 0, 2, 1, 1)
        self.filterCenterLabel = QtGui.QLabel(self.centralwidget)
        self.filterCenterLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filterCenterLabel.setObjectName("filterCenterLabel")
        self.filterGridLayout.addWidget(self.filterCenterLabel, 1, 0, 1, 1)
        self.filterCenterSlider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterCenterSlider.sizePolicy().hasHeightForWidth())
        self.filterCenterSlider.setSizePolicy(sizePolicy)
        self.filterCenterSlider.setMinimum(-2000)
        self.filterCenterSlider.setMaximum(2000)
        self.filterCenterSlider.setSingleStep(5)
        self.filterCenterSlider.setPageStep(100)
        self.filterCenterSlider.setOrientation(QtCore.Qt.Horizontal)
        self.filterCenterSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.filterCenterSlider.setTickInterval(1000)
        self.filterCenterSlider.setObjectName("filterCenterSlider")
        self.filterGridLayout.addWidget(self.filterCenterSlider, 1, 1, 1, 1)
        self.filterCenterSpin = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterCenterSpin.sizePolicy().hasHeightForWidth())
        self.filterCenterSpin.setSizePolicy(sizePolicy)
        self.filterCenterSpin.setMinimum(-2000)
        self.filterCenterSpin.setMaximum(2000)
        self.filterCenterSpin.setSingleStep(5)
        self.filterCenterSpin.setProperty("value", 0)
        self.filterCenterSpin.setObjectName("filterCenterSpin")
        self.filterGridLayout.addWidget(self.filterCenterSpin, 1, 2, 1, 1)
        self.filterShapeLabel = QtGui.QLabel(self.centralwidget)
        self.filterShapeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filterShapeLabel.setObjectName("filterShapeLabel")
        self.filterGridLayout.addWidget(self.filterShapeLabel, 2, 0, 1, 1)
        self.filterShapeCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterShapeCombo.sizePolicy().hasHeightForWidth())
        self.filterShapeCombo.setSizePolicy(sizePolicy)
        self.filterShapeCombo.setObjectName("filterShapeCombo")
        self.filterGridLayout.addWidget(self.filterShapeCombo, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.filterGridLayout)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.modeLabel = QtGui.QLabel(self.centralwidget)
        self.modeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.modeLabel.setObjectName("modeLabel")
        self.gridLayout_3.addWidget(self.modeLabel, 0, 0, 1, 1)
        self.modeCombo = QtGui.QComboBox(self.centralwidget)
        self.modeCombo.setObjectName("modeCombo")
        self.gridLayout_3.addWidget(self.modeCombo, 0, 1, 1, 1)
        self.agcLabe = QtGui.QLabel(self.centralwidget)
        self.agcLabe.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.agcLabe.setObjectName("agcLabe")
        self.gridLayout_3.addWidget(self.agcLabe, 1, 0, 1, 1)
        self.agcCombo = QtGui.QComboBox(self.centralwidget)
        self.agcCombo.setObjectName("agcCombo")
        self.gridLayout_3.addWidget(self.agcCombo, 1, 1, 1, 1)
        self.sqlLabel = QtGui.QLabel(self.centralwidget)
        self.sqlLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sqlLabel.setObjectName("sqlLabel")
        self.gridLayout_3.addWidget(self.sqlLabel, 2, 0, 1, 1)
        self.sqlSlider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqlSlider.sizePolicy().hasHeightForWidth())
        self.sqlSlider.setSizePolicy(sizePolicy)
        self.sqlSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sqlSlider.setObjectName("sqlSlider")
        self.gridLayout_3.addWidget(self.sqlSlider, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.volLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volLabel.sizePolicy().hasHeightForWidth())
        self.volLabel.setSizePolicy(sizePolicy)
        self.volLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.volLabel.setObjectName("volLabel")
        self.gridLayout_4.addWidget(self.volLabel, 0, 0, 1, 1)
        self.volSlider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volSlider.sizePolicy().hasHeightForWidth())
        self.volSlider.setSizePolicy(sizePolicy)
        self.volSlider.setMaximum(50)
        self.volSlider.setPageStep(5)
        self.volSlider.setProperty("value", 10)
        self.volSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volSlider.setObjectName("volSlider")
        self.gridLayout_4.addWidget(self.volSlider, 0, 1, 1, 1)
        self.recAudioButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recAudioButton.sizePolicy().hasHeightForWidth())
        self.recAudioButton.setSizePolicy(sizePolicy)
        self.recAudioButton.setCheckable(True)
        self.recAudioButton.setChecked(False)
        self.recAudioButton.setObjectName("recAudioButton")
        self.gridLayout_4.addWidget(self.recAudioButton, 1, 0, 1, 1)
        self.playAudioButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playAudioButton.sizePolicy().hasHeightForWidth())
        self.playAudioButton.setSizePolicy(sizePolicy)
        self.playAudioButton.setCheckable(True)
        self.playAudioButton.setObjectName("playAudioButton")
        self.gridLayout_4.addWidget(self.playAudioButton, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        spacerItem = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.buttonHorizontalLayout = QtGui.QHBoxLayout()
        self.buttonHorizontalLayout.setObjectName("buttonHorizontalLayout")
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(75, 0))
        self.closeButton.setObjectName("closeButton")
        self.buttonHorizontalLayout.addWidget(self.closeButton)
        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setCheckable(True)
        self.pauseButton.setObjectName("pauseButton")
        self.buttonHorizontalLayout.addWidget(self.pauseButton)
        self.recSpectrumButton = QtGui.QPushButton(self.centralwidget)
        self.recSpectrumButton.setCheckable(True)
        self.recSpectrumButton.setObjectName("recSpectrumButton")
        self.buttonHorizontalLayout.addWidget(self.recSpectrumButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonHorizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.buttonHorizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSaveData = QtGui.QAction(MainWindow)
        self.actionSaveData.setObjectName("actionSaveData")
        self.menuFile.addAction(self.actionSaveData)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.filterShapeCombo.setCurrentIndex(-1)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.filterCenterSlider, QtCore.SIGNAL("valueChanged(int)"), self.filterCenterSpin.setValue)
        QtCore.QObject.connect(self.filterCenterSpin, QtCore.SIGNAL("valueChanged(int)"), self.filterCenterSlider.setValue)
        QtCore.QObject.connect(self.filterWidthSlider, QtCore.SIGNAL("valueChanged(int)"), self.filterWidthSpin.setValue)
        QtCore.QObject.connect(self.filterWidthSpin, QtCore.SIGNAL("valueChanged(int)"), self.filterWidthSlider.setValue)
        QtCore.QObject.connect(self.tuningSlider, QtCore.SIGNAL("valueChanged(int)"), self.tuningSpin.setValue)
        QtCore.QObject.connect(self.tuningSpin, QtCore.SIGNAL("valueChanged(int)"), self.tuningSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GQRX", None, QtGui.QApplication.UnicodeUTF8))
        self.freqDownBut2.setText(QtGui.QApplication.translate("MainWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.freqDownBut1.setText(QtGui.QApplication.translate("MainWindow", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.freqUpBut1.setText(QtGui.QApplication.translate("MainWindow", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.freqUpBut2.setText(QtGui.QApplication.translate("MainWindow", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.gainLabel.setText(QtGui.QApplication.translate("MainWindow", "RF Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.bandwidthLabel.setText(QtGui.QApplication.translate("MainWindow", "Bandwidth", None, QtGui.QApplication.UnicodeUTF8))
        self.filterWidthLabel.setText(QtGui.QApplication.translate("MainWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.filterCenterLabel.setText(QtGui.QApplication.translate("MainWindow", "Center", None, QtGui.QApplication.UnicodeUTF8))
        self.filterShapeLabel.setText(QtGui.QApplication.translate("MainWindow", "Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.modeLabel.setText(QtGui.QApplication.translate("MainWindow", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.agcLabe.setText(QtGui.QApplication.translate("MainWindow", "AGC", None, QtGui.QApplication.UnicodeUTF8))
        self.sqlLabel.setText(QtGui.QApplication.translate("MainWindow", "Squelch", None, QtGui.QApplication.UnicodeUTF8))
        self.volLabel.setText(QtGui.QApplication.translate("MainWindow", "AF Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.recAudioButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Record audio", None, QtGui.QApplication.UnicodeUTF8))
        self.recAudioButton.setText(QtGui.QApplication.translate("MainWindow", "Rec", None, QtGui.QApplication.UnicodeUTF8))
        self.playAudioButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Replay the last recorded audio", None, QtGui.QApplication.UnicodeUTF8))
        self.playAudioButton.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pauseButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Pause the receiver", None, QtGui.QApplication.UnicodeUTF8))
        self.pauseButton.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.recSpectrumButton.setText(QtGui.QApplication.translate("MainWindow", "Rec S", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveData.setText(QtGui.QApplication.translate("MainWindow", "&Save Data", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_now_playing = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_now_playing.setFont(font)
        self.label_now_playing.setTextFormat(QtCore.Qt.AutoText)
        self.label_now_playing.setObjectName("label_now_playing")
        self.verticalLayout_2.addWidget(self.label_now_playing)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.inspector = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inspector.sizePolicy().hasHeightForWidth())
        self.inspector.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gtk-info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inspector.setIcon(icon)
        self.inspector.setIconSize(QtCore.QSize(64, 64))
        self.inspector.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.inspector.setObjectName("inspector")
        self.horizontalLayout.addWidget(self.inspector)
        self.loadnew = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadnew.sizePolicy().hasHeightForWidth())
        self.loadnew.setSizePolicy(sizePolicy)
        self.loadnew.setFocusPolicy(QtCore.Qt.TabFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ic_add_to_queue_black_24px.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadnew.setIcon(icon1)
        self.loadnew.setIconSize(QtCore.QSize(64, 64))
        self.loadnew.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.loadnew.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.loadnew.setAutoRaise(False)
        self.loadnew.setArrowType(QtCore.Qt.NoArrow)
        self.loadnew.setObjectName("loadnew")
        self.horizontalLayout.addWidget(self.loadnew)
        self.next = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next.sizePolicy().hasHeightForWidth())
        self.next.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ic_queue_play_next_black_24px.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon2)
        self.next.setIconSize(QtCore.QSize(64, 64))
        self.next.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.nextPlaying = QtWidgets.QLabel(self.centralwidget)
        self.nextPlaying.setEnabled(True)
        self.nextPlaying.setObjectName("nextPlaying")
        self.verticalLayout.addWidget(self.nextPlaying)
        self.table_videos = QtWidgets.QTableView(self.centralwidget)
        self.table_videos.setObjectName("table_videos")
        self.verticalLayout.addWidget(self.table_videos)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuVideo_Queuer = QtWidgets.QMenu(self.menuBar)
        self.menuVideo_Queuer.setObjectName("menuVideo_Queuer")
        MainWindow.setMenuBar(self.menuBar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuVideo_Queuer.addAction(self.actionHelp)
        self.menuVideo_Queuer.addAction(self.actionAbout)
        self.menuVideo_Queuer.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuVideo_Queuer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Scheduling Utility by KVK"))
        self.label_now_playing.setText(_translate("MainWindow", "Playing <File Name>"))
        self.label.setText(_translate("MainWindow", "Time left:"))
        self.inspector.setText(_translate("MainWindow", "Inspect"))
        self.loadnew.setText(_translate("MainWindow", "Load New"))
        self.next.setText(_translate("MainWindow", "Play Next"))
        self.nextPlaying.setText(_translate("MainWindow", " Next Playing: <File Name> in 1:10"))
        self.menuVideo_Queuer.setTitle(_translate("MainWindow", "Video Queuer"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


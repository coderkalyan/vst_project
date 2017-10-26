# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loadnew = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loadnew.setFont(font)
        self.loadnew.setObjectName("loadnew")
        self.horizontalLayout_4.addWidget(self.loadnew)
        self.button_override = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_override.setFont(font)
        self.button_override.setObjectName("button_override")
        self.horizontalLayout_4.addWidget(self.button_override)
        self.button_stop_all = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_stop_all.setFont(font)
        self.button_stop_all.setObjectName("button_stop_all")
        self.horizontalLayout_4.addWidget(self.button_stop_all)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_now_playing = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_now_playing.setFont(font)
        self.title_now_playing.setScaledContents(False)
        self.title_now_playing.setObjectName("title_now_playing")
        self.horizontalLayout.addWidget(self.title_now_playing)
        self.label_now_playing = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_now_playing.setFont(font)
        self.label_now_playing.setObjectName("label_now_playing")
        self.horizontalLayout.addWidget(self.label_now_playing)
        self.label_now_playing_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_now_playing_2.setFont(font)
        self.label_now_playing_2.setObjectName("label_now_playing_2")
        self.horizontalLayout.addWidget(self.label_now_playing_2)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_next_playing = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title_next_playing.setFont(font)
        self.title_next_playing.setScaledContents(False)
        self.title_next_playing.setObjectName("title_next_playing")
        self.horizontalLayout_2.addWidget(self.title_next_playing)
        self.label_next_playing = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_next_playing.setFont(font)
        self.label_next_playing.setObjectName("label_next_playing")
        self.horizontalLayout_2.addWidget(self.label_next_playing)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.schedtable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.schedtable.sizePolicy().hasHeightForWidth())
        self.schedtable.setSizePolicy(sizePolicy)
        self.schedtable.setColumnCount(3)
        self.schedtable.setObjectName("schedtable")
        self.schedtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.schedtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedtable.setHorizontalHeaderItem(2, item)
        self.schedtable.horizontalHeader().setCascadingSectionResizes(False)
        self.schedtable.horizontalHeader().setDefaultSectionSize(300)
        self.schedtable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.schedtable)
        self.verticalLayout.setStretch(4, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 23))
        self.menubar.setObjectName("menubar")
        self.menuVideo_Queuer = QtWidgets.QMenu(self.menubar)
        self.menuVideo_Queuer.setObjectName("menuVideo_Queuer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuVideo_Queuer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Queuer"))
        self.loadnew.setText(_translate("MainWindow", "Load New Video"))
        self.button_override.setText(_translate("MainWindow", "Override"))
        self.button_stop_all.setText(_translate("MainWindow", "Stop All"))
        self.label.setText(_translate("MainWindow", "Time left:"))
        self.title_now_playing.setText(_translate("MainWindow", "Now Playing:"))
        self.label_now_playing.setText(_translate("MainWindow", "<File Name>"))
        self.label_now_playing_2.setText(_translate("MainWindow", "2:03"))
        self.title_next_playing.setText(_translate("MainWindow", "Next:"))
        self.label_next_playing.setText(_translate("MainWindow", "<File Name>"))
        item = self.schedtable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Video File"))
        item = self.schedtable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Length"))
        item = self.schedtable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Start Time"))
        self.menuVideo_Queuer.setTitle(_translate("MainWindow", "Video Queuer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


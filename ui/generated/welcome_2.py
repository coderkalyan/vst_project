# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/welcome_2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(466, 378)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.exit_button = QtWidgets.QPushButton(Dialog)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_2.addWidget(self.exit_button)
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_2.addWidget(self.back_button)
        self.next_button = QtWidgets.QPushButton(Dialog)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout_2.addWidget(self.next_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.welcome_2 = QtWidgets.QWidget()
        self.welcome_2.setObjectName("welcome_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.welcome_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.welcome_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_14 = QtWidgets.QLabel(self.welcome_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.label_20 = QtWidgets.QLabel(self.welcome_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_7.addWidget(self.label_20)
        self.stackedWidget.addWidget(self.welcome_2)
        self.prerequisites_2 = QtWidgets.QWidget()
        self.prerequisites_2.setObjectName("prerequisites_2")
        self.label_22 = QtWidgets.QLabel(self.prerequisites_2)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 430, 87))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.prerequisites_2)
        self.label_24.setGeometry(QtCore.QRect(10, 103, 430, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setScaledContents(False)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.progressBar_2 = QtWidgets.QProgressBar(self.prerequisites_2)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 124, 430, 25))
        self.progressBar_2.setMaximum(0)
        self.progressBar_2.setProperty("value", -1)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.stackedWidget.addWidget(self.prerequisites_2)
        self.getting_started = QtWidgets.QWidget()
        self.getting_started.setObjectName("getting_started")
        self.gridLayoutWidget = QtWidgets.QWidget(self.getting_started)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_39.setTextFormat(QtCore.Qt.RichText)
        self.label_39.setWordWrap(True)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.getting_started)
        self.paying_manually_2 = QtWidgets.QWidget()
        self.paying_manually_2.setObjectName("paying_manually_2")
        self.layoutWidget_8 = QtWidgets.QWidget(self.paying_manually_2)
        self.layoutWidget_8.setGeometry(QtCore.QRect(10, 10, 431, 181))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_10.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setScaledContents(False)
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_10.addWidget(self.label_32)
        self.stackedWidget.addWidget(self.paying_manually_2)
        self.changing_scheduled_videos_2 = QtWidgets.QWidget()
        self.changing_scheduled_videos_2.setObjectName("changing_scheduled_videos_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.changing_scheduled_videos_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_26.setTextFormat(QtCore.Qt.RichText)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_8.addWidget(self.label_26)
        self.stackedWidget.addWidget(self.changing_scheduled_videos_2)
        self.finishing_up_2 = QtWidgets.QWidget()
        self.finishing_up_2.setObjectName("finishing_up_2")
        self.layoutWidget_10 = QtWidgets.QWidget(self.finishing_up_2)
        self.layoutWidget_10.setGeometry(QtCore.QRect(10, 10, 431, 221))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_37 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_12.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setScaledContents(False)
        self.label_38.setWordWrap(True)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_12.addWidget(self.label_38)
        self.stackedWidget.addWidget(self.finishing_up_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Form"))
        self.exit_button.setText(_translate("Dialog", "Exit"))
        self.back_button.setText(_translate("Dialog", "Back"))
        self.next_button.setText(_translate("Dialog", "Next"))
        self.label_5.setText(_translate("Dialog", "KVK Video Scheduler"))
        self.label_14.setText(_translate("Dialog", "Welcome to the KVK Video Scheduler created by Kalyan Sriram, Vincent Wang, and Kai Gottschalk"))
        self.label_20.setText(_translate("Dialog", "This tutorial will assist you in getting this program\n"
" up and running for the first time.\n"
"\n"
" You may exit any time."))
        self.label_22.setText(_translate("Dialog", "Setup and Prerequisites"))
        self.label_24.setText(_translate("Dialog", "Installing prerequisites..."))
        self.label_39.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Getting Started</span></p><ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click <span style=\" font-weight:600;\">Load New Video</span></li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After the dialog opens, click <span style=\" font-weight:600;\">Open Video</span></li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the video you want to play and click <span style=\" font-weight:600;\">Open</span></li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the time you want to play the video in the input fields, or click play manually if you don\'t want the video to autoplay at a certain time</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click <span style=\" font-weight:600;\">OK</span> to schedule the video.</li></ol><p><br/></p></body></html>"))
        self.label_31.setText(_translate("Dialog", "Playing Manually"))
        self.label_32.setText(_translate("Dialog", "If you set a video to play manually, you can play it at any time by right-clicking on the video in the list and click \'Play Manually\'"))
        self.label_26.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Changing Scheduled Videos</span><br/><span style=\" font-size:12pt;\">To change the file name, play time, or other attributes of a video you have already scheduled, do ONE of the following:</span></p><ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Select the video in the list and click </span><span style=\" font-size:12pt; font-weight:600;\">Inspect</span><span style=\" font-size:12pt;\">. This will open a dialog where you can change the file name, play time, etc.</span></li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Double click on any of the cells in the table to edit inline. If you double-click on the file name, a file dialog will open.</span></li></ol></body></html>"))
        self.label_37.setText(_translate("Dialog", "Finishing Up"))
        self.label_38.setText(_translate("Dialog", "You now know how to use this program. To open this tutorial again at any time, select Video Querer -> Tutorial. The settings page(File -> Preferences) will tell you more about the details of this program, and you can customize it there. If you need further assistance, contact Vincent Wang at vw1212@pleasantonusd.net. \n"
"\n"
"\n"
"Advanced: the README.md file also contains information about setup and use of this project, and how to get involved in its development."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


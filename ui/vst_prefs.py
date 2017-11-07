# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vst_prefs.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 479)
        Dialog.setMinimumSize(QtCore.QSize(510, 479))
        Dialog.setMaximumSize(QtCore.QSize(510, 479))
        self.preflab = QtWidgets.QLabel(Dialog)
        self.preflab.setGeometry(QtCore.QRect(0, 10, 509, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        self.preflab.setFont(font)
        self.preflab.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.preflab.setObjectName("preflab")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 161, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.personal_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personal_button.sizePolicy().hasHeightForWidth())
        self.personal_button.setSizePolicy(sizePolicy)
        self.personal_button.setCheckable(False)
        self.personal_button.setObjectName("personal_button")
        self.verticalLayout.addWidget(self.personal_button)
        self.output_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_button.sizePolicy().hasHeightForWidth())
        self.output_button.setSizePolicy(sizePolicy)
        self.output_button.setCheckable(False)
        self.output_button.setObjectName("output_button")
        self.verticalLayout.addWidget(self.output_button)
        self.helpbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpbutton.sizePolicy().hasHeightForWidth())
        self.helpbutton.setSizePolicy(sizePolicy)
        self.helpbutton.setCheckable(False)
        self.helpbutton.setDefault(False)
        self.helpbutton.setFlat(False)
        self.helpbutton.setObjectName("helpbutton")
        self.verticalLayout.addWidget(self.helpbutton)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.savebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savebutton.sizePolicy().hasHeightForWidth())
        self.savebutton.setSizePolicy(sizePolicy)
        self.savebutton.setObjectName("savebutton")
        self.verticalLayout.addWidget(self.savebutton)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 55, 509, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.person = QtWidgets.QFrame(Dialog)
        self.person.setGeometry(QtCore.QRect(180, 60, 321, 411))
        self.person.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person.setFrameShadow(QtWidgets.QFrame.Raised)
        self.person.setObjectName("person")
        self.comboBox = QtWidgets.QComboBox(self.person)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 171, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.person)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.person)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.minimal = QtWidgets.QCheckBox(self.person)
        self.minimal.setGeometry(QtCore.QRect(110, 70, 16, 16))
        self.minimal.setText("")
        self.minimal.setIconSize(QtCore.QSize(24, 24))
        self.minimal.setChecked(False)
        self.minimal.setObjectName("minimal")
        self.showlarge = QtWidgets.QCheckBox(self.person)
        self.showlarge.setGeometry(QtCore.QRect(20, 100, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.showlarge.setFont(font)
        self.showlarge.setObjectName("showlarge")
        self.personal = QtWidgets.QLabel(self.person)
        self.personal.setGeometry(QtCore.QRect(90, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.personal.setFont(font)
        self.personal.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.personal.setObjectName("personal")
        self.helpabout = QtWidgets.QFrame(Dialog)
        self.helpabout.setGeometry(QtCore.QRect(180, 60, 321, 411))
        self.helpabout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpabout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpabout.setObjectName("helpabout")
        self.about = QtWidgets.QTextBrowser(self.helpabout)
        self.about.setGeometry(QtCore.QRect(10, 210, 301, 191))
        self.about.setObjectName("about")
        self.helpbrowse = QtWidgets.QTextBrowser(self.helpabout)
        self.helpbrowse.setGeometry(QtCore.QRect(10, 40, 301, 161))
        self.helpbrowse.setObjectName("helpbrowse")
        self.aboutlbl = QtWidgets.QLabel(self.helpabout)
        self.aboutlbl.setGeometry(QtCore.QRect(100, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.aboutlbl.setFont(font)
        self.aboutlbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.aboutlbl.setObjectName("aboutlbl")
        self.output = QtWidgets.QFrame(Dialog)
        self.output.setGeometry(QtCore.QRect(180, 60, 321, 411))
        self.output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output.setObjectName("output")
        self.path = QtWidgets.QLineEdit(self.output)
        self.path.setGeometry(QtCore.QRect(10, 70, 171, 20))
        self.path.setText("")
        self.path.setFrame(True)
        self.path.setReadOnly(False)
        self.path.setObjectName("path")
        self.cmdlabel = QtWidgets.QLabel(self.output)
        self.cmdlabel.setGeometry(QtCore.QRect(10, 40, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.cmdlabel.setFont(font)
        self.cmdlabel.setObjectName("cmdlabel")
        self.txtlabel = QtWidgets.QLabel(self.output)
        self.txtlabel.setGeometry(QtCore.QRect(10, 130, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtlabel.setFont(font)
        self.txtlabel.setObjectName("txtlabel")
        self.fileout = QtWidgets.QLineEdit(self.output)
        self.fileout.setGeometry(QtCore.QRect(10, 160, 171, 20))
        self.fileout.setText("")
        self.fileout.setFrame(True)
        self.fileout.setReadOnly(False)
        self.fileout.setObjectName("fileout")
        self.namelbl = QtWidgets.QLabel(self.output)
        self.namelbl.setGeometry(QtCore.QRect(10, 180, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.namelbl.setFont(font)
        self.namelbl.setObjectName("namelbl")
        self.name2 = QtWidgets.QLabel(self.output)
        self.name2.setGeometry(QtCore.QRect(10, 100, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.name2.setFont(font)
        self.name2.setObjectName("name2")
        self.output_2 = QtWidgets.QLabel(self.output)
        self.output_2.setGeometry(QtCore.QRect(90, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_2.setFont(font)
        self.output_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.output_2.setObjectName("output_2")

        self.retranslateUi(Dialog)
        self.personal_button.clicked.connect(self.person.show)
        self.output_button.clicked.connect(self.person.hide)
        self.helpbutton.clicked.connect(self.person.hide)
        self.helpbutton.clicked.connect(self.helpabout.show)
        self.output_button.clicked.connect(self.helpabout.hide)
        self.personal_button.clicked.connect(self.helpabout.hide)
        self.output_button.clicked.connect(self.output.show)
        self.helpbutton.clicked.connect(self.output.hide)
        self.personal_button.clicked.connect(self.output.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.preflab.setText(_translate("Dialog", "Preferences"))
        self.personal_button.setText(_translate("Dialog", "Personalization"))
        self.output_button.setText(_translate("Dialog", "Output"))
        self.helpbutton.setText(_translate("Dialog", "Help/About"))
        self.savebutton.setText(_translate("Dialog", "Save"))
        self.comboBox.setItemText(0, _translate("Dialog", "Thing"))
        self.comboBox.setItemText(1, _translate("Dialog", "another thing"))
        self.comboBox.setItemText(2, _translate("Dialog", "one more thing"))
        self.comboBox.setItemText(3, _translate("Dialog", "even another thing"))
        self.comboBox.setItemText(4, _translate("Dialog", "even one more thing"))
        self.comboBox.setItemText(5, _translate("Dialog", "even one more another thing"))
        self.label_2.setText(_translate("Dialog", "Theme"))
        self.label_3.setText(_translate("Dialog", "Minimal UI"))
        self.showlarge.setText(_translate("Dialog", "Show Large Action Buttons"))
        self.personal.setText(_translate("Dialog", "Personalization"))
        self.about.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\">About/Info</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">KVK Video Scheduler Exotic Apple Version 1.5.1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Produced by Vincent Wang, Kalyan Siriam, and Kai Gottschalk.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Made in 2017 for Mrs. Jana Halle\'s 7th and 8th grade Harvest Park Middle School media class. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">UI Design and Coordinator, Backend: Kai Gottschalk</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Backend and Button Bindings: Vincent Wang</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Backend and Scheduler: Kalyan Siriam</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">This programs automatically schedules and plays programs on an alternate screen, particularly for streaming using the HPTV studio equiptment. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Designed in Qt Creator </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Backend Written in Python 3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">No copyright on this program yet...</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p></body></html>"))
        self.helpbrowse.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\">Help</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">How To Use</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Begin by opening the program.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Press New to add a new video to the queue.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">You can tell the video to loop or to play at a certain time.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Frequently Asked Questions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Help me. I dont know how to use program. Can you help me?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Read the How To Use section.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Help! The inspector won\'t work!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">This is a bug that for some reason won\'t stay fixed. Change the video to the same video and try again.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Where do i report bugs?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Call 911, our dedicated help line.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p></body></html>"))
        self.aboutlbl.setText(_translate("Dialog", "Help/About"))
        self.cmdlabel.setText(_translate("Dialog", "Run Command For Video Player"))
        self.txtlabel.setText(_translate("Dialog", "Text File Output"))
        self.namelbl.setText(_translate("Dialog", "\'name of file here\'"))
        self.name2.setText(_translate("Dialog", "\'name of file here\'"))
        self.output_2.setText(_translate("Dialog", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/welcome_3.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.resize(589, 465)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.gridLayout = QtWidgets.QGridLayout(self.wizardPage1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.wizardPage1)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wizardPage2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.wizardPage2)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Wizard"))
        self.wizardPage1.setTitle(_translate("Wizard", "Welcome"))
        self.label.setText(_translate("Wizard", "<html><head/><body><p align=\"center\"><span style=\" font-size:xx-large; font-weight:600;\">KVK Video Scheduler</span></p><p align=\"center\">Welcome to the KVK Video Scheduler</p><p align=\"center\">by: Kalyan Sriram, Vincent Wang, and Kai Gottschalk</p><p align=\"center\"><br/></p><p align=\"center\">This tutorial will assist you in getting this program up and running for the first time.</p></body></html>"))
        self.wizardPage2.setTitle(_translate("Wizard", "Setup and Prerequisites"))
        self.label_2.setText(_translate("Wizard", "<html><head/><body><p>Open up a terminal of your choice, or click the button below to open the default terminal. Once there, type:</p><p>On Linux: </p><p><code>sudo -H pip3 install -r requirements.txt</code></p><p>Note: You may need to enter your password for your computer.</p><p>MacOS:</p><p>&lt;todo&gt;</p><p>Windows:</p><p><code>py -m pip install -r requirements.txt</code></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wizard = QtWidgets.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())


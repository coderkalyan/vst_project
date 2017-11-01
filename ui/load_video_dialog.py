# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/load_video_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 277)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(423, 277))
        Dialog.setMaximumSize(QtCore.QSize(423, 277))
        Dialog.setSizeGripEnabled(False)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label_load_video_name = QtWidgets.QLabel(Dialog)
        self.label_load_video_name.setObjectName("label_load_video_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_load_video_name)
        spacerItem = QtWidgets.QSpacerItem(249, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_length = QtWidgets.QLabel(Dialog)
        self.label_length.setObjectName("label_length")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_length)
        self.label_absolute = QtWidgets.QLabel(Dialog)
        self.label_absolute.setScaledContents(False)
        self.label_absolute.setObjectName("label_absolute")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_absolute)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hours = QtWidgets.QSpinBox(Dialog)
        self.hours.setEnabled(True)
        self.hours.setMaximum(23)
        self.hours.setObjectName("hours")
        self.horizontalLayout.addWidget(self.hours)
        self.seconds = QtWidgets.QSpinBox(Dialog)
        self.seconds.setEnabled(True)
        self.seconds.setMaximum(59)
        self.seconds.setObjectName("seconds")
        self.horizontalLayout.addWidget(self.seconds)
        self.minutes = QtWidgets.QSpinBox(Dialog)
        self.minutes.setEnabled(True)
        self.minutes.setMaximum(59)
        self.minutes.setObjectName("minutes")
        self.horizontalLayout.addWidget(self.minutes)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.manualPlay = QtWidgets.QCheckBox(Dialog)
        self.manualPlay.setChecked(False)
        self.manualPlay.setTristate(False)
        self.manualPlay.setObjectName("manualPlay")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.manualPlay)
        self.loop = QtWidgets.QCheckBox(Dialog)
        self.loop.setChecked(False)
        self.loop.setObjectName("loop")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.loop)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.button_choose_video = QtWidgets.QPushButton(Dialog)
        self.button_choose_video.setObjectName("button_choose_video")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.button_choose_video)
        self.label_load_video_length = QtWidgets.QLabel(Dialog)
        self.label_load_video_length.setObjectName("label_load_video_length")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_load_video_length)
        self.label_relative = QtWidgets.QLabel(Dialog)
        self.label_relative.setObjectName("label_relative")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_relative)
        self.relative_spinBox = QtWidgets.QSpinBox(Dialog)
        self.relative_spinBox.setMaximum(6000)
        self.relative_spinBox.setSingleStep(60)
        self.relative_spinBox.setObjectName("relative_spinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.relative_spinBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.manualPlay.toggled['bool'].connect(self.hours.setDisabled)
        self.manualPlay.toggled['bool'].connect(self.seconds.setDisabled)
        self.manualPlay.toggled['bool'].connect(self.minutes.setDisabled)
        self.manualPlay.toggled['bool'].connect(self.relative_spinBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Load Video"))
        self.label_load_video_name.setText(_translate("Dialog", "<FileName>"))
        self.label_length.setText(_translate("Dialog", "Length:"))
        self.label_absolute.setToolTip(_translate("Dialog", "<html><head/><body><p>The absolute time the video starts (ex: 8:31:00) in note format (HH:MM:SS)</p></body></html>"))
        self.label_absolute.setText(_translate("Dialog", "Start Time (absolute):"))
        self.hours.setSuffix(_translate("Dialog", "h"))
        self.seconds.setSuffix(_translate("Dialog", "m"))
        self.minutes.setSuffix(_translate("Dialog", "s"))
        self.label_4.setText(_translate("Dialog", "Flags:"))
        self.manualPlay.setText(_translate("Dialog", "Play Manually"))
        self.loop.setText(_translate("Dialog", "Loop"))
        self.button_choose_video.setText(_translate("Dialog", "Change Video"))
        self.label_load_video_length.setText(_translate("Dialog", "<Length>"))
        self.label_relative.setToolTip(_translate("Dialog", "<html><head/><body><p>The delay between the END of the last video and the START of this one in seconds.</p></body></html>"))
        self.label_relative.setText(_translate("Dialog", "Start Time(relative):"))
        self.relative_spinBox.setToolTip(_translate("Dialog", "The delay between the END of the last video and the START of this one."))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Warning.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Warning(object):
    def setupUi(self, Warning):
        Warning.setObjectName("Warning")
        Warning.resize(420, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Warning.sizePolicy().hasHeightForWidth())
        Warning.setSizePolicy(sizePolicy)
        Warning.setMinimumSize(QtCore.QSize(420, 200))
        Warning.setMaximumSize(QtCore.QSize(420, 200))
        self.buttonBox = QtWidgets.QDialogButtonBox(Warning)
        self.buttonBox.setGeometry(QtCore.QRect(110, 140, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label_no = QtWidgets.QLabel(Warning)
        self.label_no.setGeometry(QtCore.QRect(20, 20, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setKerning(True)
        self.label_no.setFont(font)
        self.label_no.setMouseTracking(True)
        self.label_no.setTextFormat(QtCore.Qt.RichText)
        self.label_no.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_no.setWordWrap(True)
        self.label_no.setObjectName("label_no")
        self.label_0 = QtWidgets.QLabel(Warning)
        self.label_0.setEnabled(True)
        self.label_0.setGeometry(QtCore.QRect(50, 80, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_0.setFont(font)
        self.label_0.setText("")
        self.label_0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_0.setWordWrap(True)
        self.label_0.setObjectName("label_0")
        self.checkBox_0 = QtWidgets.QCheckBox(Warning)
        self.checkBox_0.setEnabled(True)
        self.checkBox_0.setGeometry(QtCore.QRect(20, 80, 16, 20))
        self.checkBox_0.setMouseTracking(False)
        self.checkBox_0.setText("")
        self.checkBox_0.setCheckable(False)
        self.checkBox_0.setChecked(False)
        self.checkBox_0.setAutoRepeat(False)
        self.checkBox_0.setAutoExclusive(False)
        self.checkBox_0.setTristate(False)
        self.checkBox_0.setObjectName("checkBox_0")

        self.retranslateUi(Warning)
        self.buttonBox.accepted.connect(Warning.accept) # type: ignore
        self.buttonBox.rejected.connect(Warning.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Warning)

    def retranslateUi(self, Warning):
        _translate = QtCore.QCoreApplication.translate
        Warning.setWindowTitle(_translate("Warning", "Предупреждение"))
        self.label_no.setText(_translate("Warning", "<html><head/><body><p><span style=\" font-weight:600;\">Введено избыточное количество данных.</span></p><p>Значение величины будет пересчитано:</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Warning = QtWidgets.QDialog()
    ui = Ui_Warning()
    ui.setupUi(Warning)
    Warning.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exit.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exit(object):
    def setupUi(self, Exit):
        Exit.setObjectName("Exit")
        Exit.resize(420, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Exit.sizePolicy().hasHeightForWidth())
        Exit.setSizePolicy(sizePolicy)
        Exit.setMinimumSize(QtCore.QSize(420, 170))
        Exit.setMaximumSize(QtCore.QSize(420, 170))
        self.buttonBox = QtWidgets.QDialogButtonBox(Exit)
        self.buttonBox.setGeometry(QtCore.QRect(110, 110, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label_no = QtWidgets.QLabel(Exit)
        self.label_no.setGeometry(QtCore.QRect(20, 20, 371, 61))
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

        self.retranslateUi(Exit)
        self.buttonBox.accepted.connect(Exit.accept) # type: ignore
        self.buttonBox.rejected.connect(Exit.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Exit)

    def retranslateUi(self, Exit):
        _translate = QtCore.QCoreApplication.translate
        Exit.setWindowTitle(_translate("Exit", "Выход"))
        self.label_no.setText(_translate("Exit", "<html><head/><body><p><span style=\" font-weight:600;\">Уверены, что хотите выйти?</span></p><p>Все несохраненные данные будут потеряны.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Exit = QtWidgets.QDialog()
    ui = Ui_Exit()
    ui.setupUi(Exit)
    Exit.show()
    sys.exit(app.exec_())
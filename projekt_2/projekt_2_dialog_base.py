# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projekt_2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WtyczkaProjektDialogBase(object):
    def setupUi(self, WtyczkaProjektDialogBase):
        WtyczkaProjektDialogBase.setObjectName("WtyczkaProjektDialogBase")
        WtyczkaProjektDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(WtyczkaProjektDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")

        self.retranslateUi(WtyczkaProjektDialogBase)
        self.button_box.accepted.connect(WtyczkaProjektDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(WtyczkaProjektDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WtyczkaProjektDialogBase)

    def retranslateUi(self, WtyczkaProjektDialogBase):
        _translate = QtCore.QCoreApplication.translate
        WtyczkaProjektDialogBase.setWindowTitle(_translate("WtyczkaProjektDialogBase", "Projekt 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WtyczkaProjektDialogBase = QtWidgets.QDialog()
    ui = Ui_WtyczkaProjektDialogBase()
    ui.setupUi(WtyczkaProjektDialogBase)
    WtyczkaProjektDialogBase.show()
    sys.exit(app.exec_())
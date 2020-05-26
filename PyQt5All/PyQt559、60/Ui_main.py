# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5\PyQt559\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 577)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(11, 11, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.formLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_username)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pwd)
        self.pb_submit = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pb_submit.setObjectName("pb_submit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pb_submit)
        self.pb_reset = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pb_reset.setObjectName("pb_reset")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pb_reset)
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学点编程吧：PyQt5与Web页面交互2"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_2.setText(_translate("Form", "密  码："))
        self.pb_submit.setText(_translate("Form", "传值给Web页面"))
        self.pb_reset.setText(_translate("Form", "重置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


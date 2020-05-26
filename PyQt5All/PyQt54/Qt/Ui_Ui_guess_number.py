# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yangff\Desktop\PyQt5\4\qt\Ui_guess_number.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(289, 202)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("xdbcb8.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.pushButton.setStatusTip("")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 50, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFocus()
        self.lineEdit.selectAll()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学点编程吧--猜数字游戏"))
        self.pushButton.setToolTip(_translate("MainWindow", "<b>点击这里猜数字</b>"))
        self.pushButton.setText(_translate("MainWindow", "我猜"))
        self.lineEdit.setText(_translate("MainWindow", "在这里输入数字"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5\PyQt561\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(60, 20, 661, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_F = QtWidgets.QMenu(self.menuBar)
        self.menu_F.setObjectName("menu_F")
        self.menu_G = QtWidgets.QMenu(self.menuBar)
        self.menu_G.setObjectName("menu_G")
        self.menu_A = QtWidgets.QMenu(self.menuBar)
        self.menu_A.setObjectName("menu_A")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_O = QtWidgets.QAction(MainWindow)
        self.action_O.setObjectName("action_O")
        self.action_E = QtWidgets.QAction(MainWindow)
        self.action_E.setObjectName("action_E")
        self.action_R = QtWidgets.QAction(MainWindow)
        self.action_R.setObjectName("action_R")
        self.action_S = QtWidgets.QAction(MainWindow)
        self.action_S.setObjectName("action_S")
        self.action_P = QtWidgets.QAction(MainWindow)
        self.action_P.setObjectName("action_P")
        self.action_J = QtWidgets.QAction(MainWindow)
        self.action_J.setObjectName("action_J")
        self.menu_F.addAction(self.action_O)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.action_E)
        self.menu_G.addAction(self.action_R)
        self.menu_G.addSeparator()
        self.menu_G.addAction(self.action_P)
        self.menu_A.addAction(self.action_J)
        self.menuBar.addAction(self.menu_F.menuAction())
        self.menuBar.addAction(self.menu_G.menuAction())
        self.menuBar.addAction(self.menu_A.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学点编程吧--拼图小游戏"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_G.setTitle(_translate("MainWindow", "游戏(&G)"))
        self.menu_A.setTitle(_translate("MainWindow", "关于(&A)"))
        self.action_O.setText(_translate("MainWindow", "打开图片(&O)"))
        self.action_O.setStatusTip(_translate("MainWindow", "打开图片"))
        self.action_E.setText(_translate("MainWindow", "退出游戏(&E)"))
        self.action_E.setStatusTip(_translate("MainWindow", "退出游戏"))
        self.action_R.setText(_translate("MainWindow", "重新开始(&R)"))
        self.action_R.setStatusTip(_translate("MainWindow", "重新开始游戏"))
        self.action_S.setText(_translate("MainWindow", "难度选择(&S)"))
        self.action_P.setText(_translate("MainWindow", "显示还原后的图片(&P)"))
        self.action_J.setText(_translate("MainWindow", "关于拼图小游戏(J)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


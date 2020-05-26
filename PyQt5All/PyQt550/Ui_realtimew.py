# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5\PyQt550\realtimew.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RealTime(object):
    def setupUi(self, RealTime):
        RealTime.setObjectName("RealTime")
        RealTime.resize(400, 255)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RealTime)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(RealTime)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_tt = QtWidgets.QLabel(RealTime)
        self.label_tt.setObjectName("label_tt")
        self.horizontalLayout.addWidget(self.label_tt)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(RealTime)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_ww = QtWidgets.QLabel(RealTime)
        self.label_ww.setObjectName("label_ww")
        self.horizontalLayout_2.addWidget(self.label_ww)
        self.label_icon = QtWidgets.QLabel(RealTime)
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap("res/99.png"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout_2.addWidget(self.label_icon)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RealTime)
        QtCore.QMetaObject.connectSlotsByName(RealTime)

    def retranslateUi(self, RealTime):
        _translate = QtCore.QCoreApplication.translate
        RealTime.setWindowTitle(_translate("RealTime", "Form"))
        self.label.setText(_translate("RealTime", "温度："))
        self.label_tt.setText(_translate("RealTime", "30"))
        self.label_2.setText(_translate("RealTime", "天气："))
        self.label_ww.setText(_translate("RealTime", "多云"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RealTime = QtWidgets.QWidget()
    ui = Ui_RealTime()
    ui.setupUi(RealTime)
    RealTime.show()
    sys.exit(app.exec_())


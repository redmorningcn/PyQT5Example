# -*- coding: utf-8 -*-

"""
一个关于火影忍者之写轮眼、轮回眼（QDockWidget的使用）的小例子！
文章链接：http://www.xdbcb8.com/archives/848.html
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget
from PyQt5.QtCore import QEvent
from Ui_main import Ui_MainWindow

class Naruto(QMainWindow, Ui_MainWindow):
    """
    一些初始设置
    """
    def __init__(self, parent=None):
        """
        界面初始设置
        """
        super(Naruto, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.dockWidget.setFeatures(QDockWidget.DockWidgetMovable)
        # 允许用户在dock之间移动

        # self.dockWidget.setFloating(True)
        # 需要QDockWidget就是浮动的，而不是我们把它拉出来，可以如上设置

        self.dockWidget.setWindowTitle("写轮眼")
        self.dockWidget_2.setWindowTitle("轮回眼")
        self.label_zhuozhu2.installEventFilter(self)
    
    def eventFilter(self, object, event):
        '''
        事件过滤器，双击佐助轮回眼让其显现出来。
        '''
        if object == self.label_zhuozhu2:
            if event.type() == QEvent.MouseButtonDblClick:
                self.dockWidget_2.show()
        return QMainWindow.eventFilter(self, object, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Naruto()
    ex.show()
    sys.exit(app.exec_())
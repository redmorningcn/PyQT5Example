# -*- coding: utf-8 -*-

"""
一个关于QStackedWidget使用的小例子！
文章链接：http://www.xdbcb8.com/archives/848.html
"""

import sys
from PyQt5.QtWidgets import QDockWidget, QPushButton, QApplication, QMainWindow, QHBoxLayout, QTextEdit
from PyQt5.QtCore import Qt

class Dock(QMainWindow):
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        hlayout = QHBoxLayout()
        self.dock = QDockWidget("我是一个按钮", self)
        # 使用QDockWidget首先要新建一个QDockWidget对象。

        self.bt = QPushButton("点我")
        self.dock.setWidget(self.bt)
        # 新建一个按钮放在QDockWidget对象上。

        self.tt = QTextEdit()
        self.setCentralWidget(self.tt)
        # 新建一个QTextEdit小部件设置为主窗口的中央小部件。

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        # 将给定的dockwidget添加到指定的区域，这里是中间，对象是self.dock

        self.setLayout(hlayout)
        self.setWindowTitle("学点编程吧：代码如何使用QDockWidget")
        self.bt.clicked.connect(self.game)
    
    def game(self):
        '''
        点击按钮触发
        '''
        self.tt.append("你点我啦！")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dock = Dock()
    dock.show()
    sys.exit(app.exec_())
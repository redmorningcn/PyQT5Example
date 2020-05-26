#coding=utf-8

'''
这是一个关于标签（QLabel）的小例子-简单例子！
文章链接：http://www.xdbcb8.com/archives/460.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFrame
from PyQt5.QtCore import Qt

class Example(QWidget):
    '''
    QLabel简单例子
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        界面初始设置
        '''
        self.resize(400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧')

        label = QLabel(self)
        label.resize(200, 100)
        label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        # 将框架样式设置为样式。QFrame绘制一个面板，使内容显得凸起或凹陷；使用当前颜色组的浅色和深色绘制3D凹陷线。

        label.setText("first line\nsecond line")
        label.setAlignment(Qt.AlignBottom | Qt.AlignRight)# 设置为右下方位置
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
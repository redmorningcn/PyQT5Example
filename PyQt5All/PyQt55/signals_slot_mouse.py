#coding=utf-8

'''
这是一个我们移动鼠标并进行响应的小例子，在这个例子中我们实现了鼠标坐标（x,y）的获取，以及绘制一条线。
文章链接：http://www.xdbcb8.com/archives/190.html
'''

import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter

class Example(QWidget):

    '''
    移动鼠标得到响应
    '''

    distance_from_center = 0#到中心点的距离

    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        #启用鼠标追踪，即使没有按钮被按下，小部件也会接收鼠标移动事件。

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('学点编程吧')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None
        #鼠标的坐标

    def mouseMoveEvent(self, event):
        '''
        鼠标移动时我们做出的反映
        '''
        distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)#距离中心点的距离
        self.label.setText('坐标: ( x: %d ,y: %d )' % (event.x(), event.y()) + " 离中心点距离: " + str(distance_from_center))       
        self.pos = event.pos()
        self.update()#必须调用函数update()才能更新图形。你可以尝试注释这句话，看看效果。

    def paintEvent(self, event):
        '''
        绘制一条线drawLine()，线的坐标是根据鼠标移动的坐标定的。
        '''
        if self.pos:
            q = QPainter(self)
            q.drawLine(50, 50, self.pos.x(), self.pos.y())

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
#coding=utf-8

'''
这是关于滑块的小例子！
文章链接：http://www.xdbcb8.com/archives/366.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    '''
    单选框
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
        self.resize(750, 450)
        self.setWindowTitle('关注微信公众号：学点编程吧--小车快跑（滑动块）')

        self.sld1 = QSlider(Qt.Vertical, self)
        self.sld1.setGeometry(30, 40, 30, 100)
        self.sld1.setMinimum(0)
        self.sld1.setMaximum(99)
        self.sld1.setTickPosition(QSlider.TicksLeft)#给滑块1设定了一个标记位置
        
        self.sld2 = QSlider(Qt.Horizontal, self)
        self.sld2.setGeometry(500, 350, 100, 30)
        self.sld2.setMinimum(0)
        self.sld2.setMaximum(99)
        
        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap('01.jpg'))
        self.label1.setGeometry(80, 150, 600, 180)
        
        self.label2 = QLabel('滑动块1当前值: 0 ', self)
        self.label2.move(70, 70)
        
        self.label3 = QLabel('滑动块2当前值: 0 ', self)
        self.label3.move(550, 390)

        self.sld1.valueChanged[int].connect(self.changevalue)
        self.sld2.valueChanged[int].connect(self.changevalue)
        
        self.show()

    def changevalue(self, value):
        '''
        滑块联动
        '''
        sender = self.sender()
        if sender == self.sld1:
            self.sld2.setValue(value)
        else:
            self.sld1.setValue(value)
        #滑块联动，数值同时变化

        self.label2.setText('滑动块1当前值:' + str(value))
        self.label3.setText('滑动块2当前值:' + str(value))

        if value == 0:
            self.label1.setPixmap(QPixmap('01.jpg'))
        elif value > 0 and value <= 30:
            self.label1.setPixmap(QPixmap('02.jpg'))
        elif value > 30 and value < 80:
            self.label1.setPixmap(QPixmap('03.jpg'))
        else:
            self.label1.setPixmap(QPixmap('04.jpg'))
        #滑块数值不同时加载不同的小车图片
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#coding=utf-8

'''
这是一个关于标签（QLabel）的小例子-图片显示！
文章链接：http://www.xdbcb8.com/archives/460.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    '''
    图片显示
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
        self.resize(550, 500)
        self.setWindowTitle('关注微信公众号：学点编程吧--标签:图画（QLabel）')
        
        pix = QPixmap('sexy.jpg')
        
        lb1 = QLabel(self)
        lb1.setGeometry(0, 0, 300, 200)
        lb1.setStyleSheet("border: 2px solid red")# 给图片加一个红色边框
        lb1.setPixmap(pix)# 加载图片
        
        lb2 = QLabel(self)
        lb2.setGeometry(0, 250, 300, 200)
        lb2.setPixmap(pix)
        lb2.setStyleSheet("border: 2px solid red")
        lb2.setScaledContents(True)# 缩放其内容以填充所有可用空间
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
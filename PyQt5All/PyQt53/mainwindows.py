#coding=utf-8

'''
使用PyQt5实现一个最简单的图形界面程序
文章链接：http://www.xdbcb8.com/archives/137.html
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#QWidget小部件是PyQt5中所有用户界面对象的基类。
from PyQt5.QtGui import QIcon
#从PyQt5.QtGui中引入QIcon这个类，也是为了便于图标的设定。
from PyQt5.QtCore import QCoreApplication

class Ico(QWidget):

    '''
    最简单的图形界面程序
    '''

    def __init__(self):
        super().__init__()
        self.initUI()    

    def initUI(self):
        '''
        设置一个窗口和一个按钮
        '''
        self.setGeometry(300, 300, 300, 220)
        #在屏幕上定位窗口并设置它的大小
        self.setWindowTitle('微信公众号：学点编程吧出品')
        #设置窗口标题
        self.setWindowIcon(QIcon('xdbcb8.ico'))
        #设置窗口图标

        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        #请注意，QCoreApplication是通过QApplication创建的。 点击的信号连接到终止应用程序的quit()方法。
        qbtn.resize(70, 30)
        qbtn.move(50, 50)

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())
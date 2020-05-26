#coding=utf-8

'''
这是一个我们点击鼠标后发出信号并进行响应的小例子
文章链接：http://www.xdbcb8.com/archives/190.html
'''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtCore import (pyqtSignal, QObject)

class Signal(QObject):
    
    '''
    自定义信号
    '''

    showmouse = pyqtSignal()
    #这里我们自定义一个信号showmouse

class Example(QWidget):

    '''
    点击鼠标后得到响应
    '''

    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')
        
        self.s = Signal()#这里我们实例化了自定义信号，但是并没法发出信号
        self.s.showmouse.connect(self.about)#自定义信号发出后我们会连接到槽函数about()

        self.show()
        
    def about(self):
        '''
        弹出信息
        '''
        QMessageBox.about(self, '鼠标', '你点鼠标了吧！')
        
    def mousePressEvent(self, e):
        '''
        鼠标点击事件
        '''
        self.s.showmouse.emit()#当我们点击鼠标按键的时候，这个showmouse信号会发生出去

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
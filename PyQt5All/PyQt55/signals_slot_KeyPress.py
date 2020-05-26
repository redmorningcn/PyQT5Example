#coding=utf-8

'''
这是一个我们点击键盘并进行响应的小例子
文章链接：http://www.xdbcb8.com/archives/190.html
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel)

class Example(QWidget):

    '''
    点击键盘响应
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUi()
    
    def initUi(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')
        
        self.lab = QLabel('方向', self)
        
        self.lab.setGeometry(150, 100, 50, 50)
        
        self.show()
        
    def keyPressEvent(self, e):
        '''
        这个函数用于处理键盘上不同按键所产生的Qt事件，这里只是列举了部分。
        关注微信公众号：学点编程吧，发送pyqt55d可以获得全部Qt按键代号。
        '''
        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
            #向上键
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
            #向下键
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
            #向左键
        else:
            self.lab.setText('→')
            #向右键
            
        #当我们点击方向键时，不同的方向键对应了不同的箭头方向

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#coding = 'utf-8'

'''
这是一个箱式布局的小例子！
文章链接：http://www.xdbcb8.com/archives/209.html
'''

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout)

class Example(QWidget):
    '''
    箱式布局
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        '''
        界面初始设置
        '''
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('学点编程吧')
        
        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)#水平方向增加一个伸缩量
        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(bt3)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)#垂直方向增加一个伸缩量
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
#coding = 'utf-8'

'''
这是一个关于伸缩量的小例子！
文章链接：http://www.xdbcb8.com/archives/209.html
'''

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout)

class Example(QWidget):

    '''
    伸缩量的使用
    '''
    
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        '''
        一些界面设置
        '''
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('学点编程吧')
        
        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1) #增加1个伸缩量
        hbox.addWidget(bt1)
        hbox.addStretch(1)#增加1个伸缩量
        hbox.addWidget(bt2)
        hbox.addStretch(1)#增加1个伸缩量
        hbox.addWidget(bt3)
        hbox.addStretch(6)#增加6个伸缩量

        self.setLayout(hbox)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
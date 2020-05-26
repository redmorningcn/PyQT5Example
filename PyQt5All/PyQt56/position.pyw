#coding = 'utf-8'

'''
这是一个绝对布局的小例子！
文章链接：http://www.xdbcb8.com/archives/209.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):
    '''
    绝对布局
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
        bt1.move(50, 250)

        bt2 = QPushButton('石头', self)
        bt2.move(150, 250)
        
        bt3 = QPushButton('布', self)
        bt3.move(250, 250)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
    
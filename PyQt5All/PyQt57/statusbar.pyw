#coding=utf-8

'''
这是一个关于界面搭建的小例子，显示状态栏信息！
文章链接：http://www.xdbcb8.com/archives/227.html
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Example(QMainWindow):
    '''
    状态栏信息
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.InitUI()
        
    def InitUI(self):
        '''
        界面初始设置
        '''
        self.statusBar().showMessage('准备就绪')
        #状态栏显示信息
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--状态栏')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
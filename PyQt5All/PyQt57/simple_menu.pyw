#coding=utf-8

'''
这是一个关于界面搭建的小例子，实现退出菜单！
文章链接：http://www.xdbcb8.com/archives/227.html
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    '''
    退出菜单
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
        
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--简单的菜单')
        
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)
        #退出菜单
        #qApp一个引用唯一应用程序对象的全局指针。 它等同于QCoreApplication.instance()
        #仅在唯一应用程序对象是QApplication时才有效。
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')#这里的快捷键F
        fileMenu.addAction(exitAct)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
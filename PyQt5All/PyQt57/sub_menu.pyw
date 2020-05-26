#coding=utf-8

'''
这是一个关于界面搭建的小例子，实现了子菜单！
文章链接：http://www.xdbcb8.com/archives/227.html
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    '''
    子菜单
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
        self.setWindowTitle('关注微信公众号：学点编程吧--子菜单')
        
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)
        # 退出

        saveMenu = QMenu('保存方式(&S)', self)

        saveAct = QAction(QIcon('save.png'), '保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        #子菜单：保存

        saveasAct = QAction(QIcon('saveas.png'), '另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        #子菜单：另存为

        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)
        #增加子菜单

        newAct = QAction(QIcon('new.png'), '新建(&N)', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        #增加分隔线

        fileMenu.addAction(exitAct)
        
        self.show()      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
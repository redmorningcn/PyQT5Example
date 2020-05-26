#coding=utf-8

'''
这是一个关于界面搭建的小例子，实现了上下文菜单！
文章链接：http://www.xdbcb8.com/archives/227.html
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    '''
    上下文菜单
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
        self.setWindowTitle('关注微信公众号：学点编程吧--上下文菜单')
        
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)#退出操作
        exitAct.setShortcut('Ctrl+Q')#快捷键
        exitAct.setStatusTip('退出程序')#状态提示
        exitAct.triggered.connect(qApp.quit)#点击时连接到的槽函数
        #退出菜单

        saveMenu = QMenu('保存方式(&S)', self)
        # 菜单

        saveAct = QAction(QIcon('save.png'), '保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction(QIcon('saveas.png'), '另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)
        #保存方式菜单
        
        newAct = QAction(QIcon('new.png'), '新建(&N)', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')
        #新建文件菜单
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)
        
        self.show()
        
    def contextMenuEvent(self, event):
        '''
        设定上下文菜单（右键菜单）
        '''
        cmenu = QMenu(self)
       
        newAct = cmenu.addAction("新建")
        opnAct = cmenu.addAction("保存")
        quitAct = cmenu.addAction("退出")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        #使用exec_()方法显示上下文菜单。 从事件对象获取鼠标指针的坐标。 mapToGlobal()方法将窗口小部件坐标转换为全局屏幕坐标。
        
        if action == quitAct:
            qApp.quit()
        #如果从上下文菜单返回的操作等于退出操作，我们终止应用程序。        
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
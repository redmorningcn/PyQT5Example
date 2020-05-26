#coding=utf-8

'''
这是一个关于按钮（QPushButton）的小例子！
文章链接：http://www.xdbcb8.com/archives/484.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMenu
from PyQt5.QtCore import QTimer

class Example(QWidget):
    '''
    按钮的使用
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        界面初始设置
        '''
        self.resize(400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--按钮（QPushButton）')

        bt1 = QPushButton("这是什么", self)
        bt1.move(50, 50)
        
        self.bt2 = QPushButton('发送验证码', self)
        self.bt2.move(200, 50)
        
        menu = QMenu(self)
        menu.addAction('我是')
        menu.addSeparator()# 给菜单增加一个分隔符
        menu.addAction('世界上')
        menu.addSeparator()
        menu.addAction('最帅的')# 增加一个菜单操作
        
        bt1.setMenu(menu)# 给按钮增加一个菜单
        
        self.count = 10# 倒计时10s
        
        self.bt2.clicked.connect(self.Action)
        
        self.time = QTimer(self)
        self.time.setInterval(1000)# 1s后超时
        self.time.timeout.connect(self.Refresh)
        
        self.show()
        
    def Action(self):
        '''
        当bt2状态是启用的我们开始计时
        '''
        if self.bt2.isEnabled():
            self.time.start()# 开始计时
            self.bt2.setEnabled(False)# bt2按钮禁用

    def Refresh(self):
        '''
        倒计时刷新
        '''
        if self.count > 0:
            self.bt2.setText(str(self.count) + '秒后重发')# 显示还有n秒后重发
            self.count -= 1
        else:
            self.time.stop()# 定时器停止
            self.bt2.setEnabled(True)# bt2按钮启用
            self.bt2.setText('发送验证码')
            self.count = 10
            # 倒计时时间重置为10s

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
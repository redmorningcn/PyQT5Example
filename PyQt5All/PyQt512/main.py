#coding=utf-8

'''
这是构建我们自己的密码输入框中的例子
文章链接：http://www.xdbcb8.com/archives/343.html
'''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser, QLineEdit)
from PasswdDialog import PasswdDialog

class Example(QWidget):
    '''
    DIY密码输入框
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
        self.resize(380, 180)
        self.setWindowTitle('微信公众号：学点编程吧--自定义密码输入对话框')
        
        self.lb1 = QLabel('密码在此显示...', self)
        self.lb1.move(20, 20)
        
        self.bt1 = QPushButton('输入密码(普通型)', self)
        self.bt1.move(20, 60)
        
        self.bt2 = QPushButton('输入密码(普通加强型)', self)
        self.bt2.move(20, 100)
        
        self.bt3 = QPushButton('输入密码(特别加强型)', self)
        self.bt3.move(20, 140)

        self.show()
          
        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        self.bt3.clicked.connect(self.showDialog)
        
    def showDialog(self):
        '''
        当我们输入密码的时候，会有不同的显示
        '''
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '密码输入框', '请输入密码：', QLineEdit.Password)#加密显示
            if ok:
                self.lb1.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '密码输入框', '请输入密码：', QLineEdit.PasswordEchoOnEdit)#输入后加密显示
            if ok:
                self.lb1.setText(text)
        else:
            pwd = PasswdDialog()#DIY密码输入框
            r = pwd.exec_()#执行密码输入框
            if r:
                self.lb1.setText(pwd.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
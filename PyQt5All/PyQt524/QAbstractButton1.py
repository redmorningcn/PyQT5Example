#coding=utf-8

'''
这是一个关于抽象按钮（QAbstractButton）的小例子--芝麻开门单个密码！
文章链接：http://www.xdbcb8.com/archives/506.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMessageBox

class Example(QWidget):
    '''
    芝麻开门单个密码
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
        self.resize(500, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--抽象按钮的学习1（QAbstractButton）')

        label1 = QLabel('密码输入区', self)
        label1.move(50, 50)
        
        label2 = QLabel('正确密码：麻', self)
        label2.move(50, 200)
        
        label3 = QLabel('你输入的密码：', self)
        label3.move(50, 250)
        
        self.label4 = QLabel('  ', self)
        self.label4.move(150, 250)
        
        bt1 = QPushButton('芝', self)
        bt2 = QPushButton('麻', self)
        bt3 = QPushButton('开', self)
        bt4 = QPushButton('门', self)
        
        bt1.setGeometry(150, 50, 40, 40)
        bt3.setGeometry(200, 50, 40, 40)
        bt2.setGeometry(150, 100, 40, 40)
        bt4.setGeometry(200, 100, 40, 40)
        
        bt1.setCheckable(True)#按钮按下后就不弹起来了
        bt2.setCheckable(True)
        bt3.setCheckable(True)
        bt4.setCheckable(True)
        
        bt1.setAutoExclusive(True)#启用自动排它性，每次只能一个被选中。
        bt2.setAutoExclusive(True)
        bt3.setAutoExclusive(True)
        bt4.setAutoExclusive(True)
        
        self.show()
        
        bt1.clicked.connect(self.setPassword)
        bt2.clicked.connect(self.setPassword)
        bt3.clicked.connect(self.setPassword)
        bt4.clicked.connect(self.setPassword)

    def setPassword(self):
        '''
        检测密码是否正确
        '''
        word = self.sender().text()
        self.label4.setText(word)
        if word == '麻':
            QMessageBox.information(self, '提示', '恭喜，密码正确，可以进入！')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
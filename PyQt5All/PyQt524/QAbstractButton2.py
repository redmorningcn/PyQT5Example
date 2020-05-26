#coding=utf-8

'''
这是一个关于抽象按钮（QAbstractButton）的小例子--芝麻开门多个密码结合！
文章链接：http://www.xdbcb8.com/archives/506.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMessageBox

class Example(QWidget):
    '''
    芝麻开门多个密码结合
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
        self.setWindowTitle('关注微信公众号：学点编程吧--抽象按钮的学习2（QAbstractButton）')

        label1 = QLabel('密码输入区', self)
        label1.move(50, 50)
        
        label2 = QLabel('正确密码：芝麻开门', self)
        label2.move(50, 200)
        
        label3 = QLabel('你输入的密码：', self)
        label3.move(50, 250)
        
        self.label4 = QLabel('        ', self)
        self.label4.move(150, 250)
        
        self.bt1 = QPushButton('芝', self)
        self.bt2 = QPushButton('麻', self)
        self.bt3 = QPushButton('开', self)
        self.bt4 = QPushButton('门', self)
        
        self.bt1.setGeometry(150, 50, 40, 40)
        self.bt3.setGeometry(200, 50, 40, 40)
        self.bt2.setGeometry(150, 100, 40, 40)
        self.bt4.setGeometry(200, 100, 40, 40)
        
        self.bt1.setCheckable(True)#按钮按下后就不弹起来了
        self.bt2.setCheckable(True)
        self.bt3.setCheckable(True)
        self.bt4.setCheckable(True)

        self.show()

        self.password = ''

        self.bt1.clicked.connect(self.setPassword)
        self.bt2.clicked.connect(self.setPassword)
        self.bt3.clicked.connect(self.setPassword)
        self.bt4.clicked.connect(self.setPassword)

    def setPassword(self, pressed):
        '''
        看看我们点击的密码正确吗？
        '''
        word = self.sender().text()
        if pressed:
            if len(self.password) < 4:
                #密码长度是有限制的哦
                self.password += word
                #根据点击的先后次序生产输入的密码啊
        else:
            self.password = self.password.replace(word, '')
            #要是按钮没有选中，这个按钮代表的密码就是消失
            
        self.label4.setText(self.password)

        if len(self.password) == 4 and self.password == '芝麻开门':
            QMessageBox.information(self, '提示', '恭喜，密码正确，可以进入！')
            #要是密码符合我们的要求，“恭喜，密码正确”
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
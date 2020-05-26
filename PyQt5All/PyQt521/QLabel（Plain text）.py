#coding=utf-8

'''
这是一个关于标签（QLabel）的小例子-纯文本例子！
文章链接：http://www.xdbcb8.com/archives/460.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QRadioButton, QButtonGroup, QInputDialog, QPushButton
from PyQt5.QtCore import Qt

class Example(QWidget):
    '''
    纯文本例子
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
        self.resize(550, 320)
        self.setWindowTitle('关注微信公众号：学点编程吧--标签:纯文本（QLabel）')

        self.lb1 = QLabel('学点编程吧，我爱你~！', self)
        self.lb1.setGeometry(0, 0, 550, 50)
        
        self.lb2 = QLabel('我内容很少哦...', self)
        self.lb2.setGeometry(0, 100, 120, 70)
        
        self.lb3 = QLabel('我内容很少哦...', self)
        self.lb3.setGeometry(0, 190, 120, 70)
        self.lb3.setWordWrap(True)
        
        self.bt1 = QPushButton('输入内容1', self)
        self.bt1.move(0, 150)
        
        self.bt2 = QPushButton('输入内容2', self)
        self.bt2.move(0, 280)    
        
        self.ra1 = QRadioButton('左边', self)
        self.ra2 = QRadioButton('中间', self)
        self.ra3 = QRadioButton('右边', self)
        
        self.ra1.move(10, 60)
        self.ra2.move(70, 60)
        self.ra3.move(130, 60)
        
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.ra1, 1)
        self.bg1.addButton(self.ra2, 2)
        self.bg1.addButton(self.ra3, 3)
        #给单选按钮组中的每一个单选按钮增加一个id号

        self.show()
        
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        
    def rbclicked(self):
        '''
        单选按钮组不同单选按钮被选择时，会对QLabel中信息位置进行调整。
        '''
        if self.bg1.checkedId() == 1:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        elif self.bg1.checkedId() == 2:
            self.lb1.setAlignment(Qt.AlignCenter)
        elif self.bg1.checkedId() == 3:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
    
    def showDialog(self):
        '''
        我们输入对话框信息会被显示在QLabel上
        '''
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '内容1', '请输入内容1：')
            if ok:
                self.lb2.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '内容2', '请输入内容2：')
            if ok:
                self.lb3.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
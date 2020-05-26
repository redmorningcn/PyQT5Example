#coding=utf-8

'''
这是关于单选框的小例子！
文章链接：http://www.xdbcb8.com/archives/366.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QRadioButton, QApplication, QPushButton, QMessageBox, QButtonGroup

class Example(QWidget):
    '''
    单选框
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
        self.rb11 = QRadioButton('你是', self)
        self.rb12 = QRadioButton('我是', self)
        self.rb13 = QRadioButton('他是', self)
        self.rb21 = QRadioButton('大美女', self)
        self.rb22 = QRadioButton('大帅哥', self)
        self.rb23 = QRadioButton('小屁孩', self)
        
        bt1 = QPushButton('提交', self)
        
        self.resize(320, 180)
        self.setWindowTitle('关注微信公众号：学点编程吧--单选按钮')
        
        self.rb11.move(20, 20)
        self.rb12.move(20, 50)
        self.rb13.move(20, 80)
        self.rb21.move(90, 20)
        self.rb22.move(90, 50)
        self.rb23.move(90, 80)
        bt1.move(20, 120)
        
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.rb11, 11)
        self.bg1.addButton(self.rb12, 12)
        self.bg1.addButton(self.rb13, 13)
        #单选按钮组1，后面的数字是按钮组id
        
        self.bg2 = QButtonGroup(self)
        self.bg2.addButton(self.rb21, 21)
        self.bg2.addButton(self.rb22, 22)
        self.bg2.addButton(self.rb23, 23)
        #单选按钮组2

        self.info1 = ''
        self.info2 = ''
        # 相关信息
        
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bg2.buttonClicked.connect(self.rbclicked)

        bt1.clicked.connect(self.submit)
        
        self.show()
        
    def submit(self):
        '''
        提交
        '''
        if self.info1 == '' or self.info2 == '':
            QMessageBox.information(self, 'What?', '貌似有没有选的啊，快去选一个吧！')
        else:
            QMessageBox.information(self, 'What?', self.info1 + self.info2)

    def rbclicked(self):
        '''
        将单选组1和单选组2中的各选择一个将值赋给self.info1和self.info2
        '''
        sender = self.sender()
        if sender == self.bg1:
            if self.bg1.checkedId() == 11:
                # 要是按钮组的id为11，下同
                self.info1 = '你是'
            elif self.bg1.checkedId() == 12:
                self.info1 = '我是'
            elif self.bg1.checkedId() == 13:
                self.info1 = '他是'
            else:
                self.info1 = ''
        else:
            if self.bg2.checkedId() == 21:
                self.info2 = '大美女'
            elif self.bg2.checkedId() == 22:
                self.info2 = '大帅哥'
            elif self.bg2.checkedId() == 23:
                self.info2 = '小屁孩'
            else:
                self.info2 = ''
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
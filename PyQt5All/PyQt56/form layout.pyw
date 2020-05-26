#coding = 'utf-8'

'''
这是一个表格布局的小例子！
文章链接：http://www.xdbcb8.com/archives/209.html
'''

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit)

class Example(QWidget):
    '''
    表格布局
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        '''
        界面初始设置
        '''
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('学点编程吧-表单布局')
        
        formlayout = QFormLayout()#创建一个表单布局
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        introductionLabel = QLabel("简介")
        introductionLineEdit = QTextEdit("")
        
        formlayout.addRow(nameLabel, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLineEdit)
        #向表单中增加一行，内容是我们定义的小部件。
        self.setLayout(formlayout)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
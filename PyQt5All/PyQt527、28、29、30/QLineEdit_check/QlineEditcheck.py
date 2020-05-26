#coding=utf-8

"""
这是一个关于文本输入栏（QLineEdit）的小例子--单词拼写检查！
文章链接：http://www.xdbcb8.com/archives/612.html
"""

import sys
from PyQt5.QtWidgets import QLineEdit, QApplication, QDialog, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from checkword import correct

class Line(QDialog):
    '''
    单词拼写检查
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.Ui()
    
    def Ui(self):
        '''
        界面初始设置
        '''
        self.resize(450, 100)
        self.setWindowTitle('微信公众号：学点编程吧--单词拼写检查')
        self.line = QLineEdit(self)
        self.line.move(20, 20)
        action = QAction(self)
        action.setIcon(QIcon('check.ico'))
        action.triggered.connect(self.Check)
        self.line.addAction(action, QLineEdit.TrailingPosition)# 部件显示在文本右侧
        self.show()
    
    def Check(self):
        '''
        检查下你写的是什么单词
        '''
        word = self.line.text()
        if correct(word) != word:
            QMessageBox.information(self, '提示信息', '你或许想要表达的单词是：' + correct(word))
        else:
            QMessageBox.information(self, '提示信息', '你填写的单词是：' + word)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    line = Line()
    sys.exit(app.exec_())
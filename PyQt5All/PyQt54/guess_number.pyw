#coding = utf-8

'''
这是一个猜数字的小游戏，在窗口中输入一个数字，点击我猜，看看你能猜中不！
文章链接：http://www.xdbcb8.com/archives/164.html
'''

import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon

class Example(QWidget):

    '''
    猜数字的小游戏
    '''
    
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)
        #我们随机生成一个数字，范围在1-100之间。
        
    def initUI(self):
        '''
        绘制主要窗口，其中按钮“我猜”设置的提示是加粗的。
        '''
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70 ,30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        #调用setTooltip()方法，可以使用富文本格式。
        self.bt1.clicked.connect(self.showMessage)  

        self.text = QLineEdit('在这里输入数字', self)
        self.text.selectAll()
        #selectAll()方法则是可以理解为将“在这里输入数字”进行全选，方便输入数字，否则你还得手动全选删除默认字符。
        self.text.setFocus()
        #setFocus()就是让焦点置于文本栏中，方便用户输入。
        self.text.setGeometry(80, 50, 150, 30)
        # 输入栏的大小位置信息

        self.show()

    def showMessage(self):
        '''
        提示猜数字结果
        '''
        guessnumber = int(self.text.text())
        if guessnumber > self.num:
            QMessageBox.about(self, '看结果', '猜大了!')
            self.text.setFocus()
            # 焦点集中到输入框
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event):
        '''
        如果关闭QWidget，则生成QCloseEvent。 要修改widget的行为，我们需要重新实现closeEvent()事件处理程序。
        '''
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  
# -*- coding: utf-8 -*-

"""
这是一个关于文本输入栏（QLineEdit）的小例子--掩码输入！
文章链接：http://www.xdbcb8.com/archives/612.html
"""

import sys
from PyQt5.QtWidgets import QLineEdit, QApplication, QDialog, QLabel, QMessageBox

class Line(QDialog):
    '''
    掩码输入
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
        self.resize(300, 100)
        self.setWindowTitle('微信公众号：学点编程吧--掩码输入')
        self.line = QLineEdit(self)
        line2 = QLineEdit(self)
        line3 = QLineEdit(self)
        line4 = QLineEdit(self)

        lb = QLabel('IP地址', self)
        lb2 = QLabel('MAC地址', self)
        lb3 = QLabel('日期', self)
        lb4 = QLabel('License', self)
        
        lb.move(10, 10)
        lb2.move(10, 30)
        lb3.move(10, 50)
        lb4.move(10, 70)

        self.line.move(80, 10)
        line2.move(80, 30)
        line3.move(80, 50)
        line4.move(80, 70)
        
        self.line.editingFinished.connect(self.Action)# 输入栏编辑完成后发出信号

        self.line.setInputMask('000.000.000.000;_')# 数字，空白是_
        line2.setInputMask('HH:HH:HH:HH:HH:HH;_')# 十六进制数字,MAC地址
        line3.setInputMask('0000-00-00')# 数字
        line4.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')# 大写字母

        self.show()

    def Action(self):
        '''
        输入栏完成后的槽函数
        '''
        if len(self.line.text()) > 3:
            QMessageBox.information(self, '提示信息', '这行你完成了哦')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    line = Line()
    sys.exit(app.exec_())
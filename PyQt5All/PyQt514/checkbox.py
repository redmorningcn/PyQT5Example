#coding=utf-8

'''
这是关于复选框的小例子！
文章链接：http://www.xdbcb8.com/archives/359.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class Example(QWidget):
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
        self.cb1 = QCheckBox('全选', self)
        self.cb2 = QCheckBox('你是', self)
        self.cb3 = QCheckBox('我的', self)
        self.cb4 = QCheckBox('宝贝', self)
        
        bt = QPushButton('提交', self)
        
        self.resize(300, 200)
        self.setWindowTitle('关注微信公众号：学点编程吧--复选框')
        
        self.cb1.move(20, 20)
        self.cb2.move(30, 50)
        self.cb3.move(30, 80)
        self.cb4.move(30, 110)
        
        bt.move(20, 160)
        
        self.cb1.stateChanged.connect(self.changecb1)
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        bt.clicked.connect(self.go)
        
        self.show()
        
    def go(self):
        '''
        复选框选择状态提交后看看你能输出什么
        '''
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '你是我的宝贝！')
        elif self.cb2.isChecked() and self.cb3.isChecked():
            QMessageBox.information(self, 'I Love U', '你是我的！')
        elif self.cb2.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '你是宝贝！')
        elif self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '我的宝贝！')
        elif self.cb2.isChecked():
            QMessageBox.information(self, 'I Love U', '你是！')
        elif self.cb3.isChecked():
            QMessageBox.information(self, 'I Love U', '我的！')
        elif self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '宝贝！')
        else:
            QMessageBox.information(self, 'I Love U', '貌似你没有勾选啊！')

    def changecb1(self):
        '''
        复选框cb1全选和反选
        '''
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)
            
    def changecb2(self):
        '''
        复选框cb2、cb3、cb4不同状态时，cb1状态的变化
        '''
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.cb1.setCheckState(Qt.Checked)#复选框cb2、cb3、cb4全选时，cb1状态是全选
        elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
            self.cb1.setTristate(True)
            self.cb1.setCheckState(Qt.PartiallyChecked)#复选框cb2、cb3、cb4有一个被选中时，cb1状态是半选
        else:
            self.cb1.setTristate(False)#必须设置否，否则cb1会出现半选状态。
            self.cb1.setCheckState(Qt.Unchecked)#复选框cb2、cb3、cb4其他状态时，cb1状态是半选
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#coding=utf-8

'''
这是关于进度对话框的小例子！
文章链接：http://www.xdbcb8.com/archives/354.html
'''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog)
from PyQt5.QtCore import Qt

class Example(QWidget):
    '''
    进度对话框
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
        self.resize(300, 150)
        self.setWindowTitle("微信公众号：学点编程吧--进度对话框")
        
        self.lb = QLabel("文件数量", self)
        self.lb.move(20, 40)
        
        self.bt1 = QPushButton('开始', self)
        self.bt1.move(20, 80)
        
        self.edit = QLineEdit('10000', self)
        self.edit.move(100, 40)
        
        self.show()
          
        self.bt1.clicked.connect(self.showDialog)

    def showDialog(self):
        '''
        显示进度对话框
        '''
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")  
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)
        # 估计操作所花费的时间（基于步骤的时间），并且只有当该估计值超出minimumDuration() （默认为4秒）时才显示

        progress.setWindowModality(Qt.WindowModal)
        # 此属性保留由模态小部件阻止的窗口。这个属性只对Windows有意义。
        # 模态小部件防止其他窗口中的小部件获取输入。该属性的值控制在窗口小部件可见时阻止哪些窗口。
        # 窗口可见时更改此属性无效；您必须首先hide()小部件，然后再次show()。

        progress.setRange(0, num)#设置进度范围

        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():#判断我们是否按下取消按钮
                QMessageBox.warning(self, "提示", "操作失败")
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, "提示", "操作成功")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
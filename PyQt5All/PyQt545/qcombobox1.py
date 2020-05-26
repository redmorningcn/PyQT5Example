# -*- coding: utf-8 -*-

"""
这是一个QComboBox使用的小例子！
文章链接：http://www.xdbcb8.com/archives/764.html
"""

import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon

class ExComboBox(QWidget):
    '''
    下拉框简单举例
    '''

    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        '''
        界面初始设置
        '''
        self.resize(400, 100)
        self.setWindowTitle("微信公众号：学点编程吧--下拉框1")
        self.show()

        label1 = QLabel("你可以选择", self)
        combox = QComboBox(self)
        label2 = QLabel("大家静一静，", self)
        self.label3 = QLabel("        ", self)

        hlayout1 = QHBoxLayout()
        hlayout1.addStretch(1)
        hlayout1.addWidget(label1)
        hlayout1.addStretch(1)
        hlayout1.addWidget(combox)
        hlayout1.addStretch(1)

        hlayout2 = QHBoxLayout()
        hlayout2.addStretch(1)
        hlayout2.addWidget(label2)
        hlayout2.addStretch(1)
        hlayout2.addWidget(self.label3)
        hlayout2.addStretch(1)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        self.setLayout(vlayout)

        infomation = ["我想静静", "我要开始学习了", "我要开始睡觉了", "我要开始装B了"]

        combox.addItems(infomation)
        # 使用addItems()函数将列表数据放入

        self.label3.setText(combox.currentText())
        # 将label3的文本设置为当前选项的值
        # currentText()属性保存当前文本。
        # 如果下拉框是可编辑的，则当前文本是下拉框中显示的值。否则，如果下拉框为空或未设置当前项目，则为当前项目的值或空字符串。

        combox.activated[str].connect(self.zhuangB)
        # 这个信号会把选中的值（字符串）传递给槽函数zhuangB()
    
    def zhuangB(self, text):
        '''
        一个装B功能
        '''
        self.label3.setText(text)
        if text == "我要开始装B了":
            msgBox = QMessageBox(QMessageBox.NoIcon, '装B', "让你装B")
            msgBox.setIconPixmap(QPixmap("./res/zhuangB.png"))
            msgBox.setWindowIcon(QIcon("./res/latin_b.png"))
            msgBox.exec()
            # 当我们选择“我要开始装B了”，就会弹出相应的对话框

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExComboBox()
    sys.exit(app.exec_())
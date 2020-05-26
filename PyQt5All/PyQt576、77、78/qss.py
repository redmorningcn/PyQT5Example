#coding=utf-8

'''
这是一个关于QSS的小例子
文章链接：http://www.xdbcb8.com/archives/1464.html
文章链接：http://www.xdbcb8.com/archives/1484.html
文章链接：http://www.xdbcb8.com/archives/1529.html
QSS的中文注释会有问题，建议本期去文章上看！
'''

import sys
import codecs
from PyQt5.QtWidgets import QApplication, QLineEdit, QCheckBox, QWidget, QComboBox, QPushButton, QRadioButton, QGroupBox, QVBoxLayout, qApp

class Ex(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        self.resize(500, 500)
        self.setWindowTitle("微信公众号：学点编程吧")
        line = QLineEdit(self)
        line.move(100, 120)
        check = QCheckBox("选我", self)
        check.move(300, 120)
        line.setStyleSheet("background: yellow")# 背景红色
        check.setStyleSheet("color: red")# 样式红色

        bt = QPushButton("按钮", self)
        bt.move(100, 180)
        rt = QRadioButton("单选", self)
        rt.move(200, 180)

        qcom = QComboBox(self)
        qcom.move(100, 250)
        lists = ["apple", "banana", "pear", "peach"]
        qcom.addItems(lists)

        groupbox = QGroupBox("分组", self)
        bt1 = QPushButton("按钮1", self)
        bt2 = QPushButton("按钮2", self)
        vbox = QVBoxLayout(self)
        vbox.addWidget(bt1)
        vbox.addWidget(bt2)
        groupbox.setLayout(vbox)
        
        qApp.setStyleSheet("QGroupBox, QGroupBox * { color: red; } ")# 全局按钮组红色

        with codecs.open("xx.qss", "r") as f:
            style = f.read()
        self.setStyleSheet(style)
        # 读取qss样式，并设置

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ex()
    sys.exit(app.exec_())
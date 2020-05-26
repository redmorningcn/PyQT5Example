# -*- coding: utf-8 -*-

"""
一个关于欢乐斗地主（QMdiArea的使用）的小例子！
文章链接：http://www.xdbcb8.com/archives/859.html
"""

from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap

class Card(QLabel):
    def __init__(self, num=""):
        '''
        一些初始设置
        '''
        super().__init__()
        if num == "":
            self.num = "2"
            # 最差发2
        else:
            self.num = num
        self.initui()

    def initui(self):
        '''
        界面初始设置
        '''
        path = "./res/pokercards/" + self.num + ".png"
        # 把每张牌的基本路径设置好
        pixmap = QPixmap(path)
        self.setPixmap(pixmap)
        self.setScaledContents(True)
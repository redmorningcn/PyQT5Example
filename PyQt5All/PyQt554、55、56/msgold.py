# -*- coding: utf-8 -*-

"""
一个关于QTimer与QThread的综合应用举例的小例子！
文章链接：http://www.xdbcb8.com/archives/867.html
文章链接：http://www.xdbcb8.com/archives/870.html
文章链接：http://www.xdbcb8.com/archives/872.html
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Ui_digdone import Ui_Dialog

class MsgGold(QDialog, Ui_Dialog):
    """
    自定义挖矿结果消息框
    """
    def __init__(self, cc, parent=None):
        """
        一些初始设置
        """
        super(MsgGold, self).__init__(parent)
        self.setupUi(self)
        if cc < 10:
            self.label_gold.setText("你挖到了" + str(cc) + "块金矿！\n试试挖的时间长点吧！")
        elif cc < 100:
            self.label_gold.setText("恭喜你挖到了" + str(cc) + "块金矿！")
        else:
            self.label_gold.setText("真棒！你挖到了" + str(cc) + "块金矿！")
        # 看看你挖的成果如何
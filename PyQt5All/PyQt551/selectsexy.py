# -*- coding: utf-8 -*-

"""
这是QQ秀 – 释放我不凡！（QStackedWidget的使用）的小例子--选择性别！
文章链接：http://www.xdbcb8.com/archives/838.html
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from Ui_sexy import Ui_Form

class SelectSexy(QWidget, Ui_Form):

    """
    性别选择对话框代码，由Eric6自动生成
    """

    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(SelectSexy, self).__init__(parent)
        self.setupUi(self)
    

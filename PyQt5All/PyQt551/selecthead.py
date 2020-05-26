# -*- coding: utf-8 -*-

"""
这是QQ秀 – 释放我不凡！（QStackedWidget的使用）的小例子--选择头饰！
文章链接：http://www.xdbcb8.com/archives/838.html
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from selectsexy import SelectSexy
from Ui_head import Ui_Form


class SelectHead(QWidget, Ui_Form):

    """
    头型选择对话框代码，由Eric6自动生成
    """

    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(SelectHead, self).__init__(parent)
        self.setupUi(self)
    
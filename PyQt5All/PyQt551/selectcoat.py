# -*- coding: utf-8 -*-

"""
这是QQ秀 – 释放我不凡！（QStackedWidget的使用）的小例子--选择衣着！
文章链接：http://www.xdbcb8.com/archives/838.html
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox
from Ui_coat import Ui_Form


class SelectCoat(QWidget, Ui_Form):
    """
    衣着选择对话框代码，由Eric6自动生成
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(SelectCoat, self).__init__(parent)
        self.setupUi(self)
    
    
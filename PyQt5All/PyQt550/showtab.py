# -*- coding: utf-8 -*-

"""
天气展示Tab
文章链接：http://www.xdbcb8.com/archives/827.html
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from Ui_showeather import Ui_Tab

class showTab(QWidget, Ui_Tab):
    """
    天气展示Tab，Eric6生成的对话框代码
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(showTab, self).__init__(parent)
        self.setupUi(self)

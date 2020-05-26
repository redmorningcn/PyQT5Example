# -*- coding: utf-8 -*-

"""
展示实时天气的QWidget子类，我们设置一下天气状况、当前温度、最新的更新时间，以及根据天气状况代码选择相应的天气图片
文章链接：http://www.xdbcb8.com/archives/827.html
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from Ui_realtimew import Ui_RealTime

class RealTimeWeather(QWidget, Ui_RealTime):
    """
    展示实时天气的QWidget子类
    """
    def __init__(self, parent=None):
        """
        一些初始化设置，这个一看就是Eric6自动生成的对话框代码
        """
        super(RealTimeWeather, self).__init__(parent)
        self.setupUi(self)

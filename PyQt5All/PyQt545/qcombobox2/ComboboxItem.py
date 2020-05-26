# -*- coding: utf-8 -*-

"""
这是一个像QQ多用户登录（QComboBox的使用）的例子！
文章链接：http://www.xdbcb8.com/archives/764.html
"""

import sys
import codecs
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication, QToolButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QEvent, QObject, pyqtSignal

class ComboBoxItem(QWidget):
    '''
    下拉框每个小部件
    '''
    itemOpSignal = pyqtSignal(str)
    # 自定义str信号

    def __init__(self, qq, username, user_icon):
        '''
        一些初始设置
        '''
        super().__init__()
        self.username = username
        self.qq = qq
        self.user_icon = user_icon
        self. initUi()

    def initUi(self):
        '''
        界面初始设置
        '''
        lb_username = QLabel(self.username, self)
        lb_qq = QLabel(self.qq, self)
        lb_icon = QLabel(self)
        lb_icon.setPixmap(QPixmap(self.user_icon))
        self.bt_close = QToolButton(self)
        self.bt_close.setIcon(QIcon("../res/close.png"))
        self.bt_close.setAutoRaise(True)

        vlayout = QVBoxLayout()
        vlayout.addWidget(lb_username)
        vlayout.addWidget(lb_qq)

        hlayout = QHBoxLayout()
        hlayout.addWidget(lb_icon)
        hlayout.addLayout(vlayout)
        hlayout.addStretch(1)
        hlayout.addWidget(self.bt_close)
        hlayout.setContentsMargins(5, 5, 5, 5)
        # 设置要在布局周围使用的边距。默认情况下，在大多数平台上，边距为所有方向的11个像素。
        hlayout.setSpacing(5)
        # 此属性保存布局内的窗口小部件之间的间距

        self.setLayout(hlayout)

        self.bt_close.installEventFilter(self)
        self.installEventFilter(self)
        # 为bt_close按钮和ComboBoxItem自身安装事件过滤器

    def eventFilter(self, object, event):
        '''
        事件过滤器
        '''
        if object is self:
            if event.type() == QEvent.Enter:
                self.setStyleSheet("QWidget{color:white}")
            elif event.type() == QEvent.Leave:
                self.setStyleSheet("QWidget{color:black}")
            #当我们把鼠标移入后颜色会变化哦
        elif object is self.bt_close:
            if event.type() == QEvent.MouseButtonPress:  
                self.itemOpSignal.emit(self.qq)#点击关闭按钮，发出信号
        return QWidget.eventFilter(self, object, event)
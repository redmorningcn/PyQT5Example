# -*- coding: utf-8 -*-

"""
这是一个关于文本输入栏（QLineEdit）的小例子--密码输入框超级加强版！
文章链接：http://www.xdbcb8.com/archives/632.html
"""

from PyQt5.QtWidgets import QLineEdit, QApplication
from PyQt5.QtCore import QTimer

class PwdLineEdit(QLineEdit):

    """
    自定义密码输入框
    """

    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.m_LineEditText = ""
        # 记录真实的密码

        self.m_LastCharCount = 0
        # 密码出现变化前的长度

        self.Action()
    
    def Action(self):
        '''
        一些初始设置
        '''
        self.cursorPositionChanged[int, int].connect(self.DisplayPasswordAfterEditSlot)
        # 光标发生移动时产生，返回两个整型变量并调用槽函数

        self.textEdited[str].connect(self.GetRealTextSlot)
        self.time = QTimer(self)# 设置一个定时器
        self.time.setInterval(200)# 200毫秒超时，也就是200毫秒把单个字符变成*
        self.time.start()
        self.show()
    
    def DisplayPasswordAfterEditSlot(self, old, new):
        '''
        显示密文
        '''
        if old >= 0 and new >= 0:
            if new > old:
                self.time.timeout.connect(self.DisplayPasswordSlot)# 密码在增加，自动刷新成*
            else:
                self.setCursorPosition(old)# 尝试注释这个，你可以看看效果，非常爽！

    def DisplayPasswordSlot(self):
        '''
        在密码输入框把密码变成**等
        '''
        self.setText(self.GetMaskString())      

    def GetRealTextSlot(self, text):
        '''
        获取真实密码
        '''
        self.m_LastCharCount = len(self.m_LineEditText)
        # 当前没有变化时密码的长度
        
        if len(text) > self.m_LastCharCount:
            self.m_LineEditText += text[-1]
        # 当前的长度大于之前记录的密码长度，密码在新增字符，将新增的字符和原有的密码进行合并。
            
        elif len(text) <= self.m_LastCharCount:
            self.m_LineEditText = self.m_LineEditText[:-1]
        # 密码删除中，真实密码也在变少。

    def GetMaskString(self):
        '''
        把明文密码变成*
        '''
        mask = ""
        count = len(self.text())
        if count > 0:
            for i in range(count):
                mask += "*"
        return mask
    
    def GetPassword(self):
        '''
        获得真实密码
        '''
        return self.m_LineEditText
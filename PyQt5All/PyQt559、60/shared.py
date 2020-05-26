# -*- coding: utf-8 -*-

"""
这是一个关于Web页面交互初探2（QWebChannel和QWebEngineView的综合使用）的小例子！
文章链接：http://www.xdbcb8.com/archives/1102.html
文章链接：http://www.xdbcb8.com/archives/1126.html
"""

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtProperty, pyqtSignal

class Myshared(QWidget):
    '''
    共享类
    '''

    finish = pyqtSignal(list)
    #自定义一个finish信号

    def __init__(self):
        super().__init__()
    
    def PyQt52WebValue(self):
        return "666"
    
    def Web2PyQt5Value(self, strs):
        '''
        获得Web页面传值后续处理
        '''
        info = strs.split()
        # 信息分成用户名和密码

        fullinfo = "用户名：{}，密码：{}".format(info[0], info[1])
        QMessageBox.information(self, "从Web页面传值到PyQt5", fullinfo)
        self.finish.emit(info)
        # 信号发出去

    value = pyqtProperty(str, fget=PyQt52WebValue, fset=Web2PyQt5Value)
    # pyqtProperty()函数定义新的PyQt属性
    # fget是获取属性值的函数；fset是用于设置属性值的函数。
    # 这个知识点比较新，请到文章处仔细阅读！！
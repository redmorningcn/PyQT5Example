# -*- coding: utf-8 -*-

"""
这是一个关于PyQt5与数据库互联（极简图书管理Plus）的小例子！
文章链接：http://www.xdbcb8.com/archives/1234.html
文章链接：http://www.xdbcb8.com/archives/1286.html
文章链接：http://www.xdbcb8.com/archives/1302.html
文章链接：http://www.xdbcb8.com/archives/1307.html
"""

from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtGui import QIcon

class BookSqlTableModel(QSqlTableModel):
    '''
    数据模型
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()

    def data(self, index, role):
        '''
        在模型索引存在的情况下，我们表格中数据排列是垂直、水平居中；
        同时在第一列的数据中，我们需要返回一个图标。这个图标是根据第一列的数据来选择的。
        其他情况使用父类QSqlTableModel的默认数据。
        '''
        if index.isValid():
            if role == Qt.TextAlignmentRole:
                return QVariant(Qt.AlignHCenter | Qt.AlignVCenter)
            if role == Qt.DecorationRole and index.column() == 0:
                countryName = index.data()
                countryIconPath = self.getCountry(countryName)
                return QVariant(countryIconPath)
            else:
                return super().data(index, role)

    def getCountry(self, countryName):
        '''
        根据国家名称返回对应的国旗图标
        '''
        if countryName == "中":
            countryIcon = QIcon("./res/countries/china.png")
        elif countryName == "英":
            countryIcon = QIcon("./res/countries/english.png")
        elif countryName == "日":
            countryIcon = QIcon("./res/countries/japan.png")
        elif countryName == "俄":
            countryIcon = QIcon("./res/countries/russian.png")
        elif countryName == "美":
            countryIcon = QIcon("./res/countries/usa.png")
        elif countryName == "智":
            countryIcon = QIcon("./res/countries/chile.png")
        else:
            countryIcon = QIcon("./res/countries/default.png")
        return countryIcon
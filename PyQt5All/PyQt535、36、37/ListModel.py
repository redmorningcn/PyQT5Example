#coding=utf-8

"""
这是一个关于QQ模拟（QListView的使用）的例子--模型定义！
文章链接：http://www.xdbcb8.com/archives/701.html
"""

import random
import Random_Name
from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant, QSize
from PyQt5.QtGui import QIcon, QFont

class ListModel(QAbstractListModel):
    '''
    自定义模型
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()     
        self.ListItemData = []
        # 存储每个QQ用户的列表

        self.Data_init()

    def data(self, index, role):
        '''
        子类化QAbstractListModel必须要实现的函数，主要作用就是返回index所引用项目的给定role下存储的数据。
        '''
        if index.isValid() or (0 <= index.row() < len(self.ListItemData)):
            if role == Qt.DisplayRole:
                return QVariant(self.ListItemData[index.row()]['name'])
                # 文本形式呈现数据
            elif role == Qt.DecorationRole:
                return QVariant(QIcon(self.ListItemData[index.row()]['iconPath']))
                # 以图标形式呈现装饰数据
            elif role == Qt.SizeHintRole:
                return QVariant(QSize(70, 80))
                # 视图项目大小
            elif role == Qt.TextAlignmentRole:
                return QVariant(int(Qt.AlignHCenter|Qt.AlignVCenter))
                # 文本对齐方式
            elif role == Qt.FontRole:
                font = QFont()
                font.setPixelSize(20)
                return QVariant(font)
                # 字体设置
        return QVariant()
        # 非上述情况，返回为空，记住这里是QVariant()

    def rowCount(self, parent = QModelIndex()):
        '''
        返回行数，在这里就是数据列表的大小。
        '''
        return len(self.ListItemData)

    def Data_init(self):
        '''
        数据初始化
        '''
        randomnum = random.sample(range(26), 10)
        # 从0-25个数字中随机的抽取10个不重复的数字组成一个列表
        for i in randomnum:
            randname = Random_Name.getname()
            ItemData = {'name':'', 'iconPath':''}
            ItemData['name'] = randname
            ItemData['iconPath'] = "./res/"+ str(i) + ".jpg"
            # 遍历这个列表randomnum，其中联系人的姓名我是随机生成的，随机的生成图标的路径；把姓名和图标路径添加到字典当中。

            self.ListItemData.append(ItemData)
            # append到数据列表里面。

    def addItem(self, itemData):
        '''
        新增的操作实现
        '''
        if itemData:
            self.beginInsertRows(QModelIndex(), len(self.ListItemData), len(self.ListItemData) + 1)
            self.ListItemData.append(itemData)
            self.endInsertRows()
            # 结束行插入操作

    def deleteItem(self, index):
        '''
        指定索引的数据从数据列表中删除
        '''
        del self.ListItemData[index]

    def getItem(self, index):
        '''
        获得相应的项目数据
        '''
        if index > -1 and index < len(self.ListItemData):
            return self.ListItemData[index]

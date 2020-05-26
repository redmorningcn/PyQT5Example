#coding=utf-8

"""
这是一个关于QQ模拟（QListView的使用）的例子--前面的整合！
文章链接：http://www.xdbcb8.com/archives/714.html
"""

import sys
from PyQt5.QtWidgets import QApplication, QToolBox, QListView, QMenu, QAction, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from ListView import ListView
from PyQt5.QtGui import QIcon

class QQ(QToolBox):
    '''
    自定义类的整合
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.setWindowTitle('公众号：学点编程吧--QQ')
        self.setWindowFlags(Qt.Dialog)
        self.setMinimumSize(200, 600)
        self.setWhatsThis('这个一个模拟QQ软件')
        self.setWindowIcon(QIcon('./res/log.ico'))
        pListView = ListView() 
        pListView.setViewMode(QListView.ListMode)
        # 设置模型

        pListView.setStyleSheet("QListView{icon-size:70px}")
        # 设置QListView图标的大小70像素

        dic_list = {'listview':pListView, 'groupname':"我的好友"}
        # 当前listview对象和分组名称放入到一个字典

        pListView.setListMap(dic_list)
        # 这个字典放入到map_listview这个列表

        self.addItem(pListView, "我的好友") 
        self.show()
    
    def contextMenuEvent(self, event):
        '''
        上下文菜单
        '''
        pmenu = QMenu(self)
        pAddGroupAct = QAction("添加分组", pmenu)
        pmenu.addAction(pAddGroupAct)
        pAddGroupAct.triggered.connect(self.addGroupSlot)
        pmenu.popup(self.mapToGlobal(event.pos()))
    
    def addGroupSlot(self):
        '''
        增加分组
        '''
        groupname = QInputDialog.getText(self, "输入分组名", "")
        # groupname这里返回的是一个元组，其中第0个元素是分组名，第1个元素返回是否按了确定键

        if groupname[0] and groupname[1]:
            pListView1 = ListView()
            pListView1.setViewMode(QListView.ListMode)
            pListView1.setStyleSheet("QListView{icon-size:70px}")
            self.addItem(pListView1, groupname[0])
            dic_list = {'listview':pListView1, 'groupname':groupname[0]}
            pListView1.setListMap(dic_list)
            # 新建一个ListView对象并将其与分组名称添加到字典当中，然后通过setListMap()将这个字典放入到map_listview这个列表中

        elif groupname[0] == '' and groupname[1]:
            QMessageBox.warning(self, "警告", "我说你没有填写分组名哦~！")
            # 没有填写分组名又按了确定键的话，就报错。

app = QApplication(sys.argv)
qq = QQ()
sys.exit(app.exec_())
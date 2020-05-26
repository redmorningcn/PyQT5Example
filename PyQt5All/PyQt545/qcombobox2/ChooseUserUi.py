# -*- coding: utf-8 -*-

"""
这是一个像QQ多用户登录（QComboBox的使用）的例子！
文章链接：http://www.xdbcb8.com/archives/764.html
"""

import sys
import codecs
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from AddUser import DialogAddUser
from ComboboxItem import ComboBoxItem
from Ui_ui import Ui_Dialog

class ChooseUser(QDialog, Ui_Dialog):
    """
    像QQ一样选择用户
    """
    storage_qq = []
    # 这个列表我们是存储每个联系人QQ号

    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(ChooseUser, self).__init__(parent)
        self.setupUi(self)
        self.setmode()
    
    def setmode(self):
        '''
        导入样式
        '''
        with codecs.open("../res/qcombobox.qss", "r", "utf-8") as f:
            styleSheet = f.readlines()
        style = '\r\n'.join(styleSheet)
        self.comboBox.setStyleSheet(style)

        self.listw = QListWidget()
        self.comboBox.setModel(self.listw.model())
        self.comboBox.setView(self.listw)
        # QListWidget设置为QComboBox的View，QListWidget的Model设置为QComboBox的Model
    
    @pyqtSlot()
    def on_toolButton_clicked(self):
        """
        新增联系人
        """
        user = DialogAddUser()
        # 新增联系人对话框

        r = user.exec_()
        if r > 0:
            qq, username, user_icon = user.get_userinfo()
            item = ComboBoxItem(qq, username, user_icon)
            item.itemOpSignal.connect(self.itemOp)
            self.storage_qq.append(qq)
            self.listwitem = QListWidgetItem(self.listw)
            # 用给定的父项(self.listw)构造指定类型的空列表项目

            self.listw.setItemWidget(self.listwitem, item)
            # 将小部件设置为在给定项目中显示。也就是将我们自定义的Item显示在self.listwitem中
    
    def itemOp(self, qq):
        """
        删除联系人
        """
        indexqq = self.storage_qq.index(qq)
        self.listw.takeItem(indexqq)
        del self.storage_qq[indexqq]
        # 根据得到的QQ号得到相应的索引，然后根据索引删除self.listw的项目以及storage_qq列表中存储的数据完成最后的删除操作。
    
    @pyqtSlot(int)
    def on_comboBox_activated(self, p0):
        """
        将item的索引带过来，选择显示QQ号
        """
        qq = self.storage_qq[p0]
        self.comboBox.setEditText(qq)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ChooseUser()
    ex.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

"""
这是一个像QQ多用户登录（QComboBox的使用）的例子！
文章链接：http://www.xdbcb8.com/archives/764.html
"""

import Random_Name
import random
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from Ui_adduser import Ui_Dialog


class DialogAddUser(QDialog, Ui_Dialog):
    """
    自定义新增联系人对话框
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogAddUser, self).__init__(parent)
        self.setupUi(self)
        self.username = Random_Name.getname()
        self.iconpath = "../res/user/default.jpg"
        self.qq = str(random.randint(33333333, 88888888))
        # 随机QQ号
    
    @pyqtSlot(bool)
    def on_radioButton_toggled(self, checked):
        """
        默认填写姓名不可填写
        """
        self.lineEdit.setEnabled(False)
    
    @pyqtSlot(bool)
    def on_radioButton_2_toggled(self, checked):
        """
        填写姓名可用
        """
        self.lineEdit.setEnabled(True)
    
    @pyqtSlot(bool)
    def on_radioButton_3_toggled(self, checked):
        """
        默认图标
        """
        self.pushButton.setEnabled(False)
    
    @pyqtSlot(bool)
    def on_radioButton_4_toggled(self, checked):
        """
        自定义图标
        """
        self.pushButton.setEnabled(True)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        选择图标
        """
        file = QFileDialog.getOpenFileName(self, "打开文件", "../res/user/", ("Images (*.png *jpg)"))
        if file[0]:
            self.iconpath = file[0]
    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        提交新用户
        """
        if self.lineEdit.isEnabled() and self.lineEdit.text() == "":
            QMessageBox.warning(self, "警告", "联系人姓名为空")
            self.lineEdit.setFocus()
        else:
            self.done(1)
    
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        """
        取消提交
        """
        self.done(-1)

    @pyqtSlot()
    def on_lineEdit_editingFinished(self):
        """
        用户名是输入框的内容，这个在输入框完成编辑后自动赋值
        """
        self.username = self.lineEdit.text()
    
    def get_userinfo(self):
        '''
        返回QQ号，姓名，图标路径
        '''
        return self.qq, self.username, self.iconpath
# -*- coding: utf-8 -*-

"""
这是一个关于文本输入栏（QLineEdit）的小例子--用户注册！
文章链接：http://www.xdbcb8.com/archives/632.html
"""

import sys
import re
from PyQt5.QtCore import pyqtSlot, QEvent, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QCompleter
from PyQt5.QtGui import QStandardItemModel, QKeyEvent, QKeySequence
from Ui_UI import Ui_Dialog

class Dialog_ui(QDialog, Ui_Dialog):
    """
    用户注册
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(Dialog_ui, self).__init__(parent)
        self.setupUi(self)
        self.ActionStart()
    
    def ActionStart(self):
        '''
        一些需要初始化的设置
        '''
        self.lineEdit_2.installEventFilter(self)# 安装事件过滤器
        self.lineEdit_3.installEventFilter(self)
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)# 不支持上下文菜单
        self.lineEdit_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.m_model = QStandardItemModel(0, 1, self)# 为存储自定义数据提供了一个通用模型，该模型最初具有0行和1列
        m_completer = QCompleter(self.m_model, self)# 用给定的父对象构造一个完成对象，该对象提供来自指定模型的完成对象
        self.lineEdit_7.setCompleter(m_completer)# 提供自动完成
        m_completer.activated[str].connect(self.onEmailChoosed)# 选定后连接到onEmailChoosed槽函数
    
    def onEmailChoosed(self, email):
        '''
        我们确定自动补全的电子邮件后，设置当前输入的值。
        '''
        self.lineEdit_7.setText(email)
            
    def eventFilter(self, object, event):
        '''
        事件过滤器，主要是对密码输入框进行操作的。
        '''
        if object == self.lineEdit_2:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True# 鼠标移动、鼠标双击过滤掉
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True# 键盘全选、复制、粘贴快捷键过滤掉
        elif object == self.lineEdit_3:
            # 同上
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)

    @pyqtSlot()
    def on_lineEdit_editingFinished(self):
        """
        用户名判断
        """
        regex_user = '^[a-zA-Z]\w{5,17}$'# 6-18位数字、字母，字母开头
        username = self.lineEdit.text()
        if len(username) > 0:
            self.lineEdit_6.clear()
            rruser = re.compile(regex_user)
            if rruser.match(username) is None:
                # 用正则匹配一下，要是没有匹配上
                self.lineEdit_6.setText('用户名不符合要求!')
        else:
            self.lineEdit_6.setText('用户名未填写!')
    
    @pyqtSlot()
    def on_lineEdit_2_editingFinished(self):
        """
        密码输入判断
        """
        regex_pwd = "^([A-Z]|[a-z]|[0-9]|[`~!@#$%^&*()+=|{}':;',\\\\[\\\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“'。，、？]){6,16}$"
        # 6-16个字符
        self.pwd1 = self.lineEdit_2.GetPassword()
        if len(self.pwd1) > 0:
            self.lineEdit_6.clear()
            rrpwd = re.compile(regex_pwd)
            if rrpwd.match(self.pwd1) is None:
                self.lineEdit_6.setText('密码不符合要求!')
        else:
            self.lineEdit_6.setText('密码未填写!')

    
    @pyqtSlot()
    def on_lineEdit_3_editingFinished(self):
        """
        密码输入再判断
        """
        self.pwd2 = self.lineEdit_3.GetPassword()
        regex_pwd = "^([A-Z]|[a-z]|[0-9]|[`~!@#$%^&*()+=|{}':;',\\\\[\\\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“'。，、？]){6,16}$"
        # 6-16个字符
        if len(self.pwd2) > 0:
            self.lineEdit_6.clear()
            rrpwd = re.compile(regex_pwd)
            if rrpwd.match(self.pwd2) is None:
                self.lineEdit_6.setText('密码不符合要求!')
            if self.pwd1 != self.pwd2:
                self.lineEdit_6.setText('两次密码不一致!')
        else:
            self.lineEdit_6.setText('密码未填写!')


    @pyqtSlot()
    def on_lineEdit_4_editingFinished(self):
        """
        手机号码判断
        """
        regex_phone = '^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$'
        phone = self.lineEdit_4.text()
        if len(phone) > 0:
            self.lineEdit_6.clear()
            rr1 = re.compile(regex_phone)
            if rr1.match(phone) is None:
                self.lineEdit_6.setText('请填写正确的手机号!')
        else:
            self.lineEdit_6.setText('手机号码未填写!')
    
    @pyqtSlot()
    def on_lineEdit_7_editingFinished(self):
        """
        电子邮件判断
        """
        regex_mail = '^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$'
        email = self.lineEdit_7.text()
        if len(email) > 0:
            self.lineEdit_6.clear()
            rr1 = re.compile(regex_mail)
            if rr1.match(email) is None:
                self.lineEdit_6.setText('请填写正确的邮箱地址!')
        else:
            self.lineEdit_6.setText('邮箱地址未填写!')

    @pyqtSlot(str)
    def on_lineEdit_7_textChanged(self, text):
        '''
        电子邮件自动补全
        '''
        if '@' in self.lineEdit_7.text():
            return
        # 当@出现时，就不再补全了哦

        emaillist = [ "@163.com", "@qq.com", "@gmail.com", "@live.com", "@126.com", "@139.com"]# 支持这些邮箱自动补全

        self.m_model.removeRows(0, self.m_model.rowCount())# 每次都要把之前数据清空，否则就会重复，不信你可以试试！

        for i in range(0, len(emaillist)):# 遍历支持补全的邮箱
            self.m_model.insertRow(0)# 插入位置
            self.m_model.setData(self.m_model.index(0, 0), text + emaillist[i])# 指定位置插入补全后的电子邮箱

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dg = Dialog_ui()
    dg.show()
    sys.exit(app.exec_())
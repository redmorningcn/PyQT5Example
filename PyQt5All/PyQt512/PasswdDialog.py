#coding=utf-8

'''
DIY自己的密码框，用在main.py中
文章链接：http://www.xdbcb8.com/archives/343.html
'''

from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator

class PasswdDialog(QDialog):
    '''
    我们自己的密码输入框
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        界面初始设置
        '''
        self.resize(350, 100)
        self.setWindowTitle("密码输入框")

        self.lb = QLabel("请输入密码：", self)
        
        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)# 输入框安装事件过滤器
        
        self.bt1 = QPushButton("确定", self)
        self.bt2 = QPushButton("取消", self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.edit)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
    
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)# 不允许出现上下文菜单
        self.edit.setPlaceholderText("密码不超15位，只能有数字和字母，必须以字母开头")# 输入密码前可以看到一些小提示信息，这个非常实用。
        self.edit.setEchoMode(QLineEdit.Password)# 加密显示输入内容
        
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        # 构建一个正则表达式：
        # 1、长度不能超过15位；
        # 2、字母开头；
        # 3、后面跟着的字符只能是字母或者数字。

        validator = QRegExpValidator(regx, self.edit)
        # 构造一个验证器，QLineEdit对象接受与正则表达式匹配的所有字符串。匹配是针对整个字符串。

        self.edit.setValidator(validator)
        # 将密码输入框设置为仅接受符合验证器条件的输入

        self.bt1.clicked.connect(self.Ok)
        self.bt2.clicked.connect(self.Cancel)
        
        #object = QObject()
        
    def eventFilter(self, object, event):
        '''
        鼠标移动对应的事件类型为QEvent.MouseMove，
        鼠标双击对应的事件类型为QEvent.MouseButtonDblClick，
        全选、复制、粘贴对应的事件类型为 QEvent.KeyPress，当接收到这些事件时，需要被过滤掉，返回true。
        '''
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self, object, event)#继续传递该事件到被观察者，由其本身调用相应的事件
        
    def Ok(self):
        '''
        结束对话框返回1
        '''
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(self.text) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            self.done(1)
    
    def Cancel(self):
        '''
        结束对话框返回0
        '''
        self.done(0)
    
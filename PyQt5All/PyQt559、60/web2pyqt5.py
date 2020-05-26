# -*- coding: utf-8 -*-

"""
这是一个关于Web页面交互初探2（QWebChannel和QWebEngineView的综合使用）的小例子！
文章链接：http://www.xdbcb8.com/archives/1102.html
文章链接：http://www.xdbcb8.com/archives/1126.html
"""

import sys
from PyQt5.QtCore import pyqtSlot, Qt, QUrl, QFileInfo
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from Ui_main import Ui_Form
from shared import Myshared

class Web2PyQt5(QWidget, Ui_Form):
    """
    Web像PyQt5传值
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(Web2PyQt5, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        """
        界面初始设置
        """
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 7)
        # QSplitter的窗口伸缩因子

        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # 只有关闭按钮

        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, -1, -1)
        url = QUrl(QFileInfo("./webchannel.html").absoluteFilePath())
        # 绝对路径

        self.view = QWebEngineView(self.widget)
        vLayout.addWidget(self.view)
        self.widget.setLayout(vLayout)
        self.view.load(url)
        # 读取并载入webchannel.html

    @pyqtSlot()
    def on_pb_submit_clicked(self):
        """
        用户名和密码提交
        """
        if self.lineEdit_username.text() == "":
            QMessageBox.warning(self, "警告", "用户名没有输入")
            self.lineEdit_username.setFocus()
        elif self.lineEdit_pwd.text() == "":
            QMessageBox.warning(self, "警告", "密码没有输入")
            self.lineEdit_pwd.setFocus()
        else:
            name = self.lineEdit_username.text()
            pwd = self.lineEdit_pwd.text()
            jscode = "PyQt52WebValue('{}','{}');".format(name, pwd)
            self.view.page().runJavaScript(jscode)
            # 运行javascript代码

    @pyqtSlot()
    def on_pb_reset_clicked(self):
        """
        PyQt5的输入栏内容清空--重置
        """
        self.lineEdit_username.setText("")
        self.lineEdit_pwd.setText("")

    def setLineEdit(self, list):
        '''
        根据交互值设置用户名和密码
        '''
        self.lineEdit_username.setText(list[0])
        self.lineEdit_pwd.setText(list[1])

    def __del__(self):
        '''
        删除相关对象
        '''
        self.view.deleteLater()
        # 让系统加快释放这部分内存，避免QWebEngineView崩溃
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    web_pyqt = Web2PyQt5()
    # 在Qt WebEngine中运行的客户端，可以通过”./qwebchannel.js”加载该文件
    # 本例中请在webchannel.html中加载qwebchannel.js

    web_pyqt.show()

    channel = QWebChannel()
    # 通道

    shared = Myshared()
    # 共享类

    channel.registerObject("connection", shared)
    # 将单个对象注册到QWebChannel
    # 标示符id是“connection”，对象是“shared”

    web_pyqt.view.page().setWebChannel(channel)
    # 设置此页面使用的Web通道实例，以便在JavaScript中引导和安装它。使用此方法，可以通过网页内容访问Web通道。

    shared.finish[list].connect(web_pyqt.setLineEdit)
    # 共享类中的信号传值会调用槽函数web_pyqt.setLineEdit()
    
    sys.exit(app.exec_())
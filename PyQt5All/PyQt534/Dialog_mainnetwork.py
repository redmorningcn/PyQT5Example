# -*- coding: utf-8 -*-

"""
这是一个可以浏览在线图片（QTextEdit）的例子！
文章链接：http://www.xdbcb8.com/archives/670.html
"""

import sys
import requests
from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QImage, QTextDocument
from Ui_mainnetwork import Ui_Dialog
from PIL import Image
from io import BytesIO

class Dialog_mainnetwork(QDialog, Ui_Dialog):
    """
    浏览在线图片
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(Dialog_mainnetwork, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        提交看图片
        """
        response = requests.get(self.lineEdit.text())
        # 使用requests库进行网络请求获取内容

        image1 = Image.open(BytesIO(response.content))
        # 对得到的二进制数据进行操作

        image1.save('xxx.png')
        # 保存网络图片到本地

        del image1
        # 删除图片对象(虽说会自己释放)，没有这个，会出现各种问题

        image = QImage('xxx.png')
        cursor = self.textEdit.textCursor()
        # 返回表示当前可见光标的QTextCursor的副本

        document = self.textEdit.document()
        # 返回编辑器的文档对象

        document.addResource(QTextDocument.ImageResource, QUrl("image"), image)
        # 将资源添加到资源缓存，使用类型和名称作为标识符

        cursor.insertImage("image")
        # 光标处插入图片
        
        # self.textEdit.append("<img src=\"xxx.png\" />")
        # 当然还有更简单的插入方式

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dg = Dialog_mainnetwork()
    dg.show()
    sys.exit(app.exec_())
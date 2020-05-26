# -*- coding: utf-8 -*-

"""
这是用Eric6实现的消息对话框小例子
文章链接：http://www.xdbcb8.com/archives/293.html
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication

from Ui_ui_messagebox import Ui_Dialog


class Dialog_msgbox(QDialog, Ui_Dialog):
    """
    消息对话框
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(Dialog_msgbox, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_about_clicked(self):
        """
        Qt的消息对话框
        """
        QMessageBox.aboutQt(self, '关于Qt')
    
    @pyqtSlot()
    def on_pushButton_question_clicked(self):
        """
        询问消息对话框
        """
        reply = QMessageBox.question(self, '询问', '这是选择题哦?默认值是No', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No )
        if reply == QMessageBox.Yes:
            self.label.setText('你选择了Yes')
        elif reply == QMessageBox.No:
            self.label.setText('你选择了No') 
        else:
            self.label.setText('你选择了Cancel') 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = Dialog_msgbox()
    Dialog.show()
    sys.exit(app.exec_())

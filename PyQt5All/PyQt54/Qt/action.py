# -*- coding: utf-8 -*-

"""
这是用Eric完成猜数字程序
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from Ui_Ui_guess_number import Ui_MainWindow
from random import randint

class Action(QMainWindow, Ui_MainWindow):
    """
    完成猜数字程序
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Action, self).__init__(parent)
        self.setupUi(self)
        self.num = randint(1,100)
        self.show()
    
    def closeEvent(self, event):
        '''
        关闭窗口时让人确认一下
        '''    
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()#回答Yes，同意关闭
        else:
            event.ignore()#其他，不同意关闭
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        执行看猜数字大小
        """
        guessnumber = int(self.lineEdit.text())#获得填写的数字

        if guessnumber > self.num:
            QMessageBox.about(self, '看结果','猜大了!')
            self.lineEdit.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果','猜小了!')
            self.lineEdit.setFocus()
        else:
            QMessageBox.about(self, '看结果','答对了!进入下一轮!')
            self.num = randint(1,100)
            self.lineEdit.clear()
            self.lineEdit.setFocus()
            
if __name__ == "__main__":

    app = QApplication(sys.argv)
    action = Action()
    sys.exit(app.exec_())

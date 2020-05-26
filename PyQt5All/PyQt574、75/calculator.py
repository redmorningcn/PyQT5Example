# -*- coding: utf-8 -*-

"""
这是一个关于PyQt5程序打包的小例子
文章链接：http://www.xdbcb8.com/archives/1434.html
文章链接：http://www.xdbcb8.com/archives/1439.html
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from Ui_calculator_ui import Ui_Dialog

class Calculator(QDialog, Ui_Dialog):

    '''
    计算器
    '''

    def __init__(self, parent=None):

        super(Calculator, self).__init__(parent)
        self.setupUi(self)
        self.lcdstring = ''
        # lcd显示
        self.operation = ''
        # 操作符
        self.currentNum = 0
        # 当前数
        self.previousNum = 0
        # 前一个数
        self.result = 0
        # 结果
        
    @pyqtSlot()
    def on_b0_clicked(self):
        '''
        0
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b1_clicked(self):
        '''
        1
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b2_clicked(self):
        '''
        2
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b3_clicked(self):
        '''
        3
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b4_clicked(self):
        '''
        4
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b5_clicked(self):
        '''
        5
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b6_clicked(self):
        '''
        6
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b7_clicked(self):
        '''
        7
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b8_clicked(self):
        '''
        8
        '''
        self.buttonClicked()
    
    @pyqtSlot()
    def on_b9_clicked(self):
        '''
        9
        '''
        self.buttonClicked()
        
    @pyqtSlot()
    def on_point_clicked(self):
        '''
        .
        '''
        self.buttonClicked()
        
    @pyqtSlot()
    def on_b_plus_clicked(self):
        '''
        +
        '''
        self.opClicked()
        
    @pyqtSlot()
    def on_b_sub_clicked(self):
        '''
        -
        '''
        self.opClicked()
    
    @pyqtSlot()
    def on_b_mul_clicked(self):
        '''
        *
        '''
        self.opClicked()
    
    @pyqtSlot()
    def on_b_div_clicked(self):
        '''
        /
        '''
        self.opClicked()
        
    @pyqtSlot()
    def on_b_eq_clicked(self):
        '''
        =
        '''
        self.eqClicked()
        
    @pyqtSlot()
    def on_b_clear_clicked(self):
        '''
        清除
        '''
        self.clrClicked()
        
    def buttonClicked(self):
        '''
        点数字
        '''
        if len(self.lcdstring) <= 7:
            self.lcdstring = self.lcdstring + self.sender().text()
            if self.lcdstring == '.':
                self.lcdstring = '0.'#.表示0.
            else:
                if str(self.lcdstring).count('.') > 1:
                    self.lcdstring = str(self.lcdstring)[:-1]
                    # 处理多个.的情况
                else:
                    self.lcd.display(self.lcdstring)
                    self.currentNum = float(self.lcdstring)
        else:
            pass

    def opClicked(self):
        '''
        操作符
        '''
        self.previousNum = self.currentNum
        self.currentNum = 0
        self.lcdstring = ''
        self.operation = self.sender().objectName()

    def clrClicked(self):
        '''
        全部清零
        '''
        self.lcdstring = ''
        self.currentNum = 0
        self.previousNum = 0
        self.lcd.display(0)
    
    def eqClicked(self):
        '''
        等于
        '''
        if self.operation == 'b_plus':
            # 加法
            self.result = self.previousNum + self.currentNum
            self.lcd.display(self.result)
        
        elif self.operation == 'b_sub':
            # 减法
            self.result = self.previousNum - self.currentNum
            self.lcd.display(self.result)
            
        elif self.operation == 'b_mul':
            # 乘法
            self.result = self.previousNum * self.currentNum  
            self.lcd.display(self.result)  
    
        elif self.operation == 'b_div':
            # 除法
            if self.currentNum == 0:
                self.lcd.display('Error')  
                self.result = 0
                self.previousNum = 0
                # 除数不能为0
            else:
                self.result = self.previousNum / self.currentNum
                self.lcd.display(self.result)
        
        self.currentNum = self.result
        self.lcdstring = ''
    
    def closeEvent(self, event):
        '''
        监测关闭
        '''
        reply = QMessageBox.question(self, '警告', '确认退出', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mycal = Calculator()
    mycal.show()
    sys.exit(app.exec_())

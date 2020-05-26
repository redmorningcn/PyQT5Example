#coding=utf-8

'''
这是一个我们拖动滑块或者拨号器（我自己取得名字）相关数字会在LCD上显示的例子。
文章链接：http://www.xdbcb8.com/archives/190.html
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QDial, QApplication, QSlider)

class Example(QWidget):

    '''
    拖动滑块或者拨号器响应
    '''

    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUi()
    
    def initUi(self):
        '''
        界面初始设置
        '''
        lcd = QLCDNumber(self)
        # dial = QDial(self)
        sld = QSlider(Qt.Horizontal, self)#滑块式水平放置的

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')
        
        lcd.setGeometry(100, 50, 150, 60)
        # dial.setGeometry(120, 120, 100, 100)
        sld.setGeometry(120, 120, 90, 50)
        
        # dial.valueChanged.connect(lcd.display)
        sld.valueChanged.connect(lcd.display)
        #拖动后数值直接在LCD上显示出来
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())































# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    # QVBoxLayout, QApplication)


# class Example(QWidget):
    
    # def __init__(self):
        # super().__init__()
        
        # self.initUI()
        
        
    # def initUI(self):
        
        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)

        # vbox = QVBoxLayout()
        # vbox.addWidget(lcd)
        # vbox.addWidget(sld)

        # self.setLayout(vbox)
        # sld.valueChanged.connect(lcd.display)
        
        # self.setGeometry(300, 300, 250, 150)
        # self.setWindowTitle('Signal and slot')
        # self.show()
        

# if __name__ == '__main__':
    
    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())
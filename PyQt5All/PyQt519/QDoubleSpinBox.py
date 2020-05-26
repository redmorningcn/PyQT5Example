#coding=utf-8

'''
这是一个关于微调框的小例子（第二种情况：浮点数）！
文章链接：http://www.xdbcb8.com/archives/432.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDoubleSpinBox, QLabel, QSlider
# QDoubleSpinBox会舍去数字，以便以当前精度显示。在QDoubleSpinBox小数设置为2，调用setValue(2.555)将导致value()返回2.56。
from PyQt5.QtCore import Qt
        
class Example(QWidget):
    '''
    微调框浮点型
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
        self.resize(370, 190)
        self.setWindowTitle('关注微信公众号：学点编程吧--小数微调框')
        
        self.sp = QDoubleSpinBox(self)
        self.sp.setGeometry(10, 50, 100, 20)
        self.sp.setRange(0, 20)
        self.sp.setSingleStep(0.1)
        
        self.lb = QLabel("QDoubleSpinBox精度设置为：2", self)
        self.lb.move(120, 50)

        self.sl = QSlider(Qt.Vertical, self)
        self.sl.setGeometry(300, 30, 30, 100)
        self.sl.setRange(0, 9)# 我们给微调框精度设置最该为9
        self.sl.setValue(0)
        self.sl.setTickPosition(QSlider.TicksBelow)# 滑块设置为标尺型
        
        self.sl.valueChanged.connect(self.spinbox_changevalue)
        self.show()
        
    def spinbox_changevalue(self, value):
        '''
        精度变更时显示
        '''
        if value <= 7:
            self.lb.setText("QDoubleSpinBox精度设置为:" + str(value+2))
            self.sp.setDecimals(value+2)# 更改精度

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#coding=utf-8

'''
这是一个关于微调框的小例子（第一种情况：整型）！
文章链接：http://www.xdbcb8.com/archives/426.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QSlider, QLabel, QMessageBox
from PyQt5.QtCore import QRegExp, Qt

class HolyShitBox(QSpinBox):
    '''
    自定义微调框
    ''' 
    def valueFromText(self, strings):
        regExp = QRegExp("(\\d+)(\\s*[xx]\\s*\\d+)?")
        # 正则表达式的对象：\s 匹配任意的空白符，\d 匹配数字 ，\\表示转义\
        
        if regExp.exactMatch(strings):
            return int(regExp.cap(1))
            # cap()匹配的元素的顺序如下。第一个元素cap(0)是整个匹配的字符串。cap(1)是第一个捕获括号的文本。
        return 0
            
    def textFromValue(self, num):
        return "{0} x {1}".format(num, num)
        # 重写textFromValue()函数，显示成“数字 x 数字”的形式
        
class Example(QWidget):
    '''
    整型微调框
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
        self.resize(350, 280)
        self.setWindowTitle('关注微信公众号：学点编程吧--微调框')
        
        lb1 = QLabel('普通微调框', self)
        lb2 = QLabel('加强微调框', self)
        lb3 = QLabel('超神微调框', self)
        
        self.sp1 = QSpinBox(self)
        self.sp2 = QSpinBox(self)
        self.sp3 = HolyShitBox(self)# 自定义微调框的使用
        
        self.sl = QSlider(Qt.Horizontal, self)
        # self.sl = QSlider(Qt.Vertical, self)
        # 可以试试垂直滑块
        
        self.sp1.move(130, 30)
        self.sp2.move(130, 70)
        self.sp3.move(130, 100)
        
        lb1.move(30, 32)
        lb2.move(30, 70)
        lb3.move(30, 100)
        
        self.sl.move(30, 150)
        
        self.sp1.setRange(-10, 200)
        self.sp1.setSingleStep(10)
        self.sp1.setWrapping(True)# 循环行为
        self.sp1.setValue(-10)
        
        self.sp2.setRange(0, 100)# 范围0-100
        self.sp2.setSingleStep(10)# 步长为10
        self.sp2.setValue(10)
        self.sp2.setPrefix("我的帅达到 ")# 微调框的前缀
        self.sp2.setSuffix(" %，正在充帅中...")# 微调框的后缀
        self.sp2.setSpecialValueText('我的帅达到渣的一逼')# 当前值等于minimum()时，微调框将显示该文本而不是数字值
        
        self.sp3.setRange(10, 50)
        self.sp3.setValue(10)
        self.sp3.setWrapping(True)
        
        self.sl.setRange(-10, 200)
        self.sl.setValue(-10)
        
        self.sp1.valueChanged.connect(self.slider1_changevalue)
        self.sp2.valueChanged.connect(self.slider2_changevalue)
        self.sl.valueChanged.connect(self.spinbox_changevalue)
        # 微调框的数值变化时发出的信号

        self.show()

    def slider1_changevalue(self, value):
        '''
        sp1变化时连接该槽函数
        '''
        self.sl.setValue(value)

    def slider2_changevalue(self, value):
        '''
        sp2变化时连接该槽函数
        '''
        if self.sp2.value() == self.sp2.maximum():
            QMessageBox.information(self, '提示', '你怎么还再充帅，你不知道你的帅已经引起了别人的嫉妒吗？')
            self.sp2.setSuffix(" %,我踏马太帅了！！")# sp2变化最大化时弹出信息，后缀也要变化。
        elif self.sp2.minimum() < self.sp2.value() < self.sp2.maximum():
            self.sp2.setSuffix(" %，正在充帅中...")# sp2数值在最大化与最小化之间时的后缀。

    def spinbox_changevalue(self, value):
        '''
        sp2变化时连接该槽函数
        '''
        self.sp1.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#coding=utf-8

'''
这是一个关于液晶显示屏的小例子！
文章链接：http://www.xdbcb8.com/archives/458.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QDateTime, QDate, QTime
from PyQt5.QtGui import QFont

class Example(QWidget):
    '''
    液晶显示屏
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
        self.setWindowTitle('关注微信公众号：学点编程吧--倒计时：LCD数字')

        self.lcd = QLCDNumber(self)
        lb = QLabel("距离2022年北京-张家口冬季奥林匹克运动会还有", self)
        ft = QFont()
        ft.setPointSize(15)
        lb.setFont(ft)
        vbox = QVBoxLayout(self)
        vbox.addWidget(lb)
        vbox.addWidget(self.lcd)

        self.lcd.setDigitCount(12)# 将新建的QLCDNumber对象设置为12位
        self.lcd.setMode(QLCDNumber.Dec)# 显示模式十进制（默认）
        self.lcd.setStyleSheet("border: 2px solid black; color: red; background: silver;")
        # Lcd样式设置

        time = QTimer(self)
        time.setInterval(1000)# 固定1s发出timeout信号
        time.timeout.connect(self.refresh)
        time.start()

        self.show()

    def refresh(self):
        '''
        当时间每隔1s，LCD上信息会刷新一下的。
        '''
        startDate = QDateTime.currentMSecsSinceEpoch()
        # 将其转换成当前时间到1970-01-01T00：00：00世界协调时间以来的毫秒数

        endDate = QDateTime(QDate(2022, 2, 4), QTime(0, 0, 0)).toMSecsSinceEpoch()
        # 返回2020年2月4日0:0:0自1970-01-01T00：00：00.000世界协调时间以来的毫秒数

        interval = endDate - startDate
        # 距离冬奥会还有多少时间

        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec)
            intervals = "1000:0.00"
            self.lcd.display(intervals)
            # 时间间隔转换成天数、小时数、分钟数、秒数并显示在LCD上

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

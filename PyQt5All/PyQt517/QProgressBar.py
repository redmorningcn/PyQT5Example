#coding=utf-8

'''
这是一个关于进度条的小例子！
文章链接：http://www.xdbcb8.com/archives/410.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QBasicTimer

class Example(QWidget):
    '''
    进度条
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
        self.resize(600, 480)
        self.setWindowTitle('关注微信公众号：学点编程吧--跑马灯（进度条）')

        self.pb11 = QProgressBar(self)
        self.pb12 = QProgressBar(self)
        self.pb13 = QProgressBar(self)
        self.pb14 = QProgressBar(self)
        self.pb21 = QProgressBar(self)
        self.pb22 = QProgressBar(self)
        
        self.pb11.setOrientation(Qt.Horizontal)
        self.pb12.setOrientation(Qt.Vertical)
        self.pb13.setOrientation(Qt.Horizontal)
        self.pb14.setOrientation(Qt.Vertical)
        # pb11、pb13时水平放置的进度条，其余的时垂直放置的进度条
        
        self.pb11.setGeometry(70, 40, 450, 20)
        self.pb12.setGeometry(490, 40, 20, 400)
        self.pb13.setGeometry(70, 420, 450, 20)
        self.pb14.setGeometry(70, 40, 20, 400)

        self.pb21.setGeometry(200, 100, 200, 20)
        self.pb22.setGeometry(200, 340, 200, 20)
        
        self.pb21.setFormat("%v")
        # ％p - 被完成的百分比取代
        # ％v - 被当前值替换
        # ％m - 被总step所取代

        self.pb22.setInvertedAppearance(True)
        # 进度条从右到左（水平进度条）
        
        self.b1 = QPushButton('外圈跑马灯', self)
        self.b2 = QPushButton('内圈跑进度', self)
        
        self.b1.move(250, 180)
        self.b2.move(250, 250)
        
        self.show()
        
        self.timer = QBasicTimer()
        # QBasicTimer类为对象提供计时器事件。
        # 这是Qt内部使用的一个快速，轻量级和低级别的类。注意这个定时器是一个重复的定时器，除非调用stop()函数，否则它将发送后续的定时器事件。
        # 当定时器超时时，它将向QObject子类发送一个timer事件。定时器可以随时stop()。

        self.step = 0
        
        self.b1.clicked.connect(self.running)
        self.b2.clicked.connect(self.doaction)
        
    def timerEvent(self, e):
        '''
        对计时器事件作出反应，重写事件处理程序
        '''
        if self.step >= 100:
            self.timer.stop()
            QMessageBox.information(self,'提示','内圈收工了!')
            self.b2.setText('再来一次')
            self.step = 0
            return

        self.step = self.step + 1
        # 步长自加1
        self.pb21.setValue(self.step)
        self.pb22.setValue(self.step)

    def doaction(self):
        '''
        启动和停止定时器
        '''
        if self.timer.isActive():
            # isActive()如果定时器正在运行且尚未停止，则返回True；否则返回False。
            self.timer.stop()# 定时器停止
            self.b2.setText('继续')
        else:
            self.timer.start(100, self)# 定时器开始
            self.b2.setText('停止')
        
    def running(self):
        '''
        最小值和最大值都设置为0，那么栏会显示一个繁忙的指示符！
        '''
        self.pb11.setMinimum(0)
        self.pb11.setMaximum(0)
        self.pb12.setInvertedAppearance(True)
        # 进度条从右到左（水平进度条）
        self.pb12.setMinimum(0)
        self.pb12.setMaximum(0)
        self.pb13.setInvertedAppearance(True)
        # 进度条从右到左（水平进度条）
        self.pb13.setMinimum(0)
        self.pb13.setMaximum(0)
        self.pb14.setMinimum(0)
        self.pb14.setMaximum(0)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
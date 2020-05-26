# -*- coding: utf-8 -*-

"""
一个关于QTimer与QThread的综合应用举例的小例子！
文章链接：http://www.xdbcb8.com/archives/867.html
文章链接：http://www.xdbcb8.com/archives/870.html
文章链接：http://www.xdbcb8.com/archives/872.html
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QMovie, QPixmap
from Ui_main import Ui_Form
from msgold import MsgGold
from digging import Ore

class Digging_Thread(QThread):
    '''
    多线程挖矿
    '''
    gold_finish = pyqtSignal(int)
    # 自定义了一个信号gold_finish，这个信号带int类型参数的，主要是挖矿结束后将金矿数量返回的。

    def __init__(self, sec):
        '''
        一些初始设置
        '''
        super().__init__()
        self.sec = sec

    def run(self):
        '''
        挖矿
        '''
        ore = Ore(self.sec)
        goldcnt = ore.begin_dig()
        self.gold_finish.emit(goldcnt)
        # 操作完成后发射gold_finish信号，将金矿数量发射出去。

    def __del__(self):
        self.wait()
        # 当析构多线程对象的时候，会等待我们的多线程完成任务。

class Gold(QWidget, Ui_Form):
    """
    挖矿中
    """
    def __init__(self, parent=None):
        '''
        一些初始设置
        '''
        super(Gold, self).__init__(parent)
        self.setupUi(self)
        self.value = 0
        # 进度条的当前进度

        self.second = 0
        # 挖矿的时间

        self.movie = QMovie("./res/farmer.gif")
        # QMovie对象

        self.goldNum = 0
        # 金矿数量


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        开始挖矿
        """
        self.goldNum = 0
        # 每次开始挖矿，金矿的数量需要清零

        self.second = self.spinBox.value()
        # 调节挖矿的时间

        self.pushButton.setEnabled(False)
        self.spinBox.setEnabled(False)
        # 挖矿的时候时间是不能调的哦

        self.farm(1)
        # 动画启动

        self.progressBar.setMaximum(100)
        # 进度调最大值为100

        self.timer = QTimer()
        self.timer.start(self.second * 10)
        # 时间隔（self.second * 10）毫秒启动或重新启动计时器

        self.timer.timeout.connect(self.showProgress)
        # 时间间隔超时会调动进度显示

        self.dig = Digging_Thread(self.second)
        self.dig.gold_finish.connect(self.showResult)
        self.dig.start()
        #挖矿咯

    def showProgress(self):
        '''
        进度每时每刻都在增加中
        '''
        self.value += 1
        self.progressBar.setValue(self.value)
        if self.value == 100:
        # 当值增加到100的时候，按钮和微调框都重新启用，value的值重新清零。
            self.pushButton.setEnabled(True)
            self.spinBox.setEnabled(True)
            self.value = 0

            self.timer.stop()
            del self.timer
            # 定时器停止工作，删除定时器对象。

            self.dig.quit()
            del self.dig
            # 多线程退出，并删除多线程对象。

            self.farm(0)
            msgBox = MsgGold(self.goldNum)
            msgBox.exec()
            self.progressBar.setValue(0)
            self.label_farmer.setPixmap(QPixmap("./res/ready.png"))
            # 农民挖矿的动画停止，弹出结果挖矿结果对话框。进度条结果清零，农民挖矿的动画变成准备挖矿的图片。

    def showResult(self, r):
        '''
        把挖矿的结果赋值给变量
        '''
        self.goldNum = r

    def farm(self, flag):
        '''
        flag = 1的时候，QLabel的gif动画开始播放；flag = 0的时候，gif动画停止播放。
        '''
        if flag == 1:
            self.label_farmer.setMovie(self.movie)
            self.movie.start()
        if flag == 0:
            self.movie.stop()
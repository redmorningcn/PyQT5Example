# -*- coding: utf-8 -*-

"""
这是一个关于美元对人民币汇率K线图的小例子！
文章链接：http://www.xdbcb8.com/archives/1655.html
文章链接：http://www.xdbcb8.com/archives/1675.html
文章链接：http://www.xdbcb8.com/archives/1698.html
"""

import sys
import pandas
import pyqtgraph as pg
from PyQt5.QtGui import QPicture, QPainter
from PyQt5.QtCore import pyqtSlot, QRect, QPointF, QRectF
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_ui import Ui_MainWindow

class DrawChart():
    '''
    画图哦
    '''
    def __init__(self):
        self.data_list, self.t = self.getData()

    def pyqtgraphDrawChart(self):
        '''
        画K线
        '''
        try:
            self.item = CandlestickItem(self.data_list)
            # K线图
            self.xdict = {0: self.data_list[0][1], int((self.t + 1) / 2) - 1: self.data_list[int((self.t + 1) / 2) - 1][1], self.t - 1: self.data_list[-1][1]}
            # 我们定义的坐标
            self.stringaxis = pg.AxisItem(orientation='bottom')
            # pg.AxisItem显示带有刻度，值和标签的单个绘图轴
            self.stringaxis.setTicks([self.xdict.items()])
            # setTicks()明确确定要显示的刻度
            self.plt = pg.PlotWidget(axisItems={'bottom': self.stringaxis}, enableMenu=False)
            # self.plt是我们创建的显示K线图的和坐标刻度的小部件
            self.plt.addItem(self.item)
            # 把K线图加上
            return self.plt
        except:
            return pg.PlotWidget()

    def getData(self):
        '''
        获取外汇数据
        '''
        self.exr_data = pandas.read_csv("rmb.csv").sort_index(ascending=False)
        # pandas读取csv文件（倒序）
        data_list = []
        t = 0
        # 序号
        for index, row in self.exr_data.iterrows():
            date, close, open, high, low, price_change = row
            datas = (t, date, close, open, high, low, price_change)
            data_list.append(datas)
            t = t + 1
        # 把相关的信息连同序号t一起放入datas元组中，再把这个元组放入data_list这个列表中
        return data_list, t

class CandlestickItem(pg.GraphicsObject):
    '''
    K线图，自定义CandlestickItem类，这个类继承了pyqtgraph.GraphicsObject
    '''
    def __init__(self, data):
        '''
        一些初始设置
        '''
        pg.GraphicsObject.__init__(self)
        self.data = data
        # 变量data表示我们需要带入的数据
        
        self.generatePicture()

    def generatePicture(self):
        '''
        每个小的K线
        '''
        self.picture = QPicture()
        p = QPainter(self.picture)
        p.setPen(pg.mkPen('w'))# 白色
        w = (self.data[1][0] - self.data[0][0]) / 3.# 每个K线的宽度
        for (t, date, close, open, high, low, price_change) in self.data:
            # t：每个汇率数据的序号
            # date：日期
            # close：收盘价
            # open：开盘价
            # high：最高价
            # low：最低价
            # price_change：价格变化
            if open > close:
                p.setPen(pg.mkPen('g'))
                p.setBrush(pg.mkBrush('g'))
            else:
                p.setPen(pg.mkPen('r'))
                p.setBrush(pg.mkBrush('r'))
            # 如果收盘价高于开盘价，我们就用红色；如果收盘价低于开盘价，我们就用绿色
            if low != high:
                p.drawLine(QPointF(t, low), QPointF(t, high))
                # 当最高价和最低价不相同时，我们就画一条线，两点坐标是从最低价到最高价。
            p.drawRect(QRectF(t - w, open, w * 2, close - open))
            # 画出具体的收盘价、开盘价矩形图。这里注意下：要是close - open，矩形的方向是不一样的
        p.end()

    def paint(self, p, *args):
        '''
        绘图
        '''
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        '''
        所有绘画必须限制在图元的边界矩形内
        '''
        return QRectF(self.picture.boundingRect())

class ExchangeRate(QMainWindow, Ui_MainWindow):
    """
    外汇汇率展示
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(ExchangeRate, self).__init__(parent)
        self.setupUi(self)
        self.InitUi()

    def InitUi(self):
        '''
        一些界面设置
        '''
        self.splitter.setStretchFactor(0, 4)
        self.splitter.setStretchFactor(1, 6)
        pg.setConfigOption('background', '#f0f0f0')
        # 设置背景色

        self.drawChart = DrawChart()
        self.exrwidget = self.drawChart.pyqtgraphDrawChart()
        self.verticalLayout.addWidget(self.exrwidget)
        # 将生成的pyqtgraph小部件放入到PyQt5的布局中

        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.exrwidget.addItem(self.vLine, ignoreBounds=True)
        self.exrwidget.addItem(self.hLine, ignoreBounds=True)
        # 增加x轴、y轴方向上的线

        self.exrwidget.scene().sigMouseMoved.connect(self.mouseMoved)
        # 处理鼠标移动时，线也要跟着移动，此时的信号是sigMouseMoved

    def mouseMoved(self, pos):
        '''
        处理鼠标事件
        '''
        vb = self.exrwidget.plotItem.vb
        # vb这里指的是ViewBox，允许通过鼠标拖动对其进行内部缩放/平移的框。
        # 此类通常作为PlotItem或Canvas的一部分或使用GraphicsLayout.addViewBox()自动创建。

        if self.exrwidget.sceneBoundingRect().contains(pos):
            mousePoint = vb.mapSceneToView(pos)
            index = int(mousePoint.x()+1/3.)
            # 鼠标坐标在范围内，我们要把这个坐标转换成每一天的行情index

            if index >= 0 and index < len(self.drawChart.data_list):
                # index的范围在0到全部的汇率数据行上。
                # 把汇率数据转换到qlabel，即显示出这一天汇率行情的全部信息。
                date, close, open, high, low, price_change = self.drawChart.data_list[index][1::]
                self.label_date_c.setText(date)
                self.label_close_c.setText(str(close))
                self.label_open_c.setText(str(open))
                self.label_high_c.setText(str(high))
                self.label_low_c.setText(str(low))
                self.label_change_c.setText(price_change)

                if price_change[0] == "-":
                    self.label_change_c.setStyleSheet("color:green")
                elif price_change == "0.00%":
                    self.label_change_c.setStyleSheet("color:black")
                else:
                    self.label_change_c.setStyleSheet("color:red")
                # 对汇率变化的label对象，我们根据具体的变化多少设置样式，正值红色，负值绿色，其它为黑色

                self.vLine.setPos(mousePoint.x())
                self.hLine.setPos(mousePoint.y())
                # 鼠标上垂直和水平的线

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exrate= ExchangeRate()
    exrate.show()
    sys.exit(app.exec_())

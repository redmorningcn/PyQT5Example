# -*- coding: utf-8 -*-

"""
这是一个今天几度了（QTabWidget的使用）的例子！
文章链接：http://www.xdbcb8.com/archives/827.html
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from Ui_main import Ui_Form
from showtab import showTab
from realtimeweather import RealTimeWeather
from getweather import GetWeatherInfo

class Weather(QWidget, Ui_Form):
    """
    获取天气主界面
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(Weather, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.flag = 0
        # flag为0，表示默认是查询实时天气
    
    def initUi(self):
        '''
        还是一些初始设置
        '''
        cities = ["北京", "上海", "广州"]
        self.comboBox.addItems(cities)#把可以查询的城市放到下拉框中
        self.showrealweather()

    @pyqtSlot(bool)
    def on_radioButton_toggled(self, checked):
        """
        实时天气
        """
        self.flag = 0
    
    @pyqtSlot(bool)
    def on_radioButton_2_toggled(self, checked):
        """
        近3天天气
        """
        self.flag = 1
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        查询天气：根据查询天气的种类，在选项卡上展示页面。实时天气就展示一个，近三天天气就展示3个
        """
        if self.flag == 0:
            self.showrealweather() 
        else:
            t0, t1, t2, d0, d1, d2 = self.showeather()
            self.tabWidget.addTab(t0, d0)
            self.tabWidget.addTab(t1, d1)
            self.tabWidget.addTab(t2, d2)

    def showrealweather(self):
            city = self.comboBox.currentText()
            ww = GetWeatherInfo(0, city)
            weather, weather_code, weather_temperature, last_update = ww.getweather()
            # 取得该城市的天气信息：天气状况、天气状况代码、当前温度、最新的更新时间

            msg = RealTimeWeather()
            # 实时天气信息

            msg.label_tt.setText(weather)
            msg.label_ww.setText(weather_temperature)
            msg.label_icon.setPixmap(QPixmap("./res/" + weather_code + ".png"))
            update = "天气最新更新时间--" + last_update[11:16]
            # 只取更新时间的具体时间（几点几分），否则还有某年某月等内容

            self.tabWidget.clear()
            # 之前有选项卡的清空

            self.tabWidget.addTab(msg, update)
            # 新增一个选项卡，选项卡的内容就是之前展示实时天气的QWidget子类，名称就是最新更新时间

    def showeather(self):
        '''
        近三天天气查询，和实时天气查询差不多。
        '''
        city = self.comboBox.currentText()
        ww = GetWeatherInfo(1, city)
        self.tabWidget.clear()
        weather0, weather1, weather2 = ww.getweather()
        tabwidget0 = showTab()
        tabwidget0.label_wb.setText(weather0["text_day"])
        tabwidget0.label_tb.setPixmap(QPixmap("./res/" + weather0["code_day"] + ".png"))
        tabwidget0.label_wn.setText(weather0["text_night"])
        tabwidget0.label_tw.setPixmap(QPixmap("./res/" + weather0["code_night"] + ".png"))
        tabwidget0.label_tg.setText(weather0["high"])
        tabwidget0.label_tl.setText(weather0["low"])
        tabwidget0.label_fx.setText(weather0["wind_direction"])
        tabwidget0.label_fl.setText(weather0["wind_scale"])

        tabwidget1 = showTab()
        tabwidget1.label_wb.setText(weather1["text_day"])
        tabwidget1.label_tb.setPixmap(QPixmap("./res/" + weather1["code_day"] + ".png"))
        tabwidget1.label_wn.setText(weather1["text_night"])
        tabwidget1.label_tw.setPixmap(QPixmap("./res/" + weather1["code_night"] + ".png"))
        tabwidget1.label_tg.setText(weather1["high"])
        tabwidget1.label_tl.setText(weather1["low"])
        tabwidget1.label_fx.setText(weather1["wind_direction"])
        tabwidget1.label_fl.setText(weather1["wind_scale"])

        tabwidget2 = showTab()
        tabwidget2.label_wb.setText(weather2["text_day"])
        tabwidget2.label_tb.setPixmap(QPixmap("./res/" + weather2["code_day"] + ".png"))
        tabwidget2.label_wn.setText(weather2["text_night"])
        tabwidget2.label_tw.setPixmap(QPixmap("./res/" + weather2["code_night"] + ".png"))
        tabwidget2.label_tg.setText(weather2["high"])
        tabwidget2.label_tl.setText(weather2["low"])
        tabwidget2.label_fx.setText(weather2["wind_direction"])
        tabwidget2.label_fl.setText(weather2["wind_scale"])

        return tabwidget0, tabwidget1, tabwidget2, weather0["date"], weather1["date"], weather2["date"]
        # 返回近三天天气信息

if __name__ == "__main__":
    app = QApplication(sys.argv)
    we = Weather()
    we.show()
    sys.exit(app.exec_())

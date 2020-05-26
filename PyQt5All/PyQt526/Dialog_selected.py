# -*- coding: utf-8 -*-

"""
这是一个关于日历（QCalendarWidget）的小例子！
文章链接：http://www.xdbcb8.com/archives/590.html
"""

import sys
import json
import requests
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from Ui_ui import Ui_Dialog

class Dialog_selected(QDialog, Ui_Dialog):
    """
    根据日历选中一个黄道吉日
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(Dialog_selected, self).__init__(parent)
        self.setupUi(self)
        self.appkey = "你的appkey"# 调用API要用
    
    @pyqtSlot(QDate)
    def on_calendarWidget_clicked(self, date):
        """
        选中日期看日子
        """
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd dddd")
        # 把选中的日期转换成"yyyy-MM-dd dddd"样式

        self.request1(self.appkey, date)# 获取黄历信息
    
    def request1(self, appkey, date):
        '''
        获得具体的黄历信息
        '''
        url = "http://v.juhe.cn/laohuangli/d"

        params = {
            "key" : appkey, # 应用APPKEY(应用详细页查询)
            "date" : date # 日期，格式2014-09-09
        }

        f = requests.get(url, params=params)

        content = f.text

        res = json.loads(content)# 转换成json格式
        if res:
            error_code = res["error_code"]
            data = res["result"]
            if error_code == 0:
                # 成功请求
                self.label.setText("阳历：" + date)
                self.label_2.setText("阴历：" + data["yinli"])
                self.label_3.setText("忌：" + data["ji"])
                self.label_4.setText("宜：" + data["yi"])
            else:# 请求失败
                QMessageBox.Warning(self, "警告", "错误代码:" + res["error_code"] + "错误原因:" + res["reason"])
        else:# 哦嚯，失败了
            QMessageBox.Warning(self, "警告", "API请求失败")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    Dialog = Dialog_selected()
    Dialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

"""
这是一个关于抖音视频下载的小例子！
文章链接：http://www.xdbcb8.com/archives/1801.html
文章链接：http://www.xdbcb8.com/archives/1808.html
文章链接：http://www.xdbcb8.com/archives/1821.html
文章链接：http://www.xdbcb8.com/archives/1823.html
"""

import random
import sys
import time
import re
import requests
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog
from Ui_ui import Ui_Form

class Down(QThread):
    '''
    多线程下载视频
    '''
    parsesignal = pyqtSignal(str)
    #解析视频信号

    downsignal = pyqtSignal(list)
    #下载视频信号

    def __init__(self, url, savefile):
        '''
        一些初始设置
        '''
        super().__init__()
        self.shareUrl = url
        self.savefile = savefile
        
    def run(self):
        '''
        下载咯
        '''
        resParse = self.ParsingVideo()
        if resParse != "parse error":
            self.downLoadVideo()
            #解析不错才下载啊
            
    def ParsingVideo(self):
        '''
        解析视频
        '''
        userAgent = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"]
        key = random.randint(0,3)
        # 随机选一个ua

        headers = {'content-type': 'application/json', 'User-Agent': userAgent[key]}
        try:
            res1 = requests.head(self.shareUrl, headers=headers, allow_redirects=False)
            self.cookies = res1.cookies
            redirecturl1 = res1.headers["Location"]
            # 取得第一次Location地址
            res2 = requests.get(redirecturl1, headers=headers, cookies=self.cookies)
            playUrl = re.findall(r"playAddr: (.*?),", res2.text, re.S)[0][1:-1]
            # 使用正则表达式拿到下一次跳转前的url
            res3 = requests.head(playUrl, headers=headers, allow_redirects=False, cookies=self.cookies)
            self.downloadUrl = res3.headers["Location"]
            # 取得第二次Location
        except:
            self.downloadUrl = "parse error"
        self.parsesignal.emit(self.downloadUrl)
        # 发射下载的url
        return self.downloadUrl

    def downLoadVideo(self):
        '''
        下载视频
        '''
        r = requests.get(self.downloadUrl, stream=True, cookies=self.cookies)
        length = float(r.headers['content-length'])
        count = 0
        time1 = time.clock()

        with open(self.savefile, 'wb') as f:
            # 下载视频了
            for chunk in r.iter_content(chunk_size = 512):
                if chunk:
                    f.write(chunk)
                    count += len(chunk)
                    p = count / length * 100
                    # 完成进度
                    intervals = time.clock() - time1
                    speed = count / 1024 / 1024 / intervals
                    # 下载速度
                    self.downsignal.emit([p, speed])
                    
    def __del__(self):
        self.wait()
        # 等等多线程的完成

class DownLoadDouYin(QWidget, Ui_Form):
    """
    下载抖音视频界面
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(DownLoadDouYin, self).__init__(parent)
        self.setupUi(self)
        self.progressBar.valueChanged.connect(self.loadDone)
        self.progressBar.hide()
        # 进度条隐藏先
        self.label_3.hide()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        点击下载
        """
        self.progressBar.setValue(0)
        savefileName = self.savefile()
        if savefileName:
            self.mv = QMovie(":/loading/img/loading.gif")
            self.label_2.setMovie(self.mv)
            self.mv.start()
            # 解析动画
            shareUrl = self.filterUrl(self.lineEdit.text())
            self.parse = Down(shareUrl, savefileName)
            self.parse.parsesignal[str].connect(self.getUrl)
            self.parse.downsignal[list].connect(self.downLoad)
            self.parse.start()

    def getUrl(self, url):
        '''
        获得下载视频
        '''
        if url == "parse error":
            self.mv.stop()
            self.label_2.setText("视频下载地址解析失败！")
            self.label_2.setStyleSheet("color:red")
            # 解析成功后，把出现的文字标成绿色
        else:
            self.mv.stop()
            # gif动画停止
            self.progressBar.show()
            self.label_3.show()
            self.label_2.setText("视频下载地址解析成功！")
            self.label_2.setStyleSheet("color:green")
            # 解析失败的话就标成红色

    def downLoad(self, reslit):
        '''
        下载视频
        '''
        p = round(reslit[0], 2) * 100
        speed = round(reslit[1], 2)
        downLoadInfo = "平均下载速度:{}MB/s".format(speed)
        # 下载信息
        self.label_2.setText(downLoadInfo)
        self.progressBar.setValue(p)
            
    def savefile(self):
        '''
        获得保存文件名
        '''
        fileName = QFileDialog.getSaveFileName(self, "学点编程吧:保存文件", "./", "mp4 files (*.mp4)")[0]
        return fileName

    def loadDone(self, value):
        '''
        下载完成
        '''
        if value == self.progressBar.maximum():
            QMessageBox.information(self, "提示", "下载完成")
            self.progressBar.hide()
            self.label_3.hide()

    def filterUrl(self, url):
        '''
        url去掉空格
        '''
        newUrl = url.replace(" ", "")
        return newUrl

if __name__ == "__main__":
    app = QApplication(sys.argv)
    douyin = DownLoadDouYin()
    douyin.show()
    sys.exit(app.exec_())
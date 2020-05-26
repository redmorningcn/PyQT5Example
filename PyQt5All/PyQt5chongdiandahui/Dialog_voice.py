# -*- coding: utf-8 -*-

"""
这是一个冲顶大会的小例子！
文章链接：http://www.xdbcb8.com/archives/536.html
文章链接：http://www.xdbcb8.com/archives/541.html
文章链接：http://www.xdbcb8.com/archives/549.html
文章链接：http://www.xdbcb8.com/archives/571.html
文章链接：http://www.xdbcb8.com/archives/695.html
"""

import sys
import wave
import datetime
import webbrowser
import urllib.parse
import pyaudio
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication
from Ui_ui import Ui_Dialog
from aip import AipSpeech
#百度的API调用

class Speech_Recognition_Thread(QThread):
    '''
    多线程录音
    '''
    finished_signal = pyqtSignal(str)
    voice_signal = pyqtSignal(dict)
    # 自定义信号

#一大堆参数设置    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    WAVE_OUTPUT_FILENAME = "output.wav"
    APP_ID = '*******'
    API_KEY = '*******'
    SECRET_KEY = '********'
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def __init__(self, v, parent = None):
        super().__init__(parent)
        self.RECORD_SECONDS = v
        # 录音时间

    def get_file_content(self, filePath):
        '''
        读取文件
        '''
        with open(filePath, 'rb') as fp:
            return fp.read()

    def run(self):
        
        p = pyaudio.PyAudio()

        stream = p.open(format = self.FORMAT,
                        channels = self.CHANNELS,
                        rate = self.RATE,
                        input = True,
                        frames_per_buffer = self.CHUNK)
        # format：采样大小和格式。我们这里是pyaudio.paInt16，即16位int型。
        # channels：声道数，这里我们设定的是单声道。
        # rate：采样频率，录音设备在一秒钟内对声音信号的采样次数，采样频率越高声音的还原就越真实越自然。这里是16000。
        #       这里是为了匹配后期语音识别的要求设置的。
        # input：指定这是否是输入流。 默认为False。
        # frames_per_buffer：指定每个缓冲区的帧数。

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)
        # 从流中读取样本并不断的存入帧这个列表中

        stream.stop_stream()
        # 停止流。流停止后，不会调用写入或读取。
        stream.close()
        # 关闭流。
        p.terminate()
        # 终止PortAudio这个Python接口。
        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        # 新建一个”output.wav”的音频文件
        wf.setnchannels(self.CHANNELS)
        # 设置通道数
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        # 将示例宽度设置为n个字节（返回之前我们指定示例格式的大小（以字节为单位））
        wf.setframerate(self.RATE)
        # 设置帧速率。
        wf.writeframes(b''.join(frames))
        # 写入音频帧。这里b''前缀代表的就是bytes。
        wf.close()
        # 关闭音频文件。

        self.finished_signal.emit(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t问题采集完毕！')
        self.finished_signal.emit(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t语音识别中...！')
        
        voice = self.aipSpeech.asr(self.get_file_content('output.wav'), 'wav', 16000, {
            'lan': 'zh',
        })
        # 识别本地文件

        self.voice_signal.emit(voice)

        if voice['err_no'] == 0:
                webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(str(voice['result'])[2:-3]), new=2, autoraise=True)
                #解析没有问题的话就百度一下

class Dialog_voice(QDialog, Ui_Dialog):
    """
    冲顶大会
    """
    def __init__(self, parent=None):
        """
        一些基本设置
        """
        super(Dialog_voice, self).__init__(parent)
        self.setupUi(self)
    
    def _show_message(self, message):
        '''
        显示解析过程
        '''
        if isinstance(message, str):
            self.textBrowser.append(message)
        elif isinstance(message, dict):
            if message['err_no'] == 0:
                self.textBrowser.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t问题是：' + str(message['result'])[2:-3])
                self.textBrowser.append('################################################################\n')
                # 语音解析成功了
            else:
                self.textBrowser.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t我已经尽力了，问题解析失败！' + '错误代码：' + str(message['err_no']))
                self.textBrowser.append('################################################################\n')
                # 语音解析失败
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        问题采集
        """
        self.textBrowser.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t问题采集中...')
        self.speech = Speech_Recognition_Thread(self.spinBox.value())
        # 设置录音时间，并开始录音
        self.speech.finished_signal.connect(self._show_message)
        self.speech.voice_signal.connect(self._show_message)
        self.speech.start()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    dialog = Dialog_voice()
    dialog.show()
    sys.exit(app.exec_())

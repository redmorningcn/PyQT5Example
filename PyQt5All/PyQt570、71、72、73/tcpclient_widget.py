# -*- coding: utf-8 -*-

"""
这是一个关于局域网群聊小工具Plus的小例子--带文件传输功能！
文章链接：http://www.xdbcb8.com/archives/1386.html
文章链接：http://www.xdbcb8.com/archives/1394.html
文章链接：http://www.xdbcb8.com/archives/1396.html
文章链接：http://www.xdbcb8.com/archives/1402.html
"""

from PyQt5.QtCore import pyqtSlot, QTime, QDataStream, QFile
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
from Ui_tcpclient import Ui_TcpClient


class TcpC(QDialog, Ui_TcpClient):
    """
    Tcp客户端
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(TcpC, self).__init__(parent)
        self.setupUi(self)
        self.TotalBytes = 0
        self.bytesReceive = 0
        self.fileNameSize = 0
        self.bytesToReceive = 0
        self.fileName = ""
        self.tcpClient = QTcpSocket(self)
        self.tcpPort = 7788
        self.time = QTime()

        self.tcpClient.readyRead.connect(self.readMessage)
        # 每当新数据可用于从设备的当前读取通道读取时，readyRead信号就会发出一次。

        self.tcpClient.error.connect(self.displayError)
        # 当网络连接出现问题时调用displayError()函数。

    def setHostAddress(self, address):
        """
        设置服务器地址
        """
        self.hostAddress = address
        self.newConnect()
        # 设置服务器地址，同时调用newConnect()函数。

    def setFileName(self, file):
        """
        待接收文件的文件名
        """
        self.localFile = QFile(file)
        # 设置待接收文件的文件名，这个函数是放在主程序里面调用的。

    def closeEvent(self, event):
        """
        关闭事件
        """
        self.on_tcpClientCloseBtn_clicked()

    def newConnect(self):
        """
        连接服务器并开始计时
        """
        self.tcpClient.abort()
        self.tcpClient.connectToHost(self.hostAddress, self.tcpPort)
        self.time.start()
        # abort()中止当前连接并重置套接字。与disconnectFromHost()不同，此函数立即关闭套接字，丢弃写缓冲区中的任何挂起数据。
        # connectToHost()尝试与self.hostAddress的self.tcpPort端口建立连接。

    def readMessage(self):
        """
        读取文件数据
        """
        receiver = QDataStream(self.tcpClient)
        receiver.setVersion(QDataStream.Qt_5_4)

        if self.bytesReceive <= 2:
            if self.tcpClient.bytesAvailable() >= 2 and self.fileNameSize == 0:
                self.TotalBytes = receiver.readInt64()
                self.fileNameSize = receiver.readInt64()
                self.bytesReceive += 2
        # 当接收的字节数小于等2，同时套接字返回等待读取的传入字节数大于2而文件名大小不确定时，传输的总大小receiver.readInt64()，文件名大小是receiver.readInt64()。

            if self.tcpClient.bytesAvailable() >= self.fileNameSize and self.fileNameSize != 0:
                self.fileName = receiver.readQString()
                self.bytesReceive += self.fileNameSize
                # 当我们接收的字节数一定后，我们读取文件名receiver.readQString()，自然收到的字节数要加上文件名大小。
                if not(self.localFile.open(QFile.WriteOnly)):
                    QMessageBox.warning(self, "应用程序", "无法读取文件 {}：\n {}".format(self.fileName, self.localFile.errorString()))
                    return
                    # 要是写文件存在问题就报错。
            else:
                return

        if self.bytesReceive < self.TotalBytes:
            self.bytesReceive += self.tcpClient.bytesAvailable()
            inBlock = self.tcpClient.readAll()
            self.localFile.write(inBlock)
            inBlock.resize(0)

        useTime = self.time.elapsed() / 1000
        
        bytesReceived = self.bytesReceive / (1024*1024)
        speed = bytesReceived / useTime
        total = self.TotalBytes / (1024*1024)
        left = (total - bytesReceived) / speed

        if bytesReceived < 0.01:
            # 要是我们收到的文件太小了，我们设定成KB为单位
            bytesReceived = self.bytesReceive / 1024
            speed = bytesReceived / useTime / 1024
            total = self.TotalBytes / 1024
            if left > 0:
                msg = "已接收 {0:.2f} KB ({1:.2f}KB/s)\n共{2:.2f}KB.已用时：{3:.1f}秒\n估计剩余时间：{4:.1f}秒".format(bytesReceived, speed, total, useTime, left)
            else:
                msg = "已接收 {0:.2f} KB ({1:.2f}KB/s)\n共{2:.2f}KB.已用时：{3:.1f}秒\n".format(bytesReceived, speed, total, useTime)

        else:
            # 要是文件比较大，我们设定成MB为单位
            if left > 0:
                msg = "已接收 {0:.2f} MB ({1:.2f}MB/s)\n共{2:.2f}MB.已用时：{3:.1f}秒\n估计剩余时间：{4:.1f}秒".format(bytesReceived, speed, total, useTime, left)
            else:
                msg = "已接收 {0:.2f} MB ({1:.2f}MB/s)\n共{2:.2f}MB.已用时：{3:.1f}秒\n".format(bytesReceived, speed, total, useTime)

        self.progressBar.setMaximum(total)
        self.progressBar.setValue(bytesReceived)

        self.tcpClientStatuslabel.setText(msg)
        
        if self.bytesReceive == self.TotalBytes:
            self.localFile.close()
            self.tcpClient.close()
            self.tcpClientStatuslabel.setText("接收文件{}完毕".format(self.fileName))
            self.tcpClientBtn.setEnabled(False)
        # 当我们接收的大小和文件总大小一致时，关闭网络连接、文件，提示接收完毕。


    def displayError(self, socketError):
        """
        显示错误
        """
        if socketError == QAbstractSocket.RemoteHostClosedError:
            pass
        else:
            errorMsg = self.tcpClient.errorString()
            QMessageBox.warning(self, "应用程序", errorMsg)
            return
        # 网络错误的处理。

    @pyqtSlot()
    def on_tcpClientBtn_clicked(self):
        """
        取消接收
        """
        self.tcpClient.abort()
        if self.localFile.isOpen():
            self.localFile.close()
        
        self.tcpClientBtn.setEnabled(False)
        # 点击取消时传输终止
    
    @pyqtSlot()
    def on_tcpClientCloseBtn_clicked(self):
        """
        关闭
        """
        self.tcpClient.abort()
        if self.localFile.isOpen():
            self.localFile.close()
        self.close()
        self.tcpClientBtn.setEnabled(True)
        # 关闭网络连接，相关设置复位。
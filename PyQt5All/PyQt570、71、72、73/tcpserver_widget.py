# -*- coding: utf-8 -*-

"""
这是一个关于局域网群聊小工具Plus的小例子--带文件传输功能！
文章链接：http://www.xdbcb8.com/archives/1386.html
文章链接：http://www.xdbcb8.com/archives/1394.html
文章链接：http://www.xdbcb8.com/archives/1396.html
文章链接：http://www.xdbcb8.com/archives/1402.html
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QFile, QDataStream, QIODevice, QTime, QByteArray
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, qApp
from PyQt5.QtNetwork import QTcpServer, QHostAddress, QTcpSocket
from Ui_tcpserver import Ui_TcpServer

class TcpS(QDialog, Ui_TcpServer):
    """
    文件传输服务器
    """

    sendFileName = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(TcpS, self).__init__(parent)
        self.setupUi(self)
        self.payloadSize = 64*1024
        # 读取数据64KB

        self.totalBytes = 0
        # 总大小

        self.bytesWritten = 0
        # 保存的数据

        self.bytesToWrite = 0
        # 每次减少连接写的数据量大小

        self.theFileName = ""
        # 文件名（不含路径）

        self.fileName = ""
        # 文件全名

        self.localFile = QFile()
        self.outBlock = QByteArray()
        # QByteArray()的对象，即字节数组

        self.time = QTime()
        self.initServer()

    def initServer(self):
        """
        网络设置初始化
        """
        self.tcpPort = 7788
        # 指定了TCP端口为7788

        self.tcpServer = QTcpServer(self)
        self.clientConnection = QTcpSocket(self)
        # 创建一个Tcp服务器和一个Tcp套接字

        self.tcpServer.newConnection.connect(self.sendMessage)
        # 当有新的连接来的时候发出newConnection信号，我们连接到sendMessage()函数。

        self.serverStatuslabel.setText("请选择要传送的文件")
        self.progressBar.reset()
        self.serverOpenBtn.setEnabled(True)
        self.serverSendBtn.setEnabled(False)
        self.tcpServer.close()
        # 显示我们开始创建的对话框，打开按钮是可用的，发送按钮是不可用的，进度条复位，先关闭服务器。

    def refused(self):
        """
        对端拒绝接收文件，主程序会调用服务器的refused()函数，关闭服务器。
        """
        self.tcpServer.close()
        self.serverStatuslabel.setText("对方拒绝接收")

    def closeEvent(self, event):
        """
        关闭事件
        """
        self.on_serverCloseBtn_clicked()
        # 产生关闭事件，直接调用关闭窗口按钮函数。

    def sendMessage(self):
        """
        发送文件
        """
        self.serverSendBtn.setEnabled(False)
        # 发送按钮不可用

        self.clientConnection = self.tcpServer.nextPendingConnection()
        # self.clientConnection作为连接的QTcpSocket对象返回下一个挂起的连接。

        self.clientConnection.bytesWritten.connect(self.updateClientProgress)
        # 当连接中每次将数据有效载荷写入设备的当前写通道时，都会发出此信号。在此有效负载中写入的数据量为字节数。

        self.serverStatuslabel.setText("开始传送文件 {} ！".format(self.theFileName))

        self.localFile = QFile(self.fileName)
        if not(self.localFile.open(QFile.ReadOnly)):
            errorMsg = "无法读取文件 {}:\n {}".format(self.fileName, self.localFile.errorString())
            QMessageBox.warning(self, "应用程序", errorMsg)
            return
        # 尝试打开文件，要是存在问题就报错。

        self.serverCloseBtn.setText("取消")

        self.totalBytes = self.localFile.size()
        # 记录一下需要传输的文件大小。单位：字节

        sendOut = QDataStream(self.outBlock, QIODevice.WriteOnly)
        # 这里的self.outBlock是QByteArray()的对象，即字节数组；QIODevice的模式为WriteOnly

        sendOut.setVersion(QDataStream.Qt_5_4)
        # 设定QDataStream的版本为Qt_5_4

        self.time.start()
        # 开始计时

        currentFile = self.fileName.split("/")[-1]
        # 传输的文件名

        sendOut.writeInt64(0)
        sendOut.writeInt64(0)
        sendOut.writeQString(currentFile)
        self.totalBytes += self.outBlock.size()
        # 在sendOut中写入文件名以及文件名和文件的大小，大小都是以字节为单位的。

        sendOut.device().seek(0)
        sendOut.writeInt64(self.totalBytes)
        sendOut.writeInt64(self.outBlock.size()-2)
        # QIODevice读写位置移动到0。然后分别写入总的大小和文件名大小。

        self.bytesToWrite = self.totalBytes - self.clientConnection.write(self.outBlock)
        # 待传输文件的大小。

        self.outBlock.resize(0)
        # outBlock清零。

    def updateClientProgress(self, numBytes):
        """
        发送进度显示
        """
        qApp.processEvents()
        # 长时间工作用，以免窗口假死

        self.bytesWritten += numBytes
        if self.bytesWritten > 0:
            self.block = self.localFile.read(min(self.bytesToWrite, self.payloadSize))
            self.bytesToWrite -= self.clientConnection.write(self.block)
        else:
            self.localFile.close()
        # 当我们待写入的字节数大于0时，我们每次读取的数据都是小于等于self.payloadSize的，这个self.payloadSize我们定义是64KB。
        # self.bytesToWrite每次减少连接写的数据量大小。
        # 要是待写入的字节数小于等于0，则关闭文件。

        byteSent = self.bytesWritten / (1024*1024)
        # 已经写了多少文件
        useTime = self.time.elapsed() / 1000
        # 传输用了多长时间
        speed = self.bytesWritten / useTime / (1024*1024)
        # 传输速度
        total = self.totalBytes / (1024*1024)
        # 总大小
        left = (total - byteSent) / speed
        # 表示剩余时间
        
        if byteSent < 0.01:
            byteSent = self.bytesWritten / 1024
            speed = self.bytesWritten / useTime / 1024
            total = self.totalBytes / 1024
            if left > 0:
                sendInfo = "已发送 {0:.2f}KB（{1:.2f}KB/s)\n共{2:.2f}KB 已用时：{3:.1f}秒\n 估计剩余时间:{4:.1f}秒".format(byteSent, speed, total, useTime, left)
            else:
                sendInfo = "已发送 {0:.2f}KB（{1:.2f}KB/s)\n共{2:.2f}KB 用时：{3:.1f}秒\n".format(byteSent, speed, total, useTime)
        else:
            if left > 0:
                sendInfo = "已发送 {0:.2f}MB（{1:.2f}MB/s)\n共{2:.2f}MB 已用时：{3:.1f}秒\n 估计剩余时间:{4:.1f}秒".format(byteSent, speed, total, useTime, left)
            else:
                sendInfo = "已发送 {0:.2f}MB（{1:.2f}MB/s)\n共{2:.2f}MB 用时：{3:.1f}秒\n".format(byteSent, speed, total, useTime)

        self.progressBar.setMaximum(total)
        self.progressBar.setValue(byteSent)
        
        if self.bytesWritten == self.totalBytes:
            self.serverCloseBtn.setText("关闭")
        # 进度条显示的方式，以及当传输的字节数等于总的字节数的时候，按钮就显示关闭。

        self.serverStatuslabel.setText(sendInfo)

    @pyqtSlot()
    def on_serverOpenBtn_clicked(self):
        """
        打开文件准备发送
        """
        self.fileName = QFileDialog.getOpenFileName(self, '打开文件', './')[0]
        if self.fileName:
            self.theFileName = self.fileName.split("/")[-1]
            self.serverStatuslabel.setText("要传送的文件为：{}".format(self.theFileName))
            self.serverSendBtn.setEnabled(True)
            self.serverOpenBtn.setEnabled(False)
    
    @pyqtSlot()
    def on_serverSendBtn_clicked(self):
        """
        发送文件，等待接收
        """
        if not(self.tcpServer.listen(QHostAddress.Any, self.tcpPort)):
            errorMsg = self.tcpServer.errorString()
            QMessageBox.warning(self, "错误", "发送失败：\n {}".format(errorMsg))
            self.TcpServer.close()
            return

        self.serverStatuslabel.setText("等待对方接收... ...")
        self.serverSendBtn.setEnabled(False)
        self.sendFileName.emit(self.theFileName)
    
    @pyqtSlot()
    def on_serverCloseBtn_clicked(self):
        """
        取消或者关闭
        """
        if self.tcpServer.isListening():
            self.tcpServer.close()
            if self.localFile.isOpen():
                self.localFile.close()
            self.clientConnection.abort()

        if self.serverCloseBtn.text() == "取消":
            self.serverCloseBtn.setText("关闭")
        else:
            self.close()
            self.serverOpenBtn.setEnabled(True)
            self.serverSendBtn.setEnabled(False)
            self.progressBar.reset()
            self.totalBytes = 0
            self.bytesWritten = 0
            self.bytesToWrite = 0
            self.serverStatuslabel.setText("请选择要传送的文件")
        # 关闭传输对话框，相关数据、连接进行复位，为下次传输进行准备。
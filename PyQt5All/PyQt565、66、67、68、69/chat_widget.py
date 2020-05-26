# -*- coding: utf-8 -*-

"""
这是一个关于局域网群聊小工具的小例子！
文章链接：http://www.xdbcb8.com/archives/1341.html
文章链接：http://www.xdbcb8.com/archives/1359.html
文章链接：http://www.xdbcb8.com/archives/1373.html
文章链接：http://www.xdbcb8.com/archives/1375.html
文章链接：http://www.xdbcb8.com/archives/1380.html
"""

import json
import codecs
import sys
from PyQt5.QtCore import pyqtSlot, Qt, QProcess, QDateTime, QFile, QTextStream
from PyQt5.QtGui import QFont, QColor, QTextCursor, QTextCharFormat, QTextDocumentWriter
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QFileDialog, QColorDialog, QHeaderView, QApplication, QMenu, QAction
from PyQt5.QtNetwork import QUdpSocket, QHostInfo, QNetworkInterface, QAbstractSocket, QHostAddress
from Ui_widget import Ui_Widget

class Chat(QWidget, Ui_Widget):
    """
    聊天小工具
    """
    Message, NewParticipant, ParticipantLeft = range(3)
    # 3种消息类型：消息、新用户、用户离开

    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(Chat, self).__init__(parent)
        self.setupUi(self)
        self.networkInit()
        self.userTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 表格的设置参见这篇文章，还比较全些：http://www.xdbcb8.com/archives/1414.html

        self.splitter.setStretchFactor(0, 7)
        self.splitter.setStretchFactor(1, 3)
        self.splitter_2.setStretchFactor(0, 6)
        self.splitter_2.setStretchFactor(1, 5)
    
    def networkInit(self):
        """
        网络环境初始化配置
        """
        self.udpSocket = QUdpSocket(self)
        self.port = 12345
        # 我们自定义的UDP端口号

        self.udpSocket.bind(self.port, QUdpSocket.ShareAddress | QUdpSocket.ReuseAddressHint)
        # 绑定套接字

        self.udpSocket.readyRead.connect(self.processPendingDatagrams)
        # 每当新数据可用于从设备的当前读取通道读取时，该信号就会发出一次。 
        # 只有在新数据可用时才会再次发出它，例如网络数据的新有效负载已经到达网络套接字，或者新的数据块已经附加到您的设备上。

        self.sendMessage(Chat.NewParticipant)
        # 新程序打开时我们发出“新人报到”的消息

        currentUser = "微信公众号：局域网聊天小工具 | 当前用户：{} | IP：{}".format(self.getUserName(), self.getIP())
        self.setWindowTitle(currentUser)
        # 将当前用户的用户名、IP地址带入到窗口的标题栏中

    def newParticipant(self, userName, localHostName, ipAddress):
        """
        新用户上线
        """
        isEmpty = self.userTableWidget.findItems(ipAddress, Qt.MatchExactly)
        # 先去查找下在用户列表中是否已经存在相应IP地址，查找方式为Qt.MatchExactly

        if not(isEmpty):
            user = QTableWidgetItem(userName)
            host = QTableWidgetItem(localHostName)
            ip = QTableWidgetItem(ipAddress)

            self.userTableWidget.insertRow(0)
            self.userTableWidget.setItem(0, 0, user)
            self.userTableWidget.setItem(0, 1, host)
            self.userTableWidget.setItem(0, 2, ip)
            # 要是IP找不到的话，我们就把用户名、主机名、IP地址添加到用户表格中。

            self.messageBrowser.setTextColor(Qt.gray)
            self.messageBrowser.setCurrentFont(QFont("Times New Roman", 10))
            online_user = "{}在线".format(userName)
            self.messageBrowser.append(online_user)
            # 在消息显示区显示“XX在线”，字体颜色为灰色、字体为Times New Roman，大小为10号

            online_user_cnt = "在线人数：{}".format(self.userTableWidget.rowCount())
            self.userNumLabel.setText(online_user_cnt)
            self.sendMessage(Chat.NewParticipant)
    
    def participantLeft(self, username, ipAddress, time):
        """
        剩余用户
        """
        findItem = self.userTableWidget.findItems(ipAddress, Qt.MatchExactly)
        if findItem:
            # 同样的XX离开了，我们也还是要先去用户表中找一下其对应的IP地址，如果存在的话，删除该用户，显示xx于xx时间离开，并统计一下在线人数
            rowNum = findItem[0].row()
            self.userTableWidget.removeRow(rowNum)
            self.messageBrowser.setTextColor(Qt.gray)
            self.messageBrowser.setCurrentFont(QFont("Times New Roman",10))
            offline_user = "{} 于 {} 离开！".format(username, time)
            self.messageBrowser.append(offline_user)
            online_user_cnt = "在线人数：{}".format(self.userTableWidget.rowCount())
            self.userNumLabel.setText(online_user_cnt)

    def saveFile(self, fileName):
        """
        保存文件
        """
        SuffixFileName = fileName.split(".")[1]
        if SuffixFileName in ("htm", "html"):
            content = self.messageBrowser.toHtml()
        else:
            content = self.messageBrowser.toPlainText()
        # 判断聊天记录的保存类型，是odt还是html（htm）。前者取它的字符串，后者保存内容和格式。
        try:
            with codecs.open(fileName, 'w', encoding="gbk") as f:
                f.write(content)
            return True
        except IOError:
            QMessageBox.critical(self, "保存错误", "聊天记录保存失败！")
            return False
        # 保存聊天记录。


    def closeEvent(self, event):
        """
        关闭程序发送用户离开消息
        """
        self.sendMessage(Chat.ParticipantLeft)
    
    def processPendingDatagrams(self):
        """
        处理收到的消息
        """

        while self.udpSocket.hasPendingDatagrams():
            # 开启循环，让udpSocket等待接收数据

            data, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
            # 读取收到的UDP数据，大小是返回第一个挂起的UDP数据报的大小。返回值是数据、主机信息、端口信息。

            datagram = str(data, encoding='utf-8')

            datagramDict = json.loads(datagram)# 转换成字典

            messageType = datagramDict["messageType"]
            userName = datagramDict["userName"]
            localHostName = datagramDict["localHostName"]
            ipAddress = datagramDict["ipAddress"]
            # 字节流信息转成字符串并变成字典，取得消息类型、用户名、主机名和IP地址。

            time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")

            if messageType == Chat.Message:

                message = datagramDict["message"]
                isAtUsername = self.findAt(message)
                if isAtUsername == self.getUserName():
                    QApplication.alert(self, 0)
                    # 如果窗口不是活动窗口，则会为窗口小部件显示警报。
                
                self.messageBrowser.setTextColor(Qt.blue)
                self.messageBrowser.setCurrentFont(QFont("Times New Roman", 12))
                self.messageBrowser.append("[" + userName + "]" + time)
                self.messageBrowser.append(message)
                # 在消息展示区增加相应的发送人和聊天内容

            elif messageType == Chat.NewParticipant:
                self.newParticipant(userName, localHostName, ipAddress)

            elif messageType == Chat.ParticipantLeft:
                self.participantLeft(userName, ipAddress, time)
            # 要是消息类型是Chat.NewParticipant或者Chat.ParticipantLeft，则分别调用newParticipant()和participantLeft()函数
    
    def findAt(self, message):
        """
        找到@的用户名
        """
        for row in range(self.userTableWidget.rowCount()):
            username = self.userTableWidget.item(row, 0).text()
            Atusername = "@" + username
            if message.find(Atusername) >= 0:
                return username
        return "NotFound"
    
    def sendMessage(self, messageType):
        """
        发送消息
        """
        localHostName = QHostInfo.localHostName()
        # 获得主机名

        ipAddress = self.getIP()

        username = self.getUserName()

        data = {"messageType":messageType, "userName":username, "localHostName":localHostName}
        # 我们构建一个消息数据，这个数据的类型，我们定义为字典，里面放了消息类型、用户名、主机名。

        if messageType == Chat.Message:
            if self.messageTextEdit.toPlainText() == "":
                QMessageBox.warning(self, "警告", "发送内容不能为空", QMessageBox.Ok)
                return

            message = self.getMessage()
            data["ipAddress"] = ipAddress
            data["message"] = message
            # 如果不是空消息，我们取得聊天框中的内容以及本地IP地址，并增加到消息数据当中。

        elif messageType in (Chat.NewParticipant, Chat.ParticipantLeft):
            data["ipAddress"] = ipAddress
        # 要是我们发送的消息类型是：Chat.NewParticipant和Chat.ParticipantLeft（新人报到、用户离开），我们取得Ip地址后并增加到消息数据中

        jdata = json.dumps(data)
        encodeData = bytes(jdata, encoding="utf-8")
        # 将消息data转成json格式，并通过bytes函数将其转成字节型的

        self.udpSocket.writeDatagram(encodeData, QHostAddress.Broadcast, self.port)
        # 发送UDP广播数据，端口号是12345

    def getIP(self):
        """
        获得用户IP
        """
        addressList = QNetworkInterface.allAddresses()
        # QNetworkInterface类提供主机的IP地址和网络接口的列表（list类型）。
        # QNetworkInterface表示连接到运行程序的主机的一个网络接口。
        # 每个网络接口可以包含零个或多个IP地址，每个IP地址可选地与网络掩码和/或广播地址相关联。
        # 可以使用addressEntries()获得此类三元组的列表。
        # 当不需要网络掩码或广播地址或其他信息时，使用allAddresses()便捷功能仅获取活动接口的IP地址。

        for address in addressList:
            if address.protocol() == QAbstractSocket.IPv4Protocol and address != QHostAddress.LocalHost and address.toString()[:3] != "169" and address.toString().split(".")[-1] != "1":
                return address.toString()
            # 只要IPv4、不要169开头的地址、不要结尾是1的IP地址(可能是网关)
        return "0.0.0.0"
        # 什么都获取不到返回”0.0.0.0”

    def getMessage(self):
        """
        获得消息
        """
        msg = self.messageTextEdit.toHtml()
        self.messageTextEdit.clear()
        self.messageTextEdit.setFocus()
        return msg

    def getUserName(self):
        """
        获得用户名
        """
        envVariables = ["USERNAME", "USER", "HOSTNAME", "DOMAINNAME"]
        environment = QProcess.systemEnvironment()
        # 返回系统的环境变量
        for var in environment:
            varlist = var.split("=")
            isfide = varlist[0] in envVariables
            if isfide:
                return varlist[1]
        return "unKnow"
        # 要是在系统的环境变量中key值包含envVariables中的任意一个，找到就返回；
        # 并将其作为用户名。要是都找不到则返回”UnKnow”
    
    def mergeFormatDocumentOrSelection(self, format):
        """
        格式处理，不全选，全文也能变化
        """
        cursor = self.messageTextEdit.textCursor()
        # 返回表示当前可见光标的QTextCursor的副本cursor
        if not cursor.hasSelection():
            cursor.select(QTextCursor.Document)
            # 如果我们没有进行选择操作，我们设置选择模式为全文选择

        cursor.mergeCharFormat(format)
        # 将光标的当前字符格式与格式修饰符描述的属性合并。
        # 如果光标有选择，则此函数将修饰符中设置的所有属性应用于作为选择的一部分的所有字符格式。

        self.messageTextEdit.mergeCurrentCharFormat(format)
        # 通过在编辑器的光标上调用QTextCursor.mergeCharFormat，将修饰符中指定的属性合并为当前字符格式。
        # 如果编辑器有选择，则修改器的属性将直接应用于选择。

    def contextMenuEvent(self, event):
        """
        @ TA，在线用户列表右键菜单设置，只能@别人不能@自己
        """
        items = self.userTableWidget.selectedItems()
        if items:
            selectedUserName = self.userTableWidget.selectedItems()[0].text()
            if selectedUserName != self.getUserName():
                pmenu = QMenu(self)
                pContact = QAction('@TA', self.userTableWidget)
                pmenu.addAction(pContact)
                pmenu.popup(self.mapToGlobal(event.pos()))
                pContact.triggered.connect(lambda:self.ContactTA(selectedUserName))
                # 通过lamda函数的形式传递参数
    
    def ContactTA(self, username):
        """
        显示@TA，增加一个格式
        """
        userAt = "<font color=\'#FF0000\' size='5'>@{} </font>".format(username)
        self.messageTextEdit.append(userAt)
        self.messageTextEdit.setFocus()

    @pyqtSlot(str)
    def on_SizeComboBox_currentIndexChanged(self, p0):
        """
        字体大小下拉框选择变化
        """
        fmt = QTextCharFormat()
        fmt.setFontPointSize(int(p0))
        self.mergeFormatDocumentOrSelection(fmt)
        self.messageTextEdit.setFocus()
    
    @pyqtSlot(str)
    def on_fontComboBox_currentIndexChanged(self, p0):
        """
        字体下拉框选择变化
        """
        fmt = QTextCharFormat()
        fmt.setFontFamily(p0)
        self.mergeFormatDocumentOrSelection(fmt)

        self.messageTextEdit.setFocus()
    
    @pyqtSlot(bool)
    def on_boldToolBtn_clicked(self, checked):
        """
        是否字体加粗
        """
        fmt = QTextCharFormat()
        fmt.setFontWeight(checked and QFont.Bold or QFont.Normal)
        # checked为真返回QFont.Bold否则返回QFont.Normal。一个很有用的写法。
        self.mergeFormatDocumentOrSelection(fmt)

        self.messageTextEdit.setFocus()
    
    @pyqtSlot(bool)
    def on_italicToolBtn_clicked(self, checked):
        """
        斜体
        """
        fmt = QTextCharFormat()
        fmt.setFontItalic(checked)
        self.mergeFormatDocumentOrSelection(fmt)

        self.messageTextEdit.setFocus()
    
    @pyqtSlot(bool)
    def on_underlineToolBtn_clicked(self, checked):
        """
        下划线
        """
        fmt = QTextCharFormat()
        fmt.setFontUnderline(checked)
        self.mergeFormatDocumentOrSelection(fmt)
        self.messageTextEdit.setFocus()

    @pyqtSlot(bool)
    def on_colorToolBtn_clicked(self):
        """
        颜色选择
        """
        col = QColorDialog.getColor(self.messageTextEdit.textColor(), self)
        if not col.isValid():
            return
        fmt = QTextCharFormat()
        fmt.setForeground(col)
        self.mergeFormatDocumentOrSelection(fmt)
        self.messageTextEdit.setFocus()
    
    @pyqtSlot()
    def on_saveToolBtn_clicked(self):
        """
        保存聊天记录
        """
        if self.messageBrowser.document().isEmpty():
            QMessageBox.warning(self, "警告", "聊天记录为空,无法保存!", QMessageBox.Ok)
            # 如果消息展示区为空，保存记录的话则会弹出告警对话框。
        else:
            fileName = QFileDialog.getSaveFileName(self, "保存聊天记录", "./聊天记录", ("ODT files (*.odt);;HTML-Files (*.htm *.html)"))
            if fileName[0]:# 文件的全名
                if self.saveFile(fileName[0]):
                    QMessageBox.information(self, "聊天记录保存", "保存成功！")
            # 调用QFileDiaglog，保存文件，保存的类型为ODT文件或HTML文件。其中ODT文件是可以用写字板打开的。
    
    @pyqtSlot()
    def on_clearToolBtn_clicked(self):
        """
        清空聊天记录
        """
        self.messageBrowser.clear()
    
    @pyqtSlot()
    def on_sendButton_clicked(self):
        """
        发送消息
        """
        self.sendMessage(Chat.Message)
    
    @pyqtSlot()
    def on_exitButton_clicked(self):
        """
        退出
        """
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat = Chat()
    chat.show()
    sys.exit(app.exec_())
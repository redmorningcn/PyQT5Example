# -*- coding: utf-8 -*-

"""
这是一个DIY浏览器的小例子！
文章链接：http://www.xdbcb8.com/archives/1567.html
文章链接：http://www.xdbcb8.com/archives/1571.html
文章链接：http://www.xdbcb8.com/archives/1581.html
文章链接：http://www.xdbcb8.com/archives/1597.html
"""
import sys
from PyQt5.QtCore import pyqtSlot, QUrl, QEvent, Qt, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QMessageBox, QCompleter
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from Ui_ui import Ui_MainWindow

class NewWebView(QWebEngineView):
    '''
    新的页面
    '''
    def __init__(self, tabWidget):
        '''
        一些初始设置
        '''
        super().__init__()
        self.tabWidget = tabWidget
    
    def createWindow(self, WebWindowType):
        '''
        新页面
        '''
        new_webview = NewWebView(self.tabWidget)
        self.tabWidget.newTab(new_webview)
        return new_webview
        # 新增加的QWebEngineView对象，放入tabWidget新的标签页中

class WebView(QMainWindow, Ui_MainWindow):
    """
    DIY浏览器
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(WebView, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        """
        界面初始设置
        """
        self.progressBar.hide()
        # 进度条最开始要隐藏起来，我们让进度条只用在载入新网页的时候再出现。
        self.showMaximized()
        # 同时窗口还要最大化。

        self.tabWidget.setTabShape(QTabWidget.Triangular)
        # 边角是三角型

        self.tabWidget.setDocumentMode(True)
        # 此属性保存选项卡窗口小部件是否以适合文档页面的模式呈现。
        # 此模式对于显示页面覆盖大部分选项卡小部件区域的文档类型页面非常有用。

        self.tabWidget.setMovable(True)
        # 标签页可以移动

        self.tabWidget.setTabsClosable(True)
        # 标签页可以关闭

        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        # 当标签页关闭的时候，会产生tabCloseRequested信号，与此同时会连接到closeTab()

        self.tabWidget.currentChanged.connect(self.tabChange)
        # 当标签页新增或者移动的时候，就会产生currentChanged信号，同时连接到self.tabChange函数。

        self.view = NewWebView(self)
        self.view.load(QUrl("https://www.hao123.com"))
        # 新的网页浏览页面通过QTabWidget的标签页展示出来，第一次打开的话显示“好123网址导航”

        self.newTab(self.view)
        self.lineEdit.installEventFilter(self)
        self.lineEdit.setMouseTracking(True)#启用鼠标追踪
        settings = QWebEngineSettings.defaultSettings()
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        # 启用浏览器中的flash功能

        # settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        # 支持JavaScript
        self.getModel()

    def getModel(self):
        '''
        url自动补全
        '''
        self.m_model = QStandardItemModel(0, 1, self)
        m_completer = QCompleter(self.m_model, self)
        self.lineEdit.setCompleter(m_completer)
        m_completer.activated[str].connect(self.onUrlChoosed)
    
    def newTab(self, view):
        '''
        QTabWidget的标签页展示出来
        '''
        self.pb_forward.setEnabled(False)
        self.pb_back.setEnabled(False)
        # 前进、后退按钮默认不可用

        view.titleChanged.connect(self.webTitle)
        # 标题变化信号
        view.iconChanged.connect(self.webIcon)
        # 图标变化信号
        view.loadProgress.connect(self.webProgress)
        # 载入进度变化信号
        view.loadFinished.connect(self.webProgressEnd)
        # 载入完成信号
        view.urlChanged.connect(self.webHistory)
        # url变化信号
        view.page().linkHovered.connect(self.showUrl)
        # 鼠标移动url上信号

        currentUrl = self.getUrl(view)

        self.lineEdit.setText(currentUrl)
        # 还需要将地址栏中的url改一下名称。
        self.tabWidget.addTab(view, "新标签页")
        self.tabWidget.setCurrentWidget(view)
        # 打开新页面的时候，新的标签页的名称默认是“新标签页”，并设置当前小部件是这个新的网页页面。

    def getUrl(self, webview):
        '''
        获得当前浏览页面的url
        '''
        url = webview.url().toString()
        return url

    def closeTab(self, index):
        '''
        关闭Tab页面
        '''
        if self.tabWidget.count() > 1:
            self.tabWidget.widget(index).deleteLater()
            self.tabWidget.removeTab(index)
            # 多个页面关闭，尽快释放QWebEngineView对象内存
        elif self.tabWidget.count() == 1:
            self.tabWidget.removeTab(0)
            self.on_pb_new_clicked()

    def tabChange(self, index):
        '''
        证当前浏览页面发生任何变化时，地址栏中的url始终和当前浏览页面的url保持一致。
        '''
        currentView = self.tabWidget.widget(index)
        if currentView:
            currentViewUrl = self.getUrl(currentView)
            self.lineEdit.setText(currentViewUrl)

    def closeEvent(self, event):
        '''
        浏览器关闭
        '''
        tabNum = self.tabWidget.count()
        # Tab数量
        closeInfo = "你打开了{}个标签页，现在确认关闭？".format(tabNum)
        if tabNum > 1:
            r = QMessageBox.question(self, "关闭浏览器", closeInfo, QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
            if r == QMessageBox.Ok:
                event.accept()
            elif r == QMessageBox.Cancel:
                event.ignore()
            # 多个Tab页面提示下是否关闭
        else:
            event.accept()

    def eventFilter(self, object, event):
        '''
        事件过滤器
        '''
        if object == self.lineEdit:
            if event.type() == QEvent.MouseButtonRelease:
                self.lineEdit.selectAll()
                # 鼠标点击后全选
            elif event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Return:
                    self.on_pb_go_clicked()
                    # 按住回车键开始浏览网页
        return QObject.eventFilter(self, object, event)

    def webTitle(self, title):
        '''
        取部分标题
        '''
        index = self.tabWidget.currentIndex()
        if len(title) > 16:
            title = title[0:17]
        self.tabWidget.setTabText(index, title)

    def webIcon(self, icon):
        '''
        Tab页上显示图标
        '''
        index = self.tabWidget.currentIndex()
        self.tabWidget.setTabIcon(index, icon)
    
    def webProgress(self, progress):
        '''
        显示进度条
        '''
        self.progressBar.show()
        self.progressBar.setValue(progress)
    
    def webProgressEnd(self, isFinished):
        '''
        载入完毕的话，进度条当前值设为最大值：100
        '''
        if isFinished:
            self.progressBar.setValue(100)
            self.progressBar.hide()
            self.progressBar.setValue(0)
    
    def webHistory(self, url):
        '''
        浏览历史
        '''
        self.lineEdit.setText(url.toString())
        index = self.tabWidget.currentIndex()
        currentView = self.tabWidget.currentWidget()
        history = currentView.history()
        # 当前页面的浏览历史
        if history.count() > 1:
            # 前进、后退的启用方式
            if history.currentItemIndex() == history.count()-1:
                self.pb_back.setEnabled(True)
                self.pb_forward.setEnabled(False)
            elif history.currentItemIndex() == 0:
                self.pb_back.setEnabled(False)
                self.pb_forward.setEnabled(True)
            else:
                self.pb_back.setEnabled(True)
                self.pb_forward.setEnabled(True)

    def showUrl(self, url):
        '''
        显示url
        '''
        self.statusBar.showMessage(url)

    def onUrlChoosed(self, url):
        '''
        自动补全url
        '''
        self.lineEdit.setText(url)

    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        '''
        url输入栏，自动补全功能！
        '''
        urlGroup = text.split(".")
        if len(urlGroup) == 3 and urlGroup[-1]:
            return
        elif len(urlGroup) == 3 and not(urlGroup[-1]):
            wwwList = ["com", "cn", "net", "org", "gov", "cc"]
            self.m_model.removeRows(0, self.m_model.rowCount())
            for i in range(0, len(wwwList)):
                self.m_model.insertRow(0)
                self.m_model.setData(self.m_model.index(0, 0), text + wwwList[i])
        # 当我们输入类似“www.baidu.”后，会判断一下，最后一个“.”是否为空，要是为空就把常见的域名后缀加上，否则函数就返回

    @pyqtSlot()
    def on_pb_new_clicked(self):
        """
        打开新页面
        """
        newView = NewWebView(self)
        self.newTab(newView)
        newView.load(QUrl(""))
        # url为空
    
    @pyqtSlot()
    def on_pb_forward_clicked(self):
        """
        前进
        """
        self.tabWidget.currentWidget().forward()
    
    @pyqtSlot()
    def on_pb_back_clicked(self):
        """
        后退
        """
        self.tabWidget.currentWidget().back()
    
    @pyqtSlot()
    def on_pb_refresh_clicked(self):
        """
        刷新
        """
        self.tabWidget.currentWidget().reload()
    
    @pyqtSlot()
    def on_pb_stop_clicked(self):
        """
        停止
        """
        self.tabWidget.currentWidget().stop()
    
    @pyqtSlot()
    def on_pb_go_clicked(self):
        """
        开始浏览
        """
        url = self.lineEdit.text()
        if url[0:7] == "http://" or url[0:8] == "https://":
            qurl = QUrl(url)
        else:
            qurl = QUrl("http://" + url)
        self.tabWidget.currentWidget().load(qurl)

    @pyqtSlot()
    def on_pb_home_clicked(self):
        """
        主页
        """
        homeurl = QUrl("http://www.xdbcb8.com")
        if self.tabWidget.currentWidget().title() == "about:blank":
            self.tabWidget.currentWidget().load(homeurl)
        else:
            newView = NewWebView(self)
            self.newTab(newView)
            newView.load(homeurl)
        # 要是空白页面直接载入网页，否则新开Tab页面载入网页

    def __del__(self):
        '''
        释放Web对象内存
        '''
        self.view.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wv = WebView()
    wv.show()
    sys.exit(app.exec_())
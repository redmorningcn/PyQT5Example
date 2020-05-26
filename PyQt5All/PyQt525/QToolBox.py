#coding=utf-8

'''
这是一个关于工具箱（QToolBox）的小例子！
文章链接：http://www.xdbcb8.com/archives/586.html
'''

import sys
import webbrowser
from PyQt5.QtWidgets import QToolBox, QApplication, QToolButton, QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class Example(QToolBox):
    '''
    工具箱打开网页
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        界面初始设置
        '''
        self.resize(280, 500)
        self.setWindowTitle('微信公众号：学点编程吧--QToolBox')
        self.setWindowFlags(Qt.Dialog)

        favorites = [
                        [
                            {'des':'百度搜索', 'pic':'image/se/baidu.ico'},
                            {'des':'搜狗搜索', 'pic':'image/se/sougo.ico'},
                            {'des':'必应搜索', 'pic':'image/se/bing.ico'},
                            {'des':'360搜索', 'pic':'image/se/360.ico'},
                            {'des':'谷歌搜索', 'pic':'image/se/google.ico'},
                            {'des':'雅虎搜索', 'pic':'image/se/yahoo.ico'}
                        ],
                        [
                            {'des':'腾讯视频', 'pic':'image/v/tengxun.ico'},
                            {'des':'搜狐视频', 'pic':'image/v/sohuvideo.ico'},
                            {'des':'优酷视频', 'pic':'image/v/youku.ico'},
                            {'des':'土豆视频', 'pic':'image/v/tudou.ico'},
                            {'des':'AcFun弹幕', 'pic':'image/v/acfun.ico'},
                            {'des':'哔哩哔哩', 'pic':'image/v/bilibili.ico'}
                        ]
        ]

        for item in favorites:
            groupbox = QGroupBox()
            vlayout = QVBoxLayout(groupbox)
            vlayout.setAlignment(Qt.AlignCenter)# 居中
            for category in item:
                toolButton = QToolButton()
                toolButton.setText(category['des'])
                toolButton.setIcon(QIcon(category['pic']))
                toolButton.setIconSize(QSize(64, 64))
                toolButton.setAutoRaise(True)
                toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)# 文字在图标的下面
                vlayout.addWidget(toolButton)
                name = category['des']
                toolButton.clicked.connect(self.run)
                # 内置小循环把那么多的按钮放到窗口中，我真是个天才！

            if name == '雅虎搜索':
                self.addItem(groupbox, '搜索引擎')
            else:
                self.addItem(groupbox, '视频网站')
            # 判断最后一个按钮显示的文字是“搜索引擎”还是“视频网站”，并将这一系列的按钮增加到一个选项卡中

        self.show()
    
    def run(self):
        if self.sender().text() == '百度搜索':
            webbrowser.open('https://www.baidu.com')# 打开相应的网页
        elif self.sender().text() == '搜狗搜索':
            webbrowser.open('https://www.sogou.com/')
        elif self.sender().text() == '必应搜索':
            webbrowser.open('http://cn.bing.com/')
        elif self.sender().text() == '360搜索':
            webbrowser.open('https://www.so.com/')
        elif self.sender().text() == '谷歌搜索':
            webbrowser.open('https://www.google.com/')
        elif self.sender().text() == '雅虎搜索':
            webbrowser.open('https://www.yahoo.com/')
        elif self.sender().text() == '腾讯视频':
            webbrowser.open('https://v.qq.com/')
        elif self.sender().text() == '搜狐视频':
            webbrowser.open('https://film.sohu.com')
        elif self.sender().text() == '优酷视频':
            webbrowser.open('http://www.youku.com/')
        elif self.sender().text() == '土豆视频':
            webbrowser.open('http://www.tudou.com/')
        elif self.sender().text() == 'AcFun弹幕':
            webbrowser.open('http://www.acfun.cn/')
        elif self.sender().text() == '哔哩哔哩':
            webbrowser.open('https://www.bilibili.com/')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
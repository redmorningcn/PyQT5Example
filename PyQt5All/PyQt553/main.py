# -*- coding: utf-8 -*-

"""
一个关于欢乐斗地主（QMdiArea的使用）的小例子！
文章链接：http://www.xdbcb8.com/archives/859.html
"""

import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMdiArea, QMdiSubWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from card import Card

class Example(QMainWindow):
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.InitUI()

    def InitUI(self):
        '''
        界面初始设置
        '''
        self.setWindowTitle('关注微信公众号：学点编程吧--扑克牌模拟')

        self.mid = QMdiArea()
        self.setCentralWidget(self.mid)
        # 新建一个QMdiArea类的对象，并将其设置为主窗口的中央小部件

        sendOnecardAct = QAction(QIcon('./res/sendOnecard.ico'), '发1张牌', self)
        sendOnecardAct.triggered.connect(self.sendOnecard)
        # 发1张牌命令

        sendFivecardsAct = QAction(QIcon('./res/sendFivecard.ico'), '随机5张牌', self)
        sendFivecardsAct.triggered.connect(self.sendFivecards)
        # 随机5张牌命令

        clearcardAct = QAction(QIcon('./res/clear.ico'), '清除牌', self)
        clearcardAct.triggered.connect(self.clearCards)
        # 清除牌命令

        foldcardAct = QAction(QIcon('./res/fold.ico'), '收牌', self)
        foldcardAct.triggered.connect(self.foldCards)
        # 收牌

        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(sendOnecardAct)
        toolbar.addAction(sendFivecardsAct)
        toolbar.addAction(clearcardAct)
        toolbar.addAction(foldcardAct)
        #把上面的几个命令放到工具栏上

        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #文字在图标下面
    
    def sendOnecard(self):
        '''
        随机一张牌，发出去。
        '''
        randomflag = self.randomsend(1)
        subcard = QMdiSubWindow()
        subcard.setWidget(Card(randomflag))
        self.mid.addSubWindow(subcard)
        subcard.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 设置窗口属性，让其只显示最小化按钮。
        subcard.resize(150, 200)
        subcard.show()
    
    def sendFivecards(self):
        '''
        随机5张牌
        '''
        randomflag = self.randomsend(5)
        for card in randomflag:
            # 遍历5张牌，发出去。
            subcard = QMdiSubWindow()
            subcard.setWidget(Card(card))
            self.mid.addSubWindow(subcard)
            subcard.setWindowFlags(Qt.WindowMinimizeButtonHint)
            # 设置窗口属性，让其只显示最小化按钮。
            subcard.resize(150, 200)
            subcard.show()
        
    def clearCards(self):
        '''
        清除牌
        '''
        self.mid.closeAllSubWindows()
        # 所有窗口关闭

    def foldCards(self):
        '''
        收牌
        '''
        self.mid.cascadeSubWindows()
        # 所有窗口级联模式排列
    
    def randomsend(self, num):
        '''
        发送方式：
        1、要是发1张牌，从cardlist中随机取一个元素返回就行了。
        2、要是随机发5张牌，从cardlist中随机取出一段包含有5个元素的列表。
        '''
        cardlist = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "a", "j", "joker", "k", "q"]
        if num == 1:
            return random.choice(cardlist)
        elif num == 5:
            return random.sample(cardlist, 5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
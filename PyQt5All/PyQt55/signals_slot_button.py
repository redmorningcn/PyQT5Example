#coding=utf-8

'''
这是一个猜拳的小游戏！
文章链接：http://www.xdbcb8.com/archives/190.html
'''

import sys
from random import randint
from PyQt5.QtWidgets import (QApplication, QMessageBox, QWidget, QPushButton)

class Example(QWidget):

    '''
    猜拳的小游戏
    '''
    
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        构造整个游戏界面
        '''
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')
        
        bt1 = QPushButton('剪刀', self)
        bt1.setGeometry(30, 180, 50, 50)
        
        bt2 = QPushButton('石头', self)
        bt2.setGeometry(100, 180, 50, 50)
        
        bt3 = QPushButton('布', self)
        bt3.setGeometry(170, 180, 50, 50)
        
        bt1.clicked.connect(self.buttonclicked)
        bt2.clicked.connect(self.buttonclicked)
        bt3.clicked.connect(self.buttonclicked)
        #三个按钮的clicked信号都连接到同一个槽buttonclicked()，我们会对不同按钮做出不同的反应。
        
        self.show()
        
    def buttonclicked(self):
        '''
        我们点击剪刀、石头、布不同按钮后的不同反应
        '''
        computer = randint(1, 3)#电脑出拳，用1、2、3分别表示剪刀、石头、布
        player = 0
        sender = self.sender()#我们点击按钮的对象
        if sender.text() == '剪刀':
            player = 1
        elif sender.text() == '石头':
            player = 2
        else:
            player = 3
        #根据按钮上的显示，我们将其转换成对应的数字：1、2、3

        if player == computer:
            QMessageBox.about(self, '结果', '平手')
        elif player == 1 and computer == 2:
            QMessageBox.about(self, '结果', '电脑：石头，电脑赢了！')
        elif player == 2 and computer == 3:
            QMessageBox.about(self, '结果', '电脑：布，电脑赢了！')
        elif player == 3 and computer == 1:
            QMessageBox.about(self, '结果', '电脑：剪刀，电脑赢了！')
        elif computer == 1 and player == 2:
            QMessageBox.about(self, '结果', '电脑：剪刀，玩家赢了！')
        elif computer == 2 and player == 3:
            QMessageBox.about(self, '结果', '电脑：石头，玩家赢了！')
        elif computer == 3 and player == 1:
            QMessageBox.about(self, '结果', '电脑：布，玩家赢了！')
        #和电脑猜拳输赢的判断

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
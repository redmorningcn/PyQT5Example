#coding=utf-8

'''
这是一个关于标签（QLabel）的小例子-GIF动画显示！
文章链接：http://www.xdbcb8.com/archives/460.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QMovie, QPixmap

class Example(QWidget):
    '''
    GIF动画显示
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
        self.resize(550, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--标签:动画（QLabel）')

        self.lb = QLabel(self)
        self.lb.setGeometry(100, 50, 300, 200)
        
        self.bt1 = QPushButton('开始', self)
        self.bt2 = QPushButton('停止', self)
        
        self.bt1.move(100, 20)
        self.bt2.move(280, 20)
        
        self.pix = QPixmap('movie.gif')
        self.lb.setPixmap(self.pix)
        self.lb.setScaledContents(True)# 图片全部显示出来，是多大显示多大。
        
        self.bt1.clicked.connect(self.run)
        self.bt2.clicked.connect(self.run)
        
        self.show()
        
    def run(self):
        '''
        在QLabel中加载GIF动画
        '''
        movie = QMovie("movie.gif")
        self.lb.setMovie(movie)
        if self.sender() == self.bt1:
            movie.start()# 动画开始
        else:
            movie.stop()# 动画停止
            self.lb.setPixmap(self.pix)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#coding=utf-8

'''
这是一个PyQt5与Opencv的小小融合的例子
文章链接：http://www.xdbcb8.com/archives/450.html
'''

import sys
import cv2
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication

class myLabel(QLabel):
    '''
    自定义一个QLabel类
    '''
    x0 = 0
    y0 = 0
    #记录按下的鼠标坐标

    x1 = 0
    y1 = 0
    # 记录移动的鼠标坐标

    flag = False
    #判断鼠标是否按下
    
    def mousePressEvent(self, event):
        '''
        鼠标按下事件
        '''
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
        #鼠标按下的相关坐标

    def mouseReleaseEvent(self, event):
        '''
        鼠标松开事件
        '''
        self.flag = False

    def mouseMoveEvent(self, event):
        '''
        鼠标移动事件
        '''
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            # 鼠标移动的相关坐标
            self.update()
        
    def paintEvent(self, event):
        '''
        重写画图事件
        '''
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        painter.drawRect(rect)
        # 画一个矩形框
        
        pqscreen = QGuiApplication.primaryScreen()
        # 此属性包含应用程序的主要（或默认）屏幕。

        pixmap2 = pqscreen.grabWindow(self.winId(), self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        # 创建并返回通过抓取由QRect（x，y，width，height）限制的给定窗口的内容构造的像素图。

        pixmap2.save('555.png')
        # 把像素图保存下来

class Example(QWidget):
    '''
    PyQt5与Opencv小小融合
    '''
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        界面设置
        '''
        self.resize(675, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--opencv、PyQt5的小小融合')

        self.lb = myLabel(self)
        self.lb.setGeometry(QRect(140, 30, 511, 241))

        img = cv2.imread('xxx.jpg')
        # 使用Opencv读取图像

        height, width, bytesPerComponent = img.shape
        # 在OpenCV-Python绑定中，图像使用NumPy数组的属性来表示图像的尺寸和通道信息

        bytesPerLine = 3 * width
        # 当1个像素占3个字节，此时图像为真彩色图像

        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        # 将图像从一个颜色空间转换为另一个颜色空间

        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # 用给定的宽度，高度和格式构造一个使用现有内存缓冲区数据的图像

        pixmap = QPixmap.fromImage(QImg)
        # QImage对象转换成QPixmap对象

        self.lb.setPixmap(pixmap)
        # 设置标签的图像信息

        self.lb.setCursor(Qt.CrossCursor)
        # 设置鼠标在QLabel对象中的样式

        self.show()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
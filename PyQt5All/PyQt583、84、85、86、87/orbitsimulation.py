# -*- coding: utf-8 -*-

'''
这是一个简单的Graphics View小例子（地球绕太阳）！
文章链接：http://www.xdbcb8.com/archives/1612.html
文章链接：http://www.xdbcb8.com/archives/1621.html
文章链接：http://www.xdbcb8.com/archives/1635.html
文章链接：http://www.xdbcb8.com/archives/1640.html
文章链接：http://www.xdbcb8.com/archives/1645.html
'''

import sys
from PyQt5.QtCore import (QEasingCurve, QFileInfo, QLineF, QMimeData,
        QPoint, QPointF, QPropertyAnimation, QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QDrag, QImage, QPainter, QPen,
        QPixmap, QPainterPath)
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsView)

class Animation(QPropertyAnimation):
    '''
    动画类
    '''
    def __init__(self, target, prop):
        '''
        target, prop这个两个参数分别对应：动画的产生对象和setter
        '''
        super(Animation, self).__init__(target, prop)

    def updateCurrentTime(self, currentTime):
        '''
        currentTime（此属性保存动画的当前时间和进度）总是在变化的。
        每次动画的currentTime更改时，都会调用updateCurrentTime()函数
        '''
        self.m_path = QPainterPath()
        if self.m_path.isEmpty():
            end = self.endValue()
            start = self.startValue()
            # endValue()、startValue()分别表示动画的结束值和起始值
            self.m_path.addEllipse(QRectF(start, end))
            # 在指定的boundingRectangle内创建一个椭圆，这里是QRectF(start, end)，并将其作为封闭的子路径添加到painter路径中。

        dura = self.duration()
        progress = (((currentTime - 1) % dura) + 1) / float(dura)
        # duration()此属性保存动画的持续时间（以毫秒为单位）。 默认持续时间为250毫秒。progress则描绘了当前的完成比率。

        easedProgress = self.easingCurve().valueForProgress(progress)
        if easedProgress > 1.0:
            easedProgress -= 1.0
        elif easedProgress < 0:
            easedProgress += 1.0
        # 返回进度缓和曲线的有效进度。 进度必须介于0和1之间，而返回的有效进度可能超出这些范围。大于1就减1，小于0就加1。

        pt = self.m_path.pointAtPercent(easedProgress)
        # 返回当前路径的百分比easedProgress处的点。
        # 参数easedProgress必须介于0和1之间。当存在曲线时，百分比参数被映射到贝塞尔方程的t参数。

        self.updateCurrentValue(pt)
        # 每次动画的当前值更改时，都会调用updateCurrentValue()。pt参数是新的当前值。没有这个函数动画动不了。

        self.valueChanged.emit(pt)

    def startAnimation(self, startx, starty, endx, endy, duration):
        '''
        setStartValue()、setEndValue()分别表示设置动画的起止位置，setDuration()设置动画的运行时间。
        '''
        self.setStartValue(QPointF(startx, starty))
        self.setEndValue(QPointF(endx, endy))
        self.setDuration(duration)
        self.setLoopCount(-1)
        # 值为-1时，动画将永远循环直至停止

        self.start()
        # 开始运行动画

class PlanetTypeItem(QGraphicsItem):

    '''
    自定义QGraphicsItem类
    '''

    def __init__(self, PlanetType="sun"):
        super(PlanetTypeItem, self).__init__()

        self.type = PlanetType
        self.setCursor(Qt.OpenHandCursor)
        self.setAcceptedMouseButtons(Qt.LeftButton)
        # 设置下我们鼠标放在地球、太阳上的形状
    
    def boundingRect(self):
        '''
        这个纯虚函数将图元的外边界定义为矩形;
        所有绘画必须限制在图元的边界矩形内。
        QGraphicsView使用它来确定图元是否需要重绘。
        '''
        return QRectF(0, 0, 55, 55)

    def paint(self, painter, option, widget):
        '''
        这里画出太阳或者地球。先画出一个圆形，颜色是深灰色，其次是在深灰色的基础上画出具体的星球。
        '''
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(0, 0, 50, 50)
        root = QFileInfo(__file__).absolutePath()
        image = QImage(root + '/res/{}.png'.format(self.type))
        painter.drawImage(QRectF(0, 0, 50, 50), image)

    def mousePressEvent(self, event):
        '''
        当鼠标按下的时候，设置鼠标样式！
        '''
        self.setCursor(Qt.ClosedHandCursor)

    def mouseMoveEvent(self, event):
        '''
        拖动中我们所要显示的图形、鼠标样式
        '''

        drag = QDrag(event.widget())
        mime = QMimeData()
        drag.setMimeData(mime)

        root = QFileInfo(__file__).absolutePath()#绝对路径

        image = QImage(root + '/res/{}.png'.format(self.type))
        mime.setImageData(image)
        drag.setPixmap(QPixmap.fromImage(image).scaled(50, 50))
        drag.setHotSpot(QPoint(25, 25))

        drag.exec_()
        # 设置拖动中图像以及HotSpot

        self.setCursor(Qt.OpenHandCursor)
        # 设置鼠标样式

    def mouseReleaseEvent(self, event):
        '''
        设置鼠标释放后的样式
        '''
        self.setCursor(Qt.OpenHandCursor)

class Planet(QGraphicsObject):
    """
    行星基本属性：颜色是灰色的，定义了基本拖动离开以及放下的函数。
    """
    def __init__(self, parent=None):
        super(Planet, self).__init__(parent)

        self.color = QColor(Qt.lightGray)
        self.dragOver = False
        # dragOver这个变量，默认为False。self.dragOver的使用，主要是判断表示画面上是否覆盖东西了。

        self.setAcceptDrops(True)

    def dragLeaveEvent(self, event):
        '''
        拖动离开事件
        '''
        self.dragOver = False
        self.update()

    def dropEvent(self, event):
        '''
        放下事件
        '''
        self.dragOver = False
        self.update()

class Sun(Planet):
    '''
    太阳
    '''
    def __init__(self, parent=None):
        super(Sun, self).__init__(parent)
        self.pixmap = QPixmap()
        # 放置太阳图片

    def boundingRect(self):
        '''
        把太阳的大小先定义好
        '''
        return QRectF(0, 0, 95, 95)

    def paint(self, painter, option, widget=None):
        '''
        重写绘图函数
        '''
        if self.pixmap.isNull():
            # 要是没有图片的话
            painter.setBrush(self.color.lighter(130) if self.dragOver else self.color)
            # 给它图成一种颜色，要是覆盖上图片颜色就会变亮
            painter.drawEllipse(0, 0, 90, 90)
        else:
            painter.scale(.45, .45)
            # 按比例缩放坐标系，会把图片按一定比例缩小的。
            painter.drawPixmap(QPointF(0, 0), self.pixmap)
            # 在指定位置画出图片。
    
    def dragEnterEvent(self, event):
        '''
        拖入事件
        '''
        if event.mimeData().hasImage():
            event.setAccepted(True)
            self.dragOver = True
            self.update()

    def dropEvent(self, event):
        '''
        放下事件
        '''
        if event.mimeData().hasImage():
            self.dragOver = False
            self.pixmap = QPixmap(event.mimeData().imageData())
            self.update()

class Earth(Planet):
    '''
    地球
    '''
    def __init__(self, parent=None):
        super(Earth, self).__init__(parent)
        self.pixmap = QPixmap()

    def boundingRect(self):
        '''
        把地球大小定义好
        '''
        return QRectF(0, 0, 60, 60)
    
    def paint(self, painter, option, widget=None):
        '''
        重写绘图函数，和太阳一样的意思
        '''
        if self.pixmap.isNull():
            painter.setBrush(self.color.lighter(130) if self.dragOver else self.color)
            painter.drawEllipse(0, 0, 50, 50)
        else:
            painter.scale(.25, .25)
            painter.drawPixmap(QPointF(0, 0), self.pixmap)
    
    def dragEnterEvent(self, event):
        '''
        拖进事件
        '''
        if event.mimeData().hasImage():
            event.setAccepted(True)
            self.dragOver = True
            self.update()

    def dropEvent(self, event):
        '''
        放下
        '''
        if event.mimeData().hasImage():
            self.dragOver = False
            self.pixmap = QPixmap(event.mimeData().imageData())
            self.update()

class OrbitalSimulation():
    '''
    轨道模拟
    '''
    def __init__(self, scene):
        self.scene = scene
        self.sun = Sun()
        self.sun.setPos(-150, -50)
        self.scene.addItem(self.sun)

        self.earth = Earth()
        self.earth.setPos(-350, -25)
        self.scene.addItem(self.earth)
        # 将earth、sun加入到场景中。其中scene表示场景

        self.createPlanetTypeItem()
        self.createAnimation()

    def createPlanetTypeItem(self):
        '''
        这个函数是将地球、太阳的图片加入到场景中
        '''
        for i in range(2):
            item = PlanetTypeItem("earth") if i else PlanetTypeItem("sun")
            point1 = -200 * i/2 - 50.0
            item.setPos(point1, -250)
            self.scene.addItem(item)

    def createAnimation(self):
        '''
        动画曲线样式配置
        '''
        self.animEarth = Animation(self.earth, b'pos')
        self.animEarth.setEasingCurve(QEasingCurve.BezierSpline)
        # 允许使用三次贝塞尔曲线定义自定义缓动曲线
        self.animEarth.startAnimation(-300, -150, 200, 100, 10000)

if __name__== '__main__':

    app = QApplication(sys.argv)
    scene = QGraphicsScene(-512, -384, 1024, 768)
    # 场景
    orb = OrbitalSimulation(scene)
    # orb把相关的图元加入场景中
    view = QGraphicsView(scene)
    # view把场景加入到视图中
    view.setRenderHint(QPainter.Antialiasing)
    # 设置视图的抗锯齿渲染模式
    view.setBackgroundBrush(QColor(16, 27, 33))
    # 视图背景色
    view.setWindowTitle("公众号：学点编程吧--行星模拟")
    view.show()
    sys.exit(app.exec_())
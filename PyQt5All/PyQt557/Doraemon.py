#coding = utf-8

"""
一个关于哆啦A梦ドラえもん！（QPainter、QPainterPath的综合运用）的小例子！
文章链接：http://www.xdbcb8.com/archives/910.html
"""

import sys
import math
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QIcon, QPen, QFont, QTransform, QPainterPath, QPolygonF
from PyQt5.QtCore import QRectF, Qt, QPointF

class Doraemon(QWidget):

    '''
    画一个哆啦A梦
    '''

    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUi()
    
    def initUi(self):
        '''
        界面初始设置
        '''
        self.resize(1100, 612)
        self.setWindowTitle("微信公众号：学点编程吧--蓝胖子")
        self.setWindowIcon(QIcon("Doraemon.ico"))

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        qp.setPen(QPen(Qt.black, 4))
        # 在画画的开始我们就设置画笔的颜色（黑色）和粗细（4像素）

        self.drawFace(qp)
        self.drawEyes(qp)
        self.drawNose(qp)
        self.drawBeard(qp)
        self.drawMouth(qp)
        self.drawBody(qp)
        self.drawArm(qp)
        self.drawHands(qp)
        self.drawFeet(qp)
        self.drawText(qp)
        qp.end()

    def drawFace(self, qp):
        #画脸外轮廓
        path = QPainterPath()
        outdiameter = 376.0
        outre = QRectF(261.0, 30.0, outdiameter, outdiameter)
        outre_right_x = 261 + outdiameter/2 + outdiameter/2/math.sqrt(2)
        outre_right_y = 30 + outdiameter/2 + outdiameter/2/math.sqrt(2)
        path.moveTo(outre_right_x, outre_right_y)
        # 将painter路径的起始位置迁移到我们指定的坐标。
        path.arcTo(outre, -45, 270)
        # arcTo()创建一个占据给定矩形的弧，从指定的startAngle(-45度)开始并逆时针延伸sweepLength（270度）
        path.closeSubpath()
        # 通过在子路径的开头绘制一条线来关闭当前子路径，自动启动一个新路径
        qp.setBrush(QColor(156, 214, 239))
        # 给这个图形填充我们设置的颜色
        qp.drawPath(path)
        # 画出我们刚才设置的图形

        #画脸内轮廓
        path2 = QPainterPath()
        indiameter = 311.0
        inre = QRectF(301.0, 86.0, indiameter, indiameter)
        # 画矩形
        inre_right_x = 301 + indiameter/2 + indiameter/2/math.sqrt(2)
        inre_right_y = 86 + indiameter/2 + indiameter/2/math.sqrt(2)
        path2.moveTo(inre_right_x, inre_right_y)
        path2.arcTo(inre, -45, 270)
        path2.closeSubpath()
        qp.setBrush(Qt.white)
        qp.drawPath(path2)
    
    def drawEyes(self, qp):
        #画眼睛
        re_eye_out1 = QRectF(390.0, 61.0, 56.0, 71.0)
        qp.setBrush(Qt.white)
        qp.drawEllipse(re_eye_out1)
        # 画椭圆

        re_eye_out2 = QRectF(448.0, 61.0, 56.0, 71.0)
        qp.setBrush(Qt.white)
        qp.drawEllipse(re_eye_out2)

        #画眼珠
        re_eye_in1 = QRectF(420.0, 90.0, 13.0, 19.0)
        qp.setBrush(Qt.black)
        qp.drawEllipse(re_eye_in1)

        re_eye_in2 = QRectF(461.0, 90.0, 13.0, 19.0)
        qp.setBrush(Qt.black)
        qp.drawEllipse(re_eye_in2)

    def drawNose(self, qp):
        #画鼻子
        re_nose_out = QRectF(429.0, 124.0, 42.0, 42.0)
        qp.setBrush(Qt.red)
        qp.drawEllipse(re_nose_out)
        re_nose_in = QRectF(442.0, 137.0, 11.0, 11.0)
        qp.save()
        qp.setBrush(Qt.white)
        qp.setPen(QPen(Qt.white, 4))
        qp.drawEllipse(re_nose_in)
        qp.restore()
        # 可以通过调用save()函数随时保存QPainter的状态，该函数将所有可用设置保存在内部堆栈中。
        # restore()函数会弹回它们，即恢复原先的状态
        qp.drawLine(453, 165, 453, 239)
        # 画直线

    def drawBeard(self, qp):
        #画胡须
        qp.drawLine(310, 125, 388, 163)
        qp.drawLine(292, 182, 386, 183)
        qp.drawLine(375, 205, 291, 240)
        qp.drawLine(518, 150, 582, 111)
        qp.drawLine(529, 176, 613, 160)
        qp.drawLine(543, 200, 617, 225)

    def drawMouth(self, qp):
        #画嘴巴
        path3 = QPainterPath()
        mouth_diameter = 203.0
        mouthre = QRectF(352.0, 129.0, mouth_diameter, mouth_diameter)
        mouth_center_x = 352.0 + mouth_diameter/2
        mouth_center_y = 129.0 + mouth_diameter/2
        path3.moveTo(mouth_center_x, mouth_center_y)
        path3.arcTo(mouthre, 180, 180)
        path3.closeSubpath()
        qp.setBrush(QColor(219, 36, 28))
        qp.drawPath(path3)

    def drawBody(self, qp):
        #画身体
        path4 = QPainterPath()
        body_polygon = QPolygonF() 
        body_polygon << QPointF(316.0, 349.0) << QPointF(580.0, 349.0) << QPointF(577.0, 496.0) << QPointF(319.0, 496.0)
        # 绘制一个多边形
        path4.addPolygon(body_polygon)
        path4.closeSubpath()
        qp.setBrush(QColor(156, 214, 239))
        qp.drawPath(path4)

        #画肚子
        path5 = QPainterPath()
        belly_width = 180.0
        belly_length = 235.0
        bellyre = QRectF(365.0, 240.0, belly_width, belly_length)
        belly_center_x = 365.0 + belly_width/2
        belly_center_y = 240.0 + belly_length/2
        path5.moveTo(belly_center_x, belly_center_y)
        path5.arcTo(bellyre, 180, 180)
        path5.closeSubpath()
        qp.setBrush(Qt.white)
        qp.drawPath(path5)

        #画围兜
        path6 = QPainterPath()
        scarf_polygon = QPolygonF() 
        scarf_polygon << QPointF(316.0, 349.0) << QPointF(580.0, 349.0) << QPointF(450.0, 379.0) << QPointF(319.0, 349.0)
        path6.addPolygon(scarf_polygon)
        path6.closeSubpath()
        qp.setBrush(Qt.red)
        qp.drawPath(path6)

        #画铃铛
        bell_re = QRectF(442.0, 364.0, 30, 30)
        qp.setBrush(QColor(250, 221, 81))
        qp.drawEllipse(bell_re)
        qp.drawLine(455, 370, 465, 380)
        qp.drawLine(465, 380, 455, 385)

        #画口袋
        path7 = QPainterPath()
        pocket_width = 112.0
        pocket_length = 104.0
        pocketre = QRectF(400.0, 352.0, pocket_width, pocket_length)
        pocket_center_x = 412.0 + pocket_width/2
        pocket_center_y = 352.0 + pocket_length/2
        path7.moveTo(pocket_center_x, pocket_center_y)
        path7.arcTo(pocketre, 180, 180)
        path7.closeSubpath()
        qp.setBrush(Qt.white)
        qp.drawPath(path7)

    def drawArm(self, qp):
        #画左手臂
        path8 = QPainterPath()
        arm_left_polygon = QPolygonF() 
        arm_left_polygon << QPointF(316.0, 349.0) << QPointF(250.0, 462.0) << QPointF(267.0, 480.0) << QPointF(316.0, 393.0)
        path8.addPolygon(arm_left_polygon)
        path8.closeSubpath()
        qp.setBrush(QColor(156, 214, 239))
        qp.drawPath(path8)

        #画右手臂
        path9 = QPainterPath()
        arm_right_polygon = QPolygonF() 
        arm_right_polygon << QPointF(581.0, 353.0) << QPointF(691.0, 306.0) << QPointF(700.0, 329.0) << QPointF(581.0, 380.0)
        path9.addPolygon(arm_right_polygon)
        path9.closeSubpath()
        qp.setBrush(QColor(156, 214, 239))
        qp.drawPath(path9)

    def drawHands(self, qp):
        #画左手
        hand_left_re = QRectF(234.0, 455.0, 40.0, 40.0)
        qp.setBrush(Qt.white)
        qp.drawEllipse(hand_left_re)

        #画右手
        hand_right_re = QRectF(683.0, 295.0, 40.0, 40.0)
        qp.setBrush(Qt.white)
        qp.drawEllipse(hand_right_re)

    def drawFeet(self, qp):
        #画左脚
        foot_left_re = QRectF(304.0, 475.0, 146, 64)
        qp.setBrush(Qt.white)
        qp.drawEllipse(foot_left_re)

        #画右脚
        foot_right_re = QRectF(449.0, 475.0, 146, 64)
        qp.setBrush(Qt.white)
        qp.drawEllipse(foot_right_re)

    def drawText(self, qp):
        #画机器猫经典台词
        str1 = "爸爸说不要总是依赖别人"
        str2 = "这样永远都长不大"
        str3 = "所以要学会一个人成长"
        str4 = "哆啦A梦你说是吧！"
        qp.setPen(QPen(QColor(156, 214, 239), 4))
        qp.setFont(QFont("Microsoft YaHei", 20))
        qp.drawText(709, 132, str1)
        qp.drawText(709, 182, str2)
        qp.drawText(709, 232, str3)
        qp.drawText(709, 282, str4)
        # 要在图画中写字，我们使用setPen()、setFont()设置好颜色和字体。
        # 直接使用drawText()就行了，前两个参数是这行字出现顶点坐标
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    cat = Doraemon()
    cat.show()
    sys.exit(app.exec_())
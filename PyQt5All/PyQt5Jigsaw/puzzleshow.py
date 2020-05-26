#coding=utf-8

"""
这是一个关于5×5拼图的小例子！
文章链接：http://www.xdbcb8.com/archives/1150.html
文章链接：http://www.xdbcb8.com/archives/1164.html
文章链接：http://www.xdbcb8.com/archives/1184.html
文章链接：http://www.xdbcb8.com/archives/1202.html
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QRect, QDataStream, QIODevice, Qt, pyqtSignal, QPoint, QByteArray, QMimeData
from PyQt5.QtGui import QPixmap, QDrag, QPainter, QColor, QCursor

class PuzzleShow(QWidget):

    '''
    拼图的合成区
    '''

    puzzleCompleted = pyqtSignal()
    dropCompleted = pyqtSignal()

    def __init__(self, imageSize):
        super().__init__()
        self.imageSize = imageSize
        # 载入图片的大小

        self.inPlace = 0
        # 位置摆放正确的拼图数量

        self.piecePixmaps = []
        # 存储从拼图展示区拖到拼图合成区的拼图

        self.pieceRects = []
        # 存储拼图放到拼图合成区的目标矩形

        self.pieceLocations = []
        # 存储从拼图展示区拖到拼图合成区的拼图的位置

        self.highlightedRect = QRect()
        # 拼图放到拼图合成区的目标矩形，以高亮形式出现

        self.initUi()

    def initUi(self):
        self.setAcceptDrops(True)
        self.setMaximumSize(self.imageSize, self.imageSize)
        self.setMinimumSize(self.imageSize, self.imageSize)

    def dragEnterEvent(self, event):
        """
        鼠标移入准备拖动
        """
        if event.mimeData().hasFormat("image/x-puzzle-xdbcb8"):
            event.accept()
        else:
            event.ignore()
        # 鼠标移入准备拖动，因为你放置的拼图不一定合适，需要再次调整放置

    def dragLeaveEvent(self, event):
        """
        鼠标移开小窗口
        """
        updateRect = self.highlightedRect
        self.highlightedRect = QRect()
        self.update(updateRect)
        event.accept()
        # 避免多了一个高亮的矩形出来

    def dragMoveEvent(self, event):
        """
        拖动
        """
        updateRect = self.highlightedRect.united(self.targetSquare(event.pos()))
        # 两个矩形的拼接

        if event.mimeData().hasFormat("image/x-puzzle-xdbcb8") and self.findPiece(self.targetSquare(event.pos())) == -1:
            self.highlightedRect = self.targetSquare(event.pos())
            # 若我们拖动时符合要求的，我们将取得一个矩形，这个矩形就是我们可以放置在拼图合成区的目标矩形，并将其赋值给self.highlightedRect
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            self.highlightedRect = QRect()
            event.ignore()

        self.update(updateRect)

    def dropEvent(self, event):
        """
        拖动结束，图片落下
        """
        if event.mimeData().hasFormat("image/x-puzzle-xdbcb8") and self.findPiece(self.targetSquare(event.pos())) == -1:
            # 要是我们拖动的符合要求以及没有在存储目标矩形的列表中找到的话
            pieceData = event.mimeData().data("image/x-puzzle-xdbcb8")
            dataStream = QDataStream(pieceData, QIODevice.ReadOnly)
            square = self.targetSquare(event.pos())
            pixmap = QPixmap()
            location = QPoint()
            dataStream >> pixmap >> location

            self.pieceLocations.append(location)
            self.piecePixmaps.append(pixmap)
            self.pieceRects.append(square)
            # 把拖动拼图的位置、图片、以及目标矩形分别存入self.pieceLocations、self.piecePixmaps、self.pieceRects

            self.highlightedRect = QRect()
            self.update(square)
            # 必须要有这句话，否则，哼哼！
    
            event.setDropAction(Qt.MoveAction)
            event.accept()

            if location == QPoint(square.x()/self.pieceSize(), square.y()/self.pieceSize()):
                self.inPlace += 1
                # 要是我们放置的拼图位置和正确的拼图位置是一样的，self.inPlace += 1。
                if self.inPlace == 25:
                    self.puzzleCompleted.emit()
                    # 要是正确位置的拼图达到25个，发射puzzleCompleted信号。

        else:
            self.highlightedRect = QRect()
            event.ignore()

    def mousePressEvent(self, event):
        """
        鼠标按下事件（QWidget中是没有self.setDragEnabled(True)这个属性的。故我们重写了mousePressEvent方法）
        """
        square = self.targetSquare(event.pos())
        found = self.findPiece(square)
        if found == -1:
            return
        # 先看看鼠标点击的地方有没有我们的目标矩形，没有的话直接return，有的话返回相关的索引
        location = self.pieceLocations[found]
        pixmap = self.piecePixmaps[found]
        del self.pieceLocations[found]
        del self.piecePixmaps[found]
        del self.pieceRects[found]
    
        if location == QPoint(square.x()/self.pieceSize(), square.y()/self.pieceSize()):
            self.inPlace -= 1
        # 得到位置信息、拼图信息，并把它们从相关的列表中删除，当然拼图正确的总数也要减1
        self.update(square)
    
        itemData = QByteArray()
        dataStream = QDataStream(itemData, QIODevice.WriteOnly)
    
        dataStream << pixmap << location
        # 相关的变量放入数据流中。
    
        mimeData = QMimeData()
        mimeData.setData("image/x-puzzle-xdbcb8", itemData)
    
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - square.topLeft())
        drag.setPixmap(pixmap)
        # 新建一个QDrag对象，该对象中设置mimeData，HotSpot和图片信息
    
        if drag.exec(Qt.MoveAction) != Qt.MoveAction:
            self.pieceLocations.insert(found, location)
            self.piecePixmaps.insert(found, pixmap)
            self.pieceRects.insert(found, square)
            self.update(self.targetSquare(event.pos()))
    
            if location == QPoint(square.x()/self.pieceSize(), square.y()/self.pieceSize()):
                self.inPlace += 1
                # 正确的拼图数也要加上1

        # 要是drag不是拖动，那么我们给self.pieceLocations、self.piecePixmaps、self.pieceRects
        # 按照之前找到的索引增加位置、图片和目标矩形信息，相当于把之前删除掉的又加上

    def paintEvent(self, event):
        """
        绘画事件
        """
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), Qt.white)
        if self.highlightedRect.isValid():
            painter.setBrush(QColor("#E6E6FA"))
            painter.setPen(Qt.NoPen)
            painter.drawRect(self.highlightedRect.adjusted(0, 0, -1, -1))
            # 首先绘制目标矩形
    
        for i in range(len(self.pieceRects)):
            painter.drawPixmap(self.pieceRects[i], self.piecePixmaps[i])
        painter.end()
        # 到目前矩形后，要画出来，所以就重写绘图事件

    def targetSquare(self, position):
        """
        拼图放下的矩形位置
        """
        x = position.x()//self.pieceSize() * self.pieceSize()
        y = position.y()//self.pieceSize() * self.pieceSize()
        return QRect(x, y, self.pieceSize(), self.pieceSize())
        # x、y表示的是拼图放下具体矩形位置的x、y坐标，矩形的大小是拼图的大小

    def findPiece(self, piece_Rect):
        """
        找到拼图
        """
        try:
            return self.pieceRects.index(piece_Rect)
        except ValueError:
            return -1
        # 找一找拼图合成区中的单个拼图的矩形是否已经在pieceRects列表中，有的话返回索引，没有的话返回-1。
    
    def pieceSize(self):
        """
        单个拼图的大小
        """
        return int(self.imageSize // 5)

    def clear(self):
        """
        相关数据清空。这个我们在游戏初始化的时候会用到
        """
        self.piecePixmaps.clear()
        self.pieceRects = []
        self.pieceLocations = []
        self.highlightedRect = QRect()
        self.inPlace = 0
        self.update()
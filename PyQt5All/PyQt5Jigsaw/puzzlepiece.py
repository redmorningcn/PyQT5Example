#coding=utf-8

"""
这是一个关于5×5拼图的小例子！
文章链接：http://www.xdbcb8.com/archives/1150.html
文章链接：http://www.xdbcb8.com/archives/1164.html
文章链接：http://www.xdbcb8.com/archives/1184.html
文章链接：http://www.xdbcb8.com/archives/1202.html
"""

from PyQt5.QtWidgets import QListWidget, QApplication, QListView, QListWidgetItem
from PyQt5.QtGui import QPixmap, QDrag, QIcon
from PyQt5.QtCore import QSize, Qt, QByteArray, QDataStream, QIODevice, QPoint, QVariant, QMimeData

class PuzzlePiece(QListWidget):
    '''
    拼图块
    '''
    def __init__(self, pieceSize):
        '''
        一些初始设置
        '''
        super().__init__()
        self.pieceSize = pieceSize
        self.initUi()

    def initUi(self):
        '''
        一些界面设置
        '''
        self.setDragEnabled(True)
        # 保存视图是否支持拖动其自己的项目
        self.setViewMode(QListView.IconMode)
        self.setIconSize(QSize(self.pieceSize, self.pieceSize))
        self.setSpacing(10)
        self.setAcceptDrops(True)
        # 启用了放置事件

    def dragEnterEvent(self, event):
        """
        鼠标移入准备拖动
        """
        if event.mimeData().hasFormat("image/x-puzzle-xdbcb8"):
            event.accept()
        else:
            event.ignore()
        # QMimeData类型的数据是指定的MIME类型的数据”image/x-puzzle-xdbcb8”，则返回True，否则返回False。
        # TRUE我就接受事件，反之忽略事件
    
    def dragMoveEvent(self, event):
        """
        拖动
        """
        if event.mimeData().hasFormat("image/x-puzzle-xdbcb8"):
            event.setDropAction(Qt.MoveAction)
            # 设置拖动动作为Qt.MoveAction
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """
        拖动结束，图片落下
        """
        if event.mimeData().hasFormat("image/x-puzzle-xdbcb8"):
            piece = event.mimeData().data("image/x-puzzle-xdbcb8")
            dataStream = QDataStream(piece, QIODevice.ReadOnly)
            pixmap = QPixmap()
            location = QPoint()
            dataStream >> pixmap >> location
            self.addPiece(pixmap, location)
            # 当我们在拼图展示区放置拼图的时候，我们需要把数据流中的拼图信息取出来
            # 分别存入pixmap、location变量中，并通过addPiece()函数，增加一块拼图。
            event.setDropAction(Qt.MoveAction)
            # 设置放置动作为：Qt.MoveActio
            event.accept()
        else:
            event.ignore()
        

    def startDrag(self, DropActions):
        """
        开始拖
        """
        item = self.currentItem()
        # 表示一个小拼图
        itemData = QByteArray()
        # QByteArray类提供了一个字节数组
        dataStream = QDataStream(itemData, QIODevice.WriteOnly)
        # QDataStream类提供二进制数据到QIODevice的序列化
        piecePix = item.data(Qt.UserRole)
        pieceLocation = item.data(Qt.UserRole+1)
        # 返回给定角色的项目数据，这里分别是拼图本身和拼图的位置。
        # 这里的Qt.UserRole是特定于应用程序目的的角色。
        dataStream << piecePix << pieceLocation
        # 将拼图数据和拼图位置信息存入数据流中，注意：这里的操作符<<
        mimeData = QMimeData()
        mimeData.setData("image/x-puzzle-xdbcb8", itemData)
        # 构造一个没有数据的新MIME数据对象

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        # QDrag类支持基于MIME的拖放数据传输
        drag.setHotSpot(QPoint(piecePix.width()/2, piecePix.height()/2))
        # 光标的热点指向其底边的中心
        drag.setPixmap(piecePix)
        # 拖得时候显示的图片

        if drag.exec(Qt.MoveAction) == Qt.MoveAction:
            moveItem = self.takeItem(self.row(item))
            del moveItem
        # 把这个拼图从原来位置删除

    def addPiece(self, pix, loc):
        """
        增加一个拼图
        """
        puzzleItem = QListWidgetItem(self)
        puzzleItem.setIcon(QIcon(pix))
        puzzleItem.setData(Qt.UserRole, QVariant(pix))
        puzzleItem.setData(Qt.UserRole+1, loc)
        puzzleItem.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
        # QListWidgetItem时给其增加一些相应属性，例如图片、位置信息、拼图是否启用、是否可选、是否可以放置
# -*- coding: utf-8 -*-

"""
这是一个关于5×5拼图的小例子！
文章链接：http://www.xdbcb8.com/archives/1150.html
文章链接：http://www.xdbcb8.com/archives/1164.html
文章链接：http://www.xdbcb8.com/archives/1184.html
文章链接：http://www.xdbcb8.com/archives/1202.html
"""

import sys
import random
import os
import codecs
import pickle
from PyQt5.QtCore import pyqtSlot, QPoint, Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QHBoxLayout, QCheckBox, QDockWidget, QLabel
from PyQt5.QtGui import QPixmap
from puzzlepiece import PuzzlePiece
from puzzleshow import PuzzleShow
from Ui_main import Ui_MainWindow

class Jigsaw(QMainWindow, Ui_MainWindow):
    """
    拼图主程序
    """
    saveData = []

    def __init__(self, parent=None):
        """
        界面初始化
        载入历史时间
        记录时间初始化
        载入游戏
        """
        super(Jigsaw, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.puzzleImage = QPixmap("./img/Peppa.png")
        self.saveData = self.loadTime()
        self.dock2 = QDockWidget("完整的图片", self)
        self.dock2.resize(400, 400)
        self.setupPuzzle()
        self.initTimeUi()

    def initUi(self):
        """
        一些简单布局
        """
        self.setWindowFlags(Qt.Dialog)
        self.setWhatsThis("这是一个拼图小游戏")
        frameLayout = QHBoxLayout(self.frame)
        self.puzzleshow = PuzzleShow(400)
        self.puzzlepiece = PuzzlePiece(self.puzzleshow.pieceSize())
        frameLayout.addWidget(self.puzzlepiece)
        frameLayout.addWidget(self.puzzleshow)
        self.setCentralWidget(self.frame)

        self.puzzleshow.puzzleCompleted.connect(self.setCompleted)
        # 当我们完成游戏的时候会发出puzzleCompleted信号，这个信号是连接setCompleted()函数的
    
    def initTimeUi(self):
        """
        游戏时间初始化
        """
        self.dock = QDockWidget("游戏时间", self)
        self.label = QLabel("当前游戏用时：0秒，最佳时间：0秒")
        self.label.setStyleSheet("color: rgb(255, 0, 0);font: 14pt \"微软雅黑\";")
        self.dock.setWidget(self.label)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock)
    
    def setCompleted(self):
        """
        完成后弹出游戏结果对话框
        """
        self.timer.stop()
        self.saveData.append(self.time)
        self.saveTime()
        info = "恭喜通关成功！用时：{}秒，继续努力吧！\n按下OK继续！".format(self.time)
        QMessageBox.information(self, "通过成功", info, QMessageBox.Ok)
        self.setupPuzzle()
        # 游戏完成后，我们的定时器会停止。保存当前游戏时间。弹出恭喜对话框。游戏重新初始化（setupPuzzle()）
    
    def setupPuzzle(self):
        """
        游戏初始化
        """

        size = min(self.puzzleImage.width(), self.puzzleImage.height())
        #游戏图片尺寸
        
        self.puzzleImage = self.puzzleImage.copy((self.puzzleImage.width() - size)/2,
            (self.puzzleImage.height() - size)/2, size, size).scaled(self.puzzleshow.width(),
                self.puzzleshow.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        #得到压缩尺寸后的图形
        
        if self.puzzlepiece.count() > 1:
            self.puzzlepiece.clear()
            #只有在当前拼图列表存在拼图的情况下才能清空列表

        for y in range(5):
            for x in range(5):
                pieceSize = self.puzzleshow.pieceSize()
                piece = self.puzzleImage.copy(x * pieceSize, y * pieceSize, pieceSize, pieceSize)
                self.puzzlepiece.addPiece(piece, QPoint(x, y))
        #切割图片并添加到列表中
        
        for i in range(self.puzzlepiece.count()):
            if random.random() * 10 > 3:
                item = self.puzzlepiece.takeItem(i)
                self.puzzlepiece.insertItem(0, item)
        #图片随机排序
    
        self.puzzleshow.clear()
        #还原的图形展示小部件清空

        self.setDock(self.puzzleImage)
        #完整的图形刷新

        self.time = 0
        self.timing()

    def loadTime(self):
        """
        载入游戏时间数据
        """
        pathname = "m.dat"

        if not(os.path.exists(pathname) and os.path.isfile(pathname)):
            data = [100000]
            with codecs.open("m.dat", "wb") as f:
                pickle.dump(data, f)

        with codecs.open("m.dat", "rb") as f:
            data = pickle.load(f)
        return data

    def saveTime(self):
        """
        保存游戏时间
        """
        with codecs.open("m.dat", "wb") as f:
            pickle.dump(self.saveData, f)

    def timing(self):
        """
        开始计时
        """
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.second)
    
    def second(self):
        """
        显示游戏时间
        """
        self.time += 1
        timeinfo = "当前游戏用时：{}秒，最佳时间：{}秒".format(self.time, min(self.saveData))
        self.label.setText(timeinfo)

    def setDock(self, pix):
        """
        显示还原后的图片
        """
        label2 = QLabel()
        label2.setScaledContents(True)
        label2.setPixmap(pix)
        self.dock2.setWidget(label2)
        self.dock2.setFloating(True)

    @pyqtSlot()
    def on_action_O_triggered(self):
        """
        选择图片并开始游戏
        """
        fileName = QFileDialog.getOpenFileName(self, "打开文件", "./img", ("Images (*.png *.jpg)"))
        filepath = fileName[0]
        if filepath:
            self.puzzleImage = QPixmap(filepath)
            self.dock2.close()
            # 完成的拼图

            self.setupPuzzle()
            # 游戏初始化

            self.dock2.show()

            # 刷新一下这个画面，否则画面可能不会变
        else:
            QMessageBox.warning(self, "打开图片", "图片加载失败！", QMessageBox.Cancel)
            return


    @pyqtSlot()
    def on_action_E_triggered(self):
        """
        退出游戏
        """
        self.close()
        
    @pyqtSlot()
    def on_action_R_triggered(self):
        """
        重新开始游戏
        """
        self.setupPuzzle()

    @pyqtSlot()
    def on_action_P_triggered(self):
        """
        重新显示完成的图片
        """
        self.dock2.close()
        self.dock2.show()

    @pyqtSlot()
    def on_action_J_triggered(self):
        """
        关于
        """
        QMessageBox.information(self, "关于", "学点编程吧出品，必属精品！")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Jigsaw()
    game.show()
    sys.exit(app.exec_())

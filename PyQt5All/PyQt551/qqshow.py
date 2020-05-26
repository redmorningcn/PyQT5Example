# -*- coding: utf-8 -*-

"""
这是QQ秀 – 释放我不凡！（QStackedWidget的使用）的小例子！
文章链接：http://www.xdbcb8.com/archives/838.html
"""

import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from Ui_main import Ui_MainWindow
from selectsexy import SelectSexy
from selecthead import SelectHead
from selectcoat import SelectCoat
from selectpants import SelectPants

class QQShow(QMainWindow, Ui_MainWindow):
    
    sexy = ""
    # 性别

    head = ""
    # 头饰

    coat = ""
    # 衣着

    pants = ""
    # 裤子

    # 4个变量用于记录图片的路径信息

    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(QQShow, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
    
    def initUi(self):
        '''
        界面初始设置
        '''
        self.sexywidget = SelectSexy()
        self.headwidget = SelectHead()
        self.coatwidget = SelectCoat()
        self.pantswidget = SelectPants()

        self.stackedWidget.addWidget(self.sexywidget)
        self.stackedWidget.addWidget(self.headwidget)
        # 新建了性别、头型小部件（sexywidget、headwidget），然后添加到stackedWidget对象中

        self.stackedWidget.addWidget(self.coatwidget)
        self.stackedWidget.addWidget(self.pantswidget)
        # 同上

        self.sexywidget.pushButton.clicked.connect(self.unlockhead)
        # 性别页面→解锁→unlockhead()
        self.sexywidget.radioButton_man.toggled.connect(self.setman)
        # 性别页面→男→setman()
        self.sexywidget.radioButton_feman.toggled.connect(self.setfeman)
        # 性别页面→女→setfeman()

        self.headwidget.pushButton.clicked.connect(self.unlockcoat)
        # 头型页面→解锁→unlockcoat()
        self.headwidget.radioButton_head1.toggled.connect(self.sethead1)
        # 头型页面→头型1→sethead1()
        self.headwidget.radioButton_head2.toggled.connect(self.sethead2)
        # 头型页面→头型2→sethead2()
        self.headwidget.radioButton_head3.toggled.connect(self.sethead3)
        # 头型页面→头型3→sethead3()

        self.coatwidget.pushButton.clicked.connect(self.unlockpants)
        # 衣服页面→解锁→unlockpants()
        self.coatwidget.radioButton_coat1.toggled.connect(self.setcoat1)
        # 衣服页面→衣着1→setcoat1()
        self.coatwidget.radioButton_coat2.toggled.connect(self.setcoat2)
        # 衣服页面→衣着2→setcoat2()
        self.coatwidget.radioButton_coat3.toggled.connect(self.setcoat3)
        # 衣服页面→衣着3→setcoat3()

        self.pantswidget.radioButton_pants1.toggled.connect(self.setpants1)
        # 裤子页面→裤子1→setpants1()
        self.pantswidget.radioButton_pants2.toggled.connect(self.setpants2)
        # 裤子页面→裤子2→setpants2()
        self.pantswidget.radioButton_pants3.toggled.connect(self.setpants3)
        # 裤子页面→裤子3→setpants3()

    
    @pyqtSlot(int)
    def on_listWidget_currentRowChanged(self, p0):
        """
        选择造型
        """
        self.stackedWidget.setCurrentIndex(p0)
        # 当我们选择的QListWidget项目发生变化的时候，就会产生currentRowChanged()信号，并把当前项目的索引号带上。
        # 然后我们设定stackedWidget当前显示的QWidget的索引是当前QListWidget项目的索引。也就是根据选择切换不同的页面。
    
    @pyqtSlot(int)
    def on_stackedWidget_currentChanged(self, p0):
        """
        页面切换时，判断当前页面的单选按钮是否被选择过，要是没有则显示当前选项上一页面的造型。
        否则就是用我们保存在 sexy、head、coat、pants路径信息来显示帅哥、美女造型。
        一句话：科学选择，避免出现不科学的事实！
        """
        if p0 == 1:
            if self.headwidget.radioButton_head1.isChecked():
                self.headwidget.label.setPixmap(QPixmap(self.sexy + self.head + ".png"))
            elif self.headwidget.radioButton_head2.isChecked():
                self.headwidget.label.setPixmap(QPixmap(self.sexy +  self.head + ".png"))
            elif self.headwidget.radioButton_head3.isChecked():
                self.headwidget.label.setPixmap(QPixmap(self.sexy +  self.head + ".png"))
            else:
                self.headwidget.label.setPixmap(QPixmap(self.sexy + "sexy.png"))
        elif p0 == 2:
            if self.coatwidget.radioButton_coat1.isChecked():
                self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + ".png"))
            elif self.coatwidget.radioButton_coat2.isChecked():
                self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + ".png"))
            elif self.coatwidget.radioButton_coat3.isChecked():
                self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + ".png"))
            else:
                self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + ".png"))
        elif p0 == 3:
            if self.pantswidget.radioButton_pants1.isChecked():
                self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + self.pants + ".png"))
            elif self.pantswidget.radioButton_pants2.isChecked():
                self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + self.pants + ".png"))
            elif self.pantswidget.radioButton_pants3.isChecked():
                self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + self.pants + ".png"))
            else:
                self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + ".png"))

    def unlockhead(self):
        '''
        解锁头型
        '''
        if self.sexywidget.radioButton_man.isChecked() or self.sexywidget.radioButton_feman.isChecked():
            QMessageBox.information(self, "提示", "头型解锁成功！")
            self.sexywidget.pushButton.setEnabled(False)
            item = self.listWidget.item(1)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            # 设定第1个列表选项（从0开始的），使其可以使用和被选择。最开始是不能的，这点是在Qt设计师里面设定的。下同
        else:
            QMessageBox.information(self, "提示", "还没有选择男女呢？") 
            # 要是男、女都没有选择，你解锁的话，会提示不让你解锁的   

    def setman(self):
        '''
        让self.sexy记录下当前的男图片库，同时设定label显示男照片
        '''
        self.sexy = "./res/man/"
        self.sexywidget.label_sexy.setPixmap(QPixmap("./res/man/sexy.png"))

    def setfeman(self):
        '''
        让self.sexy记录下当前的女图片库，同时设定label显示女照片
        '''
        self.sexy = "./res/feman/"
        self.sexywidget.label_sexy.setPixmap(QPixmap("./res/feman/sexy.png"))

    def unlockcoat(self):
        '''
        解锁衣着
        '''
        if self.headwidget.radioButton_head1.isChecked() or self.headwidget.radioButton_head2.isChecked() or self.headwidget.radioButton_head3.isChecked():
            QMessageBox.information(self, "提示", "上衣解锁成功！")
            self.headwidget.pushButton.setEnabled(False)
            item = self.listWidget.item(2)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        else:
            QMessageBox.information(self, "提示", "还没有选择头型呢？")
    
    def sethead1(self):
        '''
        设置头型1
        '''
        self.headwidget.label.setPixmap(QPixmap(self.sexy + "1.png"))
        self.head = "1"

    def sethead2(self):
        '''
        设置头型2
        '''
        self.headwidget.label.setPixmap(QPixmap(self.sexy + "2.png"))
        self.head = "2"

    def sethead3(self):
        '''
        设置头型3
        '''
        self.headwidget.label.setPixmap(QPixmap(self.sexy + "3.png"))
        self.head = "3"

    def unlockpants(self):
        '''
        解锁裤子
        '''
        if self.coatwidget.radioButton_coat1.isChecked() or self.coatwidget.radioButton_coat2.isChecked() or self.coatwidget.radioButton_coat3.isChecked():
            QMessageBox.information(self, "提示", "裤子解锁成功！")
            self.coatwidget.pushButton.setEnabled(False)
            item = self.listWidget.item(3)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        else:
            QMessageBox.information(self, "提示", "还没有选择上衣呢？")
    
    def setcoat1(self):
        '''
        设置衣着1
        '''
        self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + "1.png"))
        self.coat = "1"

    def setcoat2(self):
        '''
        设置衣着2
        '''
        self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + "2.png"))
        self.coat = "2"

    def setcoat3(self):
        '''
        设置衣着3
        '''
        self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + "3.png"))
        self.coat = "3"

    def setpants1(self):
        '''
        设置裤子1
        '''
        self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + "1.png"))
        self.pants = "1"

    def setpants2(self):
        '''
        设置裤子2
        '''
        self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + "2.png"))
        self.pants = "2"

    def setpants3(self):
        '''
        设置裤子3
        '''
        self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + "3.png"))
        self.pants = "3"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qshow = QQShow()
    qshow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

"""
这是一个关于PyQt5与数据库互联（极简图书管理Plus）的小例子！
文章链接：http://www.xdbcb8.com/archives/1234.html
文章链接：http://www.xdbcb8.com/archives/1286.html
文章链接：http://www.xdbcb8.com/archives/1302.html
文章链接：http://www.xdbcb8.com/archives/1307.html
"""

from PyQt5.QtCore import pyqtSlot, QSize, Qt, QModelIndex
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QMenu, QAction, QHeaderView
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlTableModel
from createbook import CreateBook
from diySqltablemodel import BookSqlTableModel
from diyDelegate import TableDelegate
from Ui__mainUI import Ui_MainWindow


class Mbook(QMainWindow, Ui_MainWindow):
    """
    图书管理
    """
    def __init__(self, db, parent=None):
        """
        一些初始设置
        """
        super(Mbook, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.initUi()
        
    def initUi(self):
        '''
        界面初始设置
        '''
        self.splitter.setStretchFactor(0, 6)
        self.splitter.setStretchFactor(1, 4)
        # QSplitter按窗口索引增加伸缩因子

        searchkey = ["ISBN", "书名", "作者"]
        self.comboBox.addItems(searchkey)
        # 下拉框增加索引关键字

        self.tableView.setIconSize(QSize(55, 25))
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 表格的设置参见这篇文章，还比较全些：http://www.xdbcb8.com/archives/1414.html

        delegate = TableDelegate()
        self.tableView.setItemDelegate(delegate)
        # 调用我们自定义的代理

        self.setTableModel()

    @pyqtSlot(QModelIndex)
    def on_tableView_clicked(self, index):
        """
        单击显示图书详细信息
        """
        row = index.row()
        # 当我们单击表格的时候，取得行号。

        self.label_country.setText(self.tablemodel.record(row).value("country"))
        self.label_isbn.setText(self.tablemodel.record(row).value("isbn"))
        self.label_bookname.setText(self.tablemodel.record(row).value("subtitle"))
        self.label_author.setText(self.tablemodel.record(row).value("author"))
        self.label_publisher.setText(self.tablemodel.record(row).value("publisher"))
        self.label_price.setText(str(self.tablemodel.record(row).value("price")))
        self.label_pubdate.setText(self.tablemodel.record(row).value("pubdate"))
        self.label_classification.setText(self.tablemodel.record(row).value("classification"))           
        self.label_pages.setText(str(self.tablemodel.record(row).value("pages")))
        self.textBrowser.setText(self.tablemodel.record(row).value("summary"))
        imgPath = self.tablemodel.record(row).value("img")
        # 图片路径
        self.label.setPixmap(QPixmap(imgPath))

    @pyqtSlot()
    def on_pushButton_search_clicked(self):
        """
        查找图书
        """
        searchtext = self.lineEdit.text()
        if searchtext:
            if self.comboBox.currentText() == "ISBN":
                queryIsbn = "isbn = {}".format(searchtext)
                self.tablemodel.setFilter(queryIsbn)
                # 设置要过滤的当前过滤器。过滤器是不带关键字WHERE的SQL WHERE子句（例如，name =’Josephine’）。
                
            elif self.comboBox.currentText() == "书名":
                querySubtile = "subtitle = '{}'".format(searchtext)
                self.tablemodel.setFilter(querySubtile)
            elif self.comboBox.currentText() == "作者":
                queryAuthor= "author = '{}'".format(searchtext)
                self.tablemodel.setFilter(queryAuthor)
        else:
            self.setTableModel()

    @pyqtSlot()
    def on_pushButton_createbook_clicked(self):
        """
        新增图书
        """
        bookinfo = CreateBook(self.db)
        r = bookinfo.exec_()
        if r > 0:
            self.setTableModel()

    def setTableModel(self):
        """
        表格数据显示
        """
        self.tablemodel = BookSqlTableModel()
        self.tableView.setModel(self.tablemodel)
        # 设置要显示的视图的模型

        self.tablemodel.setEditStrategy(QSqlTableModel.OnFieldChange)
        # 设置数据库中的值编辑策略，这里是更改即保存到数据库

        self.tablemodel.setTable("books")
        self.tablemodel.select()
        # 要使用表的数据填充模型，请调用select()

        self.tablemodel.setHeaderData(0, Qt.Horizontal, "国家（地区）")
        self.tablemodel.setHeaderData(1, Qt.Horizontal, "ISBN")
        self.tablemodel.setHeaderData(2, Qt.Horizontal, "书名")
        self.tablemodel.setHeaderData(3, Qt.Horizontal, "作者")
        self.tablemodel.setHeaderData(4, Qt.Horizontal, "出版单位")
        self.tablemodel.setHeaderData(5, Qt.Horizontal, "图书分类")
        self.tablemodel.setHeaderData(6, Qt.Horizontal, "定价")
        # 设置表头内容

        self.tableView.hideColumn(7)
        self.tableView.hideColumn(8)
        self.tableView.hideColumn(9)
        self.tableView.hideColumn(10)
        # 隐藏不需要显示的数据

    def contextMenuEvent(self, event):
        """
        右键菜单
        """
        pmenu = QMenu(self)
        pDeleteAct = QAction('删除行',self.tableView)
        pmenu.addAction(pDeleteAct)
        pmenu.popup(self.mapToGlobal(event.pos()))
        pDeleteAct.triggered.connect(self.deleterows)
    
    def closeEvent(self, event):
        """
        关闭提示
        """
        r = QMessageBox.warning(self, "(*´∀｀*)　", "别急着走啊，再玩会？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if r == QMessageBox.No:
            event.accept()
        else:
            event.ignore()
    
    def filter(self, selectedIndexes):
        """
        过滤出选择的行
        """
        filtered = []
        for s in selectedIndexes:
            filtered.append(s.row())
        return list(set(filtered))
        # 根据返回的索引列表，去重一下，取得相应的行号。

    def deleterows(self):
        """
        删除行
        """
        rr = QMessageBox.warning(self, "注意", "确认删除数据？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if rr == QMessageBox.Yes:
            selectedIndexes = self.tableView.selectedIndexes()
            # 返回所有选定模型项索引的列表。

            selectedRows = self.filter(selectedIndexes)
            for row in reversed(selectedRows):
                self.tablemodel.removeRow(row)
                # 倒序删除
            self.tablemodel.select()
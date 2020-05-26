# -*- coding: utf-8 -*-

"""
这是一个关于PyQt5与数据库互联（极简图书管理Plus）的小例子！
文章链接：http://www.xdbcb8.com/archives/1234.html
文章链接：http://www.xdbcb8.com/archives/1286.html
文章链接：http://www.xdbcb8.com/archives/1302.html
文章链接：http://www.xdbcb8.com/archives/1307.html
"""

from io import BytesIO
import requests
from PIL import Image
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQuery
from Ui__bookinfoUI import Ui_Dialog
from getbookinfo import GetBookInfo

class CreateBook(QDialog, Ui_Dialog):
    """
    创建图书档案
    """ 
    def __init__(self, db, parent=None):
        """
        初始化一些信息，包括图书的一些属性，例如：ISBN号等
        """
        super(CreateBook, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.isbn = ""
        self.subtitle = ""
        self.author = ""
        self.pubdate = ""
        self.classification = ""
        self.publisher = ""
        self.price = ""
        self.pages = ""
        self.summary = ""
        self.img = ""
        self.country = ""
        self.header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
        }
        self.db = db

    def initUi(self):
        '''
        初始化部分图书信息，将分类增加进去。
        '''
        classifications = ["", "马克思主义、列宁主义、毛泽东思想、邓小平理论", "哲学、宗教", "社会科学总论", 
                    "政治、法律", "军事", "经济", "文化、科学、教育、体育", "语言、文字", "文学", 
                    "艺术", "历史、地理", "自然科学总论", "数理科学和化学", "天文学、地球科学", "生物科学", 
                    "医药、卫生", "农业科学", "工业技术", "交通运输", "航空、航天", "环境科学、劳动保护科学（安全科学）", 
                    "综合性图书"]
        self.comboBox.addItems(classifications)

    @pyqtSlot()
    def on_pushButton_read_clicked(self):
        """
        读取图书信息
        """
        self.isbn = self.lineEdit_isbn.text()
        if self.isbn == "":
            QMessageBox.warning(self, "警告", "ISBN号为空")
            self.lineEdit_isbn.setFocus()
            # 焦点移动到ISBN的输入栏，下同。
        else:
            book = GetBookInfo(self.isbn)
            rstatus, bookinfo = book.getbookinfo()
            if rstatus == "1":
                self.subtitle = bookinfo["subtitle"]
                self.author = bookinfo["author"]
                self.pubdate = bookinfo["pubdate"]
                self.classification = bookinfo["classification"]
                self.publisher = bookinfo["publisher"]
                self.price = bookinfo["price"]
                self.pages = bookinfo["pages"]
                self.summary = bookinfo["summary"]
                self.img = bookinfo["img"]
                self.country = bookinfo["country"]
                if self.pages.find("页") > 0:
                    self.pages = self.pages.replace("页", "")
                if self.price.find("元") > 0:
                    self.price = self.price.replace("元", "")
                    # 页、元替换成空
                self.set_bookinfo(self.subtitle, self.author, self.pubdate, self.classification, self.publisher, self.price, self.pages, self.summary, self.img)
            else:
                QMessageBox.warning(self, "警告", "大兄dei貌似查不到哦")
                self.lineEdit_isbn.setFocus()

    @pyqtSlot()
    def on_pushButton_chioce_clicked(self):
        """
        图书封面选择
        """
        f = QFileDialog.getOpenFileName(self, "选择图书封面", "./res/book/", ("Images (*.png *.jpg)"))
        if f[0]:
            self.label_pic.setPixmap(QPixmap(f[0]))
            self.img = f[0]
            # 封面路径

    def accept(self):
        """
        点击确认提交
        """
        if self.lineEdit_isbn.text() == "":
            QMessageBox.information(self, "提示", "ISBN号为空！")
        elif self.lineEdit_bookname.text() == "":
            QMessageBox.information(self, "提示", "书名为空！")
        elif self.lineEdit_author.text() == "":
            QMessageBox.information(self, "提示", "作者为空！")
        else:
            isbn = self.lineEdit_isbn.text()
            subtitle = self.lineEdit_bookname.text()
            author = self.lineEdit_author.text()
            pubdate = self.lineEdit_pudate.text()
            classification = self.comboBox.currentText()
            publisher = self.lineEdit_publisher.text()
            price = self.lineEdit_price.text()
            pages = self.lineEdit_pages.text()
            summary = self.textEdit_content.toPlainText()
            img = self.getImgPath(self.img)
            if not(self.country):
                if author[0] == "[" or author[0] == "【":
                    country = author[1]
                else:
                    country = "中"
            else:
                country = self.country
            query = QSqlQuery()
            insertBookInfo = "insert into books values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(country, isbn, subtitle, author, publisher, classification, price, pubdate, pages, summary, img)
            r = query.exec(insertBookInfo)
            if r:
                self.done(1)
            else:
                QMessageBox.information(self, "提示", "新增图书失败，貌似已经有相同的ISBN图书存在了！")
            self.db.close()
            
    def reject(self):
        """
        点击取消后
        """
        self.done(-1)
    
    def set_bookinfo(self, subtitle, author, pubdate, classification, publisher, price, pages, summary, img):
        """
        设置图书信息
        """
        self.lineEdit_bookname.setText(subtitle)
        self.lineEdit_author.setText(author)
        self.comboBox.setEditText(classification)
        self.lineEdit_publisher.setText(publisher)
        self.lineEdit_pudate.setText(pubdate)
        self.lineEdit_pages.setText(pages)
        self.lineEdit_price.setText(price)
        self.textEdit_content.setPlainText(summary)

        imgPath = self.getImgPath(img)
        response = requests.get(img, headers = self.header)
        image1 = Image.open(BytesIO(response.content))
        image1.save(imgPath)
        self.label_pic.setPixmap(QPixmap(imgPath))

    def getImgPath(self, img):
        """
        获得图书封面相对地址
        """
        imgPath = './res/book/' + img.split("/")[-1]
        return imgPath
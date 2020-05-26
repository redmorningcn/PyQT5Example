# -*- coding: utf-8 -*-

"""
这是一个关于PyQt5与数据库互联（极简图书管理Plus）的小例子！
文章链接：http://www.xdbcb8.com/archives/1234.html
文章链接：http://www.xdbcb8.com/archives/1286.html
文章链接：http://www.xdbcb8.com/archives/1302.html
文章链接：http://www.xdbcb8.com/archives/1307.html
"""

import sys
from mbook import Mbook
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtSql import QSqlDatabase

def connectDB():
    '''
    连接数据库
    '''
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("./res/db/book.db")
    # 数据库的路径
    if not db.open():
        QMessageBox.critical(None, "严重错误", "数据连接失败，程序无法使用，请按取消键退出", QMessageBox.Cancel)
        return False
    return db

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = connectDB()
    if db:
        mb = Mbook(db)
        mb.show()
        sys.exit(app.exec_())
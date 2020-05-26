# -*- coding: utf-8 -*-

"""
一个关于QTimer与QThread的综合应用举例的小例子！
文章链接：http://www.xdbcb8.com/archives/867.html
文章链接：http://www.xdbcb8.com/archives/870.html
文章链接：http://www.xdbcb8.com/archives/872.html
"""

import sys
from PyQt5.QtWidgets import QApplication
from diggingold import Gold

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gold = Gold()
    gold.show()
    sys.exit(app.exec_())
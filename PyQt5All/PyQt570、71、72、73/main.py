#coding = utf-8

"""
这是一个关于局域网群聊小工具Plus的小例子--带文件传输功能！
文章链接：http://www.xdbcb8.com/archives/1386.html
文章链接：http://www.xdbcb8.com/archives/1394.html
文章链接：http://www.xdbcb8.com/archives/1396.html
文章链接：http://www.xdbcb8.com/archives/1402.html
"""

import sys
from PyQt5.QtWidgets import QApplication
from chat_widget import Chat

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat = Chat()
    chat.show()
    sys.exit(app.exec_())
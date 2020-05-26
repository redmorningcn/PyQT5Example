#coding=utf-8

'''
这是一个关于标签（QLabel）的小例子-富文本例子！
文章链接：http://www.xdbcb8.com/archives/460.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Example(QWidget):
    '''
    富文本显示
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        界面初始设置
        '''
        self.resize(400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--标签:富文本（QLabel）')

        lb = QLabel(self)
        lb.resize(400, 200)
        
        html = '''
                <style type="text/css">
                    table.imagetable {
                        font-family: verdana,arial,sans-serif;
                        font-size:11px;
                        color:#333333;
                        border-width: 1px;
                        border-color: #999999;
                        border-collapse: collapse;
                    }
                    table.imagetable th {
                        background:#b5cfd2 url('cell-blue.jpg');
                        border-width: 1px;
                        padding: 8px;
                        border-style: solid;
                        border-color: #999999;
                    }
                    table.imagetable td {
                        background:#dcddc0 url('cell-grey.jpg');
                        border-width: 1px;
                        padding: 8px;
                        border-style: solid;
                        border-color: #999999;
                    }
                </style>

                <table class="imagetable">
                    <tr>
                        <th>Info Header 1</th><th>Info Header 2</th><th>Info Header 3</th>
                    </tr>
                    <tr>
                        <td>Text 1A</td><td>Text 1B</td><td>Text 1C</td>
                    </tr>
                    <tr>
                        <td>Text 2A</td><td>Text 2B</td><td>Text 2C</td>
                    </tr>
                </table>
            '''
        lb.setText(html)
        #把HTML中的内容以Web形式在QLabel中显示出来

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
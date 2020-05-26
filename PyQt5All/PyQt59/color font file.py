#conding=utf-8

'''
这是一个关于颜色、字体、打开文件对话框的小例子！
文章链接：http://www.xdbcb8.com/archives/274.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
# QColorDialog, QFontDialog, QFileDialog分别负责颜色选择对话框、字体选择对话框、打开文件对话框，QTextEdit则是将刚才提到的类的结果用于呈现。
# QTextEdit能够呈现富文本。

class Example(QWidget):
    '''
    颜色、字体、打开文件对话框
    '''
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        '''
        一些初始设置
        '''
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--记得好看点')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)
        
        self.bt1 = QPushButton('打开文件', self)
        self.bt1.move(350, 20)
        self.bt2 = QPushButton('选择字体', self)
        self.bt2.move(350, 70)
        self.bt3 = QPushButton('选择颜色', self)
        self.bt3.move(350, 120)
        
        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)
        
        self.show()
    
    def openfile(self):
        '''
        打开文件对话框的使用
        '''
        fname = QFileDialog.getOpenFileName(self, '打开文件', './')
        if fname[0]:
            with open(fname[0], 'r', encoding='gb18030', errors='ignore') as f:
                self.tx.setText(f.read())
            # 使用with语句来自动帮我们调用close()方法，避免由于文件读写时产生IOError，导致close()不会调用，用try ... finally来实现不太方便

    def choicefont(self):
        '''
        字体选择对话框的使用
        '''
        font, ok = QFontDialog.getFont()# getFont()方法返回字体名称以及用户点击按钮的状态
        if ok:
            self.tx.setCurrentFont(font)# 设置文本的字体信息为选择的字体信息
        
    def choicecolor(self):
        '''
        颜色选择对话框的使用
        '''
        col = QColorDialog.getColor()
        if col.isValid():# 检查颜色是否有效
            self.tx.setTextColor(col)# 设置文本颜色为选择的颜色
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
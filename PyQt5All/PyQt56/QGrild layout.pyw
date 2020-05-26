#coding = 'utf-8'

'''
这是一个格栅布局的小例子！
文章链接：http://www.xdbcb8.com/archives/209.html
'''

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLCDNumber)

class Example(QWidget):
    '''
    格栅布局
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        '''
        界面初始设置
        '''
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('学点编程吧-计算器')
        
        self.lcd = QLCDNumber()
        
        grid.addWidget(self.lcd, 0, 0, 3, 0)#我们使QLCDNumber小部件跨越4行
        grid.setSpacing(10)#将垂直和水平间距设置为10
        
        names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
                
        positions = [(i, j) for i in range(4, 9) for j in range(4, 8)]#将小部件添加到窗口中

        for position, name in zip(positions, names):
            #小部件的上的名称和它们的位置一一对应起来，注意zip的用法
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.Cli)
        
        self.show()
    
    def Cli(self):
        '''
        点击按钮时对应的槽函数
        '''
        sender = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.lcd.display('A')#当我们点击'/', '*', '-', '=', '+'时，LCD上显示'A'
        else:
            self.lcd.display(sender)#反之显示按钮上的名称，如：1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())

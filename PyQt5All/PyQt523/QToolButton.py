#coding=utf-8

'''
这是一个关于工具按钮（QToolButton）的小例子！
文章链接：http://www.xdbcb8.com/archives/489.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QToolButton, QMenu, QAction
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices

class Example(QWidget):
    '''
    工具按钮的使用
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
        self.setWindowTitle('关注微信公众号：学点编程吧--工具按钮（QToolButton）')

        tb = QToolButton(self)
        tb.move(100, 100)
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)# 文字出现在图标旁边
        # tb.setArrowType(Qt.DownArrow)# 设置按钮是否显示一个箭头，这里有好几种方式。
        tb.setPopupMode(QToolButton.InstantPopup)# 按下工具按钮菜单显示
        tb.setText('支付方式')
        tb.setIcon(QIcon('icon/bank.ico'))
        tb.setAutoRaise(True)# 启用自动浮起

        menu = QMenu(self)
        self.alipayAct = QAction(QIcon('icon/alipay.ico'), '支付宝支付', self)# 带图标的菜单
        self.wechatAct = QAction(QIcon('icon/wechat.ico'), '微信支付', self)
        self.visaAct = QAction(QIcon('icon/visa.ico'), 'Visa卡支付', self)
        self.master_cardAct = QAction(QIcon('icon/master_card.ico'), '万事达卡支付', self)
        menu.addAction(self.alipayAct)
        menu.addAction(self.wechatAct)
        menu.addSeparator()
        menu.addAction(self.visaAct)
        menu.addAction(self.master_cardAct)
        
        tb.setMenu(menu)
        self.show()
         
        self.alipayAct.triggered.connect(self.on_click)# 点击菜单后连接到相应的槽函数
        self.wechatAct.triggered.connect(self.on_click)
        self.visaAct.triggered.connect(self.on_click)
        self.master_cardAct.triggered.connect(self.on_click)
       
        
    def on_click(self):
        '''
        点击工具按钮触发网页打开
        '''
        if self.sender() == self.alipayAct:
            QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))# 打开对应的url，这里其实也可以使用Python的方式打开。
        elif self.sender() == self.wechatAct:
            QDesktopServices.openUrl(QUrl('https://pay.weixin.qq.com/index.php'))
        elif self.sender() == self.visaAct:
            QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))
        else:
            QDesktopServices.openUrl(QUrl('https://www.mastercard.com.cn/zh-cn.html'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

"""
这是一个关于PyQt5与数据库互联（极简图书管理Plus）的小例子！
文章链接：http://www.xdbcb8.com/archives/1234.html
文章链接：http://www.xdbcb8.com/archives/1286.html
文章链接：http://www.xdbcb8.com/archives/1302.html
文章链接：http://www.xdbcb8.com/archives/1307.html
"""

from PyQt5.QtWidgets import QStyledItemDelegate, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class TableDelegate(QStyledItemDelegate):
    '''
    自定义委托（代理）
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()

    def createEditor(self, parent, option, index):
        '''
        这个函数返回用于编辑index指定的项目以进行编辑的小部件。 父窗口小部件和样式选项用于控制编辑器窗口小部件的显示方式。

        parent：表示我们下面的小部件承载的位置。

        option：它是QStyleOptionViewItem对象。QStyleOptionViewItem类用于描述用于在视图窗口小部件中绘制Item的参数。
                QStyleOptionViewItem包含QStyle函数为Qt的模型/视图类绘制Item所需的所有信息。

        index：QModelIndex类对象，用于定位数据模型中的数据。
        '''
        editor = QComboBox(parent)
        editor.setIconSize(QSize(55, 25))
        # 首先创建一个下拉框，并设置它的图标大小。这里需要注意的是：parent，必须有

        if index.column() == 0:
            editor.addItem(QIcon("./res/countries/china.png"), "中")
            editor.addItem(QIcon("./res/countries/english.png"), "英")
            editor.addItem(QIcon("./res/countries/japan.png"), "日")
            editor.addItem(QIcon("./res/countries/russian.png"), "俄")
            editor.addItem(QIcon("./res/countries/usa.png"), "美")
            editor.addItem(QIcon("./res/countries/chile.png"), "智")
            editor.addItem(QIcon("./res/countries/default.png"), "其它国家")
            return editor
        elif index.column() == 5:
            classifications = ["", "马克思主义、列宁主义、毛泽东思想、邓小平理论", "哲学、宗教", "社会科学总论", 
            "政治、法律", "军事", "经济", "文化、科学、教育、体育", "语言、文字", "文学", 
            "艺术", "历史、地理", "自然科学总论", "数理科学和化学", "天文学、地球科学", "生物科学", 
            "医药、卫生", "农业科学", "工业技术", "交通运输", "航空、航天", "环境科学、劳动保护科学（安全科学）", 
            "综合性图书"]
            editor.addItems(classifications)
            editor.setEditable(True)
            return editor
            # 给第0列或者第5列的下拉框增加数据，并将这个下拉框返回
        else:
            return super().createEditor(parent, option, index)
            # 不是上面这种情况的话，调用父类默认的createEditor()函数
    
    def setEditorData(self, editor, index):
        '''
        从模型索引指定的数据模型项中通过编辑器显示和编辑的数据。
        当前表格里面是什么内容，我们双击显示下拉框里面的当前内容就是什么内容。
        '''
        if index.column() == 0 or index.column() == 5:
            text = index.model().data(index, Qt.EditRole)
            editor.setCurrentText(text)
        else:
            return super().setEditorData(editor, index)

    
    def setModelData(self, editor, model, index):
        '''
        从编辑器窗口小部件获取数据，并将其存储在项目索引处的指定模型中。
        默认实现从编辑器窗口小部件的用户属性获取要存储在数据模型中的值。
        '''
        if index.column() == 0 or index.column() == 5:
            strData = editor.currentText()
            model.setData(index, strData, Qt.EditRole)
        else:
            return super().setModelData(editor, model, index)

    def updateEditorGeometry(self, editor, option, index):
        '''
        重新绘制下拉框，你可以尝试注释看看效果
        '''
        editor.setGeometry(option.rect)
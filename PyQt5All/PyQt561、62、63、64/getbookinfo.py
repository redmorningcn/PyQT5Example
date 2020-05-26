# -*- coding: utf-8 -*-

"""
这是一个关于PyQt5与数据库互联（极简图书管理Plus）的小例子！
文章链接：http://www.xdbcb8.com/archives/1234.html
文章链接：http://www.xdbcb8.com/archives/1286.html
文章链接：http://www.xdbcb8.com/archives/1302.html
文章链接：http://www.xdbcb8.com/archives/1307.html
"""

import json
import requests

class GetBookInfo:

    '''
    获取图书信息
    '''

    def __init__(self, isbn):
        '''
        弄一个默认的ISBN号
        '''
        if isbn == "":
            self.isbn = "1234567890123"
        else:
            self.isbn = isbn
    
    def getbookinfo(self):
        """
        利用豆瓣API读取图书信息
        """
        url = "https://api.douban.com/v2/book/isbn/:" + self.isbn
        header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
        }
        try:
            r = requests.get(url, headers=header)
            info = r.text
        except Exception as e:
            print(e)
            return
        # 获取图书信息，要是出现异常就抛出

        bookinfo_dic = json.loads(info)
        bookinfo = {"subtitle" : "", "author": "", "pubdate" : "", "classification" : "",
                        "publisher" : "", "price" : "", "pages" : "", "summary" : "", "img" : "", "country" : ""           
            }

        if bookinfo_dic.get("code"):
            rstatus = "0"
            return rstatus, bookinfo
        else:
            rstatus = "1"
            subtitle = bookinfo_dic["title"]
            author = " ".join(bookinfo_dic["author"])
            pubdate = bookinfo_dic["pubdate"]
            classification = bookinfo_dic["tags"][1]["title"]
            publisher =  bookinfo_dic["publisher"]
            price = bookinfo_dic["price"]
            pages = bookinfo_dic["pages"]
            summary = bookinfo_dic["summary"]
            img = bookinfo_dic["images"]["small"].replace("\\", "")
            if author[0] == "[" or author[0] == "【":
                country = author[1]
            else:
                country = "中"
            bookinfo = {"subtitle" : subtitle, "author": author, "pubdate" : pubdate, "classification" : classification,
                        "publisher" : publisher, "price" : price, "pages" : pages, "summary" : summary, "img" : img, "country" : country            
            }
            return rstatus, bookinfo
            # 获取图书信息并放入到bookinfo的字典中，以及是否成功状态
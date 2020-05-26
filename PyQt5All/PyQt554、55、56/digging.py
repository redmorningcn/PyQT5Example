# -*- coding: utf-8 -*-

"""
一个关于QTimer与QThread的综合应用举例的小例子！
文章链接：http://www.xdbcb8.com/archives/867.html
文章链接：http://www.xdbcb8.com/archives/870.html
文章链接：http://www.xdbcb8.com/archives/872.html
"""

import itertools
import codecs
import random
import bisect
import time
import os

class Ore:
    '''
    具体挖矿工作
    '''
    def __init__(self, sec):
        '''
        一些初始设置
        '''
        self.second = sec
        # 期望的挖矿时间

        self.goldnum = 0
        # 挖矿数量

        self.start = time.clock()
        # 实际开始挖矿时间

        if os.path.exists('gold.gd'):
            # 先看看有没有矿池：gold.gd这个文件，没有的话给它创建这个文件，并写入一个空字符串
            with codecs.open('gold.gd', 'w', 'utf-8') as f:
                f.write('\x00')

    def digging(self):
        '''
        筛选金矿
        '''
        ore_list = [i for i in range(256)]
        # 我们建立一个0-255的列表，每个元素对应具体的ASCII

        weights = [100 for i in range(256)]
        weights[170] = 5
        # 得到的矿石（每一个ASCII码）都是随机的，但是金矿相对于其他矿石来说，含量更低，被挖到的可能性更小。
        # 别的矿石都是100，它只有5。除非挖矿的时间长，否则出现的几率小。

        cumdist = list(itertools.accumulate(weights))
        # 使用itertools.accumulate对权重进行累加

        x = random.random() * cumdist[-1]
        # 我们利用random.random()与最后一个cumdist相乘，random.random()的范围是浮点数0.0-1.0（不含）

        isgold = ore_list[bisect.bisect(cumdist, x)]
        # bisect.bisect(cumdist, x)返回的是在有序列表cumdist中要插入元素x，返回其需要插入的位置。
        # 这个位置在ore_list中的元素就是我们需要挖取矿石

        # 因为金矿的权重和其它矿石相比权重很低，在itertools.accumulate(weights)列表中
        # 这个插入点的位置出现的情况就会比较少，间接造成金矿出现的几率少

        with codecs.open('gold.gd', 'a', 'utf-8') as f:
            f.write(chr(isgold))
        if isgold == 170:
            return 1
        return 0
        # 返回是否是金矿的信息，是返回1，否返回0

    def begin_dig(self):
        '''
        循环挖矿中
        '''
        while True:
            gold = self.digging()
            if gold == 1:
                self.goldnum += 1
            end = time.clock ()
            besec = int(end - self.start)
            if besec == self.second:
                break
            # 挖矿时间到了之后停止循环
        return self.goldnum
        # 把金矿数量返回
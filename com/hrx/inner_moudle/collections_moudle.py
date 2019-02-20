#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 下午10:31
# @Author  : Aries
# @Site    :
# @File    : collections_moudle.py
# @Software: PyCharm

# collections是Python内建的一个集合模块，提供了许多有用的集合类。
# dict 其中的两种构造
from collections import namedtuple

d = dict(id='1', name='tony')
d = dict([(1, 2), (2, 3)])
containsKey = 8 if 1 in d else 0
print(containsKey)


def haha():
	print(1)


print("-----------------------------------------namedtuple-----------------------------------------------------------")
# 定义一个tuple 是以一个obj的形式 point 会有点的属性    ---- 创建一个类似tuple属性的class
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)


# 同样定义一个circle

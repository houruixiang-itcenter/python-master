#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 下午7:01
# @Author  : Aries
# @Site    : 
# @File    : itertools_moudle.py
# @Software: PyCharm

# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数


# todo 无限的迭代器
import itertools

# it = itertools.count(1)
# for i in it:
#     print(i)

# todo 无限重复当前str cycle()
# cy = itertools.cycle('hou')
# for c in cy:
#     print(c)

# todo 无限重复当前str repeat() 但是可以指明次数
# re = itertools.repeat('LA', 3)
# for r in re:
#     print(r)

# todo 添加条件 进行截取 比如:
# it1 = itertools.count(1)
# ns = itertools.takewhile(lambda x: x < 10, it1)
# for n in ns:
#     print(n)

# todo 将两个字符串串联起来 chain()
# for c in itertools.chain('HRX', 'HRX'):
#     print(c)

# todo  把相邻的重复字符挑出来 groupby()
for key, group in itertools.groupby('AAABBBNNNNNNn'):
    print(key, list(group))

s = 'a'
print(s.upper())
print(s)

# todo 忽略大小写进行比较
for key, group in itertools.groupby('AAABBBNNNNNNn', lambda i: i.upper()):
    print(key, list(group))

# 小结
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。

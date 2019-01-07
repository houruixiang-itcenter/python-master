#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 下午5:45
# @Author  : Aries
# @Site    : 
# @File    : m2.py
# @Software: PyCharm


# todo python 高阶函数
from com.hrx.simple.function import command


class m2:
    # 相当于空构造
    def __init__(self):
        pass


# todo sort test 假设我们用一组tuple表示学生名字和成绩 L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# todo 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=command.by_name))
print(sorted(L, key=command.by_score, reverse=True))

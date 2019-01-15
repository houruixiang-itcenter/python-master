#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 下午7:26
# @Author  : Aries
# @Site    : 
# @File    : Person.py
# @Software: PyCharm

class Person:
    def __init__(self):
        pass
    # 使用__slots__关键字限制属性  只能添加 name和age这两个属性
    __slots__ = ('name', 'age')

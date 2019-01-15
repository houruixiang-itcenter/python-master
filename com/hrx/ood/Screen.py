#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 下午8:36
# @Author  : Aries
# @Site    : 
# @File    : Screen.py
# @Software: PyCharm

class Screen:
    pass

    def __init__(self):
        pass

    # 因为此时的width方法已经变成了属性，调用的时候直接self.width，所以内部的数据要用self._width更合适，否则会重名造成嵌套死循环
    # 循环次数过多的时候就会造成错误：
    # RecursionError: maximum recursion depth exceeded
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        self._width = val

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self._height = val

    @property
    def resolution(self):
        return 786432

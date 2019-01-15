#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 下午8:21
# @Author  : Aries
# @Site    :
# @File    : Doctor.py
# @Software: PyCharm
from com.hrx.ood.Person import Person


class Docter(Person):
    pass

    # 在实际中,有时候我们要通过set/get来操作属性 这样出于解耦封装的考虑 其作用之一就是可以检查属性
    # 但是调用起来显然没有xx.属性开起来没关方便 那么有没有调用方便 又具备set/get有点的方法呢
    # 那么 我们接着看@property  这是一个装饰器  类似之前打log时用到的装饰器decorator

    # 这样 就把方法 set/get  直接变成了属性  瞒天过海
    @property  # 对应get方法
    def score(self):
        return self._score

    @score.setter  # 对应set方法
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def age(self):
        return 2015 - self._birth

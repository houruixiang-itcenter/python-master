#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 下午6:02
# @Author  : Aries
# @Site    : 
# @File    : Dog.py
# @Software: PyCharm
from com.hrx.ood.Animal import Animal

# 为了统计Dog数，可以给dOG类增加一个类属性，每创建一个实例，该属性自动增加：
class Dog(Animal):
    count = 0

    def __init__(self):

        self.count = self.count + 1
        pass

    age = 18
    name = 'john'
    form = 'china'

    def run(self):
        print('dog is running')

    def print_this(self):
        print('hallo my son')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 下午6:02
# @Author  : Aries
# @Site    : 
# @File    : Dog.py
# @Software: PyCharm
from com.hrx.ood.Animal import Animal

# 为了统计Pig数，可以给Pig类增加一个类属性，每创建一个实例，该属性自动增加：
class Pig(Animal):
    count = 0

    def __init__(self):

        Pig.count = Pig.count + 1
        pass


    def run(self):
        print('pig is running')

    def print_this(self):
        print('hallo my son')

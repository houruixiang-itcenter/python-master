#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 下午4:51
# @Author  : Aries
# @Site    : 
# @File    : odd_test.py
# @Software: PyCharm
from com.hrx.ood.Cat import Cat
from com.hrx.ood.Dog import Dog
from com.hrx.ood.Student import Student


class Ood:
    def __init__(self):
        pass

    s = Student('小明', '18')
    print(s.get_age())
    print(s.get_name())

    s1 = Student()
    print(s1.get_age())
    print(s1.get_name())


    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()

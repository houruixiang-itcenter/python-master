#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/6 下午3:27
# @Author  : Aries
# @Site    : 
# @File    : Student.py
# @Software: PyCharm
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if 80 > self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'

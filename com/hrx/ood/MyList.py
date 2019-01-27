#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 下午9:24
# @Author  : Aries
# @Site    :
# @File    : MyList.py
# @Software: PyCharm


# metaclass是类的模板，所以必须从`type`类型派生：
class Metaclass(type):
	def __new__(cls, name, base, attrs):
		print(name)
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, base, attrs)


class MyList(list, metaclass=Metaclass):
	pass

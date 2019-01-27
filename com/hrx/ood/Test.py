#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 下午8:28
# @Author  : Aries
# @Site    :
# @File    : Test.py
# @Software: PyCharm
from enum import Enum


class Ood_test(object):
	def __init__(self, name):
		self.name = name
		self.a, self.b = 0, 1
	
	def __str__(self):
		return "test __str__ (name %s)" % self.name
	
	__repr__ = __str__
	
	def __iter__(self):
		return self
	
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.b > 10000:
			raise StopIteration()
		return self.a, self.b
	
	# 注意 这里使用 __getitem__关键字  参数的作用决定 循环几次 所以从外面 调用看起来 这个类就像一个 list  可以根据索引取到值
	def __getitem__(self, item):
		if isinstance(item, int):
			a, b = 1, 1
			for x in range(item):
				a, b = b, a + b
			return a
		elif isinstance(item, slice):
			start = item.start
			stop = item.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L


class Ood_test1(object):
	
	def __init__(self):
		self.name = "feng"
	
	def __getattr__(self, item):
		if item != "name":
			return "libai"
	
	def __getitem__(self, item):
		return self.dict[item]
	
	dict = {}
	
	def __setitem__(self, key, value):
		self.dict[key] = value
	
	def __delitem__(self, key):
		self.dict.pop(key)


class Chain(object):
	
	def __init__(self, path=''):
		print("__init__")
		self._path = path
	
	def __getattr__(self, path):
		print("__getattr__")
		return Chain('%s/%s' % (self._path, path))
	
	def __str__(self):
		print("__call__")
		return self._path
	
	def __call__(self, args):
		print("__call__")
		return Chain('%s/%s' % (self._path, args))
	
	__repr__ = __str__


class TT(object):
	def __init__(self, name):
		self.name = name
	
	def __call__(self):
		print('My name is %s.' % self.name)


class Gender(Enum):
	Male = 0
	Female = 1


class Doctor(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

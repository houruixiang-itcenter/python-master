#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 下午10:31
# @Author  : Aries
# @Site    :
# @File    : collections_moudle.py
# @Software: PyCharm

# collections是Python内建的一个集合模块，提供了许多有用的集合类。
# dict 其中的两种构造
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

d = dict(id='1', name='tony')
d = dict([(1, 2), (2, 3)])
containsKey = 8 if 1 in d else 0
print(containsKey)


def haha():
	print(1)


print("--------------------------------------namedtuple对齐tuple--------------------------------------------------------")
# 定义一个tuple 是以一个obj的形式 point 会有点的属性    ---- 创建一个类似tuple属性的class
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# 同样定义一个circle
Circle = namedtuple('circle', ['x', 'y', 'z'])
c = Circle(1, 2, 3)
print(c.x, c.y, c.z)

print("-----------------------------------------deque对其list-----------------------------------------------------------")
# list是线性存储的 类似于java的数组 所以按索引查询比较快  插入删除慢一点
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('r')
# 这个内建模块 相当于是对list的一个加工  优化插入进而删除的效率 并且提供了appendleft和popleft的api  更加方便了操作


print("--------------------------------------defaultdict对其dict--------------------------------------------------------")
d = defaultdict(lambda: 'N/A')
d['key'] = 'adc'
print(d['key'], d['1111'])

print("--------------------------------------OrderedDict对其dict--------------------------------------------------------")
o = OrderedDict([('a', 1), ('z', 10), ('b', 3)])
print(o)
# dict 是无序的  而OrderedDict是有序的
print("------------------------------OrderedDict实现一个FIFO(先进先出)-------------------------------------------------")


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):
	
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity
	
	def __setitem__(self, key, value):
		
		containsKey = 1 if key in self else 0
		
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)


print("------------------------------------------ChainMap------------------------------------------------------")
print("-----------------------------------------Counter-------------------------------------------------------")
c = Counter()
d = dict([])
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)

# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
#
# 小结
# collections模块提供了一些有用的集合类，可以根据需要选用。



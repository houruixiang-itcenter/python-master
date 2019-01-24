#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 下午4:59
# @Author  : Aries
# @Site    :
# @File    : m1.py
# @Software: PyCharm

# python高级特性
from collections.abc import Iterable

from com.hrx.simple.function import command


class m1:
    # 相当于空构造
    def __init__(self):
        pass


# todo python python高级特性 --- 切片
# 在python的list/tuple中取其中元素
# 如  case1:取前3个    但是 case2:取前30个
# case1:
L = list(range(100))

print(L[0], L[1], L[2])

# 去前N个
i = 0
while i < 30:
    print(L[i], end=' ')
    i = i + 1

#  可以 看到当取的个数较多时候 就要通过循环来取了
#  todo 下面的程序 均为list  tuple也同样适用
#  对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
print('-------------------------------切片------------------------------------------')
#  注意 有一个原则 包前  不包后
print(L[0])
print(L[:3])
print(L[1:3])
# 倒着取
print(L[-1])
print(L[-3:])
print(L[-3:-1])

# 隔n个 取一个
print(L[:10:3])

# 取全部
print(L[:])

# todo 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
print(command.trim('    hello!'))

# 测试:
if command.trim('hello  ') != 'hello':
    print('测试失败!')
elif command.trim('  hello') != 'hello':
    print('测试失败!')
elif command.trim('  hello  ') != 'hello':
    print('测试失败!')
elif command.trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif command.trim('') != '':
    print('测试失败!')
elif command.trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

print('-------------------------------迭代------------------------------------------')
# 首先 python的迭代  是和js为一个级别  抽象程度高于java和c  只要是可迭代对象 就可以迭代
# 迭代 字典 dict
d = {'数学': 95, '语文': 88, '英语': 100}
# 获取 key
for k in d:
    print(k, end=' ')
print()
# 获取 value
for v in d.values():
    print(v, end=' ')
print()
# 获取 key + value
for k, v in d.items():
    print('key: ', k, 'value: ', v, end=' ')
print()

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# 判断当前的元素集合是否可以迭代  --- 其实就是 类型检查 当前的集合是否位collections的Iterable
print(isinstance([1, 2, 3], Iterable))
print(isinstance('abc', Iterable))
print(isinstance(100, Iterable))

# python中遍历list 怎么拿到value和索引呢
# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['哈哈', '呵呵', '嘿嘿']):
    print(i, ':::', value, end=' ')
print()

# 还有在list中每个元素 不是仅仅一个变量
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y, end=' ')
print()

# todo 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
# 测试
if command.findMinAndMax([]) != (None, None):
    print('测试失败!')
elif command.findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif command.findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif command.findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

print('-------------------------------列表生成式------------------------------------------')
# 生成list
list = list(range(10))
# 现在要生成一个 1*1,2*2...的一个list
# L = []
# for x in range(1, 11):
# 	L.append(x * x)
# 可以利用python的强大公式 列表生成器
# 利用列表生成器 可以写出特别简洁的代码
print([x * x for x in list])

# todo 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple']
L2 = [s.lower() if isinstance(s, str) else s for s in L1]
print('列表生成式TEST ', L2)

print('-------------------------------生成式------------------------------------------')
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。
#
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 创建 generator 第一种方法 []--->()
g = (x * x for x in range(10))
print(g)
#  取其中的元素
print(next(g))
print(next(g))
print(next(g))
print('...')
for item in g:
    print(item, end=' ')
print()

# 注意 当生成器数组越界时候  会抛出异常  StopIteration
# generator非常强大 如果推荐算法比较复杂 用类似生成式的for循环无法实现的时候,还可以用函数来实现
# 实例一  斐波那契数列<不死神兔>
print(command.fib(10))

# 将其改造为一个生成器 首先要符合一下要求
# 1.解决内存问题  2.可以 使用next取数据 类似于java中的游标
#  使用yield
print('-------------------------------斐波那契生成式------------------------------------------')
fg = command.generator_fib(5)  # 获取斐波那契数列的生成器
#  测试
while True:
    try:
        i = next(fg)
        print('generator_fib: ', i)
    except StopIteration as e:
        print('generator StopIteration')
        break
print('-------------------------------杨辉三角形生成式------------------------------------------')
#  测试
tg = command.triangles(5)
#  初始化自定义gennerator时候 初始化 是不执行的 --- 原因 断点function无反应
while True:
    try:
        i = next(tg)
        print('generator_fib: ', i)
    except StopIteration as e:
        print('generator StopIteration')
        break

print('-------------------------------迭代器------------------------------------------')

# Iterator是迭代器  Iterable是可迭代对象

# 可以直接作用于for循环的数据类型有以下几种：
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。



# 需要注意的是  list、tuple、dict、set、str是 Iterable 可迭代对象
# 而generator，包括生成器和带yield的generator function是 Iterator 迭代器


# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

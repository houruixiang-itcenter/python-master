#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 上午10:48
# @Author  : Aries
# @Site    :
# @File    : m3.py
# @Software: PyCharm

# todo  函数式编程  1---返回函数  2---匿名函数  3---装饰器 4---偏函数
from com.hrx.simple.function import command


class m3:
    def __init__(self):
        pass


# 1-返回函数
print('-------------------------------1-返回函数------------------------------------------')
# python中高阶函数 不仅可以接受函数作为参数  还可以将函数做为返回值返回
# 在python中定义方法有一下 不同的特性
# todo  1.函数内部 支持定义函数   2.函数的参数可以是函数  返回值 也可以是函数  3.函数可以对象化  函数名可以理解为函数对象
f = command.lazy_sum(1, 2, 3)
print(f())

# 同样 函数做为返回 即使参数相同 返回的函数对象也是相互独立的
f1 = command.lazy_sum(1, 2, 3)
print(f == f1)

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 闭包就是能够读取其他函数内部变量的函数。例如在javascript中，只有函数内部的子函数才能读取局部变量，
# 所以闭包可以理解成“定义在一个函数内部的函数“。在本质上，闭包是将函数内部和函数外部连接起来的桥梁。
print('-------------------------------闭包------------------------------------------')
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易
l = command.count()
for i in l:
    print(i())
l1 = command.count_1()
l2 = command.count_1()
l3 = command.count_1()
print(len(l1), ':::', len(l2), ':::', len(l3))
for i in l1:
    print(i())
# l = [1, 2, 3, 4]
# print(l(), l(), l())


# todo 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# 测试:
counterA = command.createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = command.createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print('-------------------------------方案2------------------------------------------')
counterA = command.createCounter_1()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = command.createCounter_1()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print('-------------------------------方案3------------------------------------------')
counterA = command.createCounter_2()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = command.createCounter_2()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 2-匿名函数
print('-------------------------------2-匿名函数------------------------------------------')
# 匿名函数 其实就是 lambda表达式来构建函数  之前 map有提供
# todo 匿名函数的优点:1.调用简单 2.不会有function重名的风险
# todo 匿名函数的缺点:不能 构建 return返回值的函数
f = lambda x: x * x
print(f(3))

# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1
# L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)

# 3-装饰器
print('-------------------------------3-装饰器------------------------------------------')
# 在python中 函数也是一个变量 我们可以调用他
# 获取function的name
# print(command.now.__name__)
# command.now()
# command.now_1()

f = command.log(command.now)
f()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 下午10:47
# @Author  : Aries
# @Site    :
# @File    : command.py
# @Software: PyCharm

# 引用
from typing import Dict

from com.hrx.simple.function import command


class test5:

    def __init__(self):
        pass


# python 调用函数
print('-------------------------------调用函数------------------------------------------')

# abs 取正整数  在python中调用API即函数时候 参数类型/参数数目不对 编译器会抛出TypeError
print(abs(100))

# max求最大值函数   参数数目不限定
print(max(0, 1))
print(max(0, 1, 2, 6))

print('-------------------------------数据类型转换------------------------------------------')

# python中基本数据类型 对应同名的function  可以任意转换
print(int('111'))
print(float(1))
print(str(12.90))
print(bool(22))
print(bool(0))

print('-------------------------------定义函数------------------------------------------')

print(command.my_abs(99))


# 如果想定义一个什么事也不做的空函数，可以用pass语句： --- 缺少了pass，代码运行就会有语法错误。
def nop():
    pass


# 类型检查

# print(command.my_abs_check('哈哈'))

# 返回多个值的函数
print(command.move(100, 1000, 1))

print('-------------------------------函数的参数------------------------------------------')

# python的函数定义非常简单,但是灵活度却非常大.除了正常的必选参数外,还可以使用
# todo 默认参数
# todo 可变参数
# todo 关键字参数
# 是的函数定义出来的接口,不但能处理复杂的参数,还可以建华调用者的代码


print('-------------------------------位置参数------------------------------------------')
# 调用普通function  1参  and  两参
print(command.power_1(10))
print(command.power_2(10, 3))

print(command.power_common(10))
print(command.power_common(10, 3))

print('-------------------------------默认参数------------------------------------------')
# 但是需要注意  默认参数 必须是不可变对象 这样会导致默认值随着函数的调用发生改变
command.print_error()
command.print_error()
command.print_error(['hallo'])

command.print_curr(['end'])
command.print_curr()

print('-------------------------------可变参数------------------------------------------')
#  可变参数 顾名思义 就是传入参数的个数是可变的
#  计算 a2 + b2 + c2 + ……
#  但是 调用时候要事先组装一个list 或者tuple  作为参数
print(command.calc([1, 2, 3]))

# 简化一下 在python中 在一个参数 num前面加* 即*num可以把num转化为一个简单的多参数(用,隔开  类似于java中的value...),而这个num就是tuple或者list
#  这样来说 nums = [1, 2, 3] 那么*num = 1,2,3 这样更加符合一个函数的传参
print(command.calc_command(1, 2, 3))

print('-------------------------------可变参数 + *------------------------------------------')
# 也就是说 一个list 或者tuple  可以直接加* 号传入
nums = [1, 2, 3]
print(command.calc_command(nums[0], nums[1], nums[2]))
print(command.calc_command(*nums))

print('-------------------------------关键参数------------------------------------------')
# 关键参数  其实就是对一个函数的扩展
# 其中**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
# 比如 设定 一个person属性的输出函数  首先 name  age 是必传参数,不同的person有不同的特性 比如 小A会飞 小B会叫 这时候 就需要定义一个关键字参数
extra = {'city': 'Beijing', 'job': 'Engineer'}
hallo = {'语文': '90', '数学': '88'}
command.print_person_info2('张三', 18, city='北京')
command.print_person_info2('张三', 18, **extra)
command.print_person_info2('张三', 18, **hallo)
# 注意这样 print(**extra)是没有结果的
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# ，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

print('-------------------------------命名关键参数------------------------------------------')
command.person('jhon', 56, city='beijing', job='docter')
command.person_defult('bob', 20)


# 参数组合
# 在Python中定义函数，
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


print('-------------------------------递归函数------------------------------------------')
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
print(command.fact(100))
print(command.fact_init(100))

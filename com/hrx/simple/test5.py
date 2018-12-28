#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 下午10:47
# @Author  : Aries
# @Site    :
# @File    : command.py
# @Software: PyCharm

# 引用
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






































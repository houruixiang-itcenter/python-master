#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 下午10:47
# @Author  : Aries
# @Site    :
# @File    : test5.py
# @Software: PyCharm


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

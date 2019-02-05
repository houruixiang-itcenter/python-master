#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/5 下午10:55
# @Author  : Aries
# @Site    : 
# @File    : err_raise.py
# @Software: PyCharm
print("------------------------------------------抛出问题---------------------------------------------------")


# class FooError(ValueError):
#     pass
#
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
#
# foo('0')

# 捕获异常仅仅为了程序可以继续执行 而继续在捕获后抛出异常 是为了 让调用者知道是什么异常 其实两者并不冲突
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        # raise


bar()


# 小结
# Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
#
# 程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。



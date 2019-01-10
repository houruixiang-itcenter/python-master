#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 下午4:42
# @Author  : Aries
# @Site    :
# @File    : m4.py
# @Software: PyCharm

# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' todo 模块  1--使用模块  2--安装第三方模块 '

# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
__author__ = 'houruixiang'

# 使用sys模块的第一步，就是导入该模块：
import sys

import com.hrx.middle.m3


class m4:
    def __init__(self):
        pass


# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

a = 2

# 与java中的main  方法差不多 执行类的时候会执行 但是被其他类引用时候不会执行
if __name__ == '__main__':
    test()

# 这有一个小插曲 当用控制台执行python文件的时候   会报一个错can't open file 'm4.py': [Errno 2] No such file or directory
# 这是路径的问题  比较低级  暂时记录一下

# 在python中也有修饰符
# todo 但是是通过变量命名来实现的  没有像java那样的public private  protected
'''public --- abc'''
'''private --- _abc或者__abc'''
# todo 但是需要注意的是python中的所谓public 和private仅仅是定义上的区分  并不是不可以引用 而是不应该 更像是一种到的约束


# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，
# __name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test2.py


"""
1.python 的基本数据类型
2.python 格式  输入输出
"""

from __future__ import print_function


class test2:
    def __init__(self):
        pass

    if True:
        print("Answer")
        print("True")
        import sys;
        x = 'runoob';
        sys.stdout.write(x + '\n')
    else:
        print("Answer")
        # 没有严格缩进，在执行时会报错
    print("False")
    x = 'a'
    y = 'b'
    # python默认输出是换行的, 如果不换行需要在末尾加”, ”
    print(x)
    print(y)
    var = x, y
    print(x, y)
    print(x, end='')
    print(y, )
    print("------------------------")
    if x.__eq__(y):
        print("===")
    else:
        print("!=")
    print("LALO")
    # 像if、while 、def和class这样的复合语句，首行以关键字开始，以冒号(: )
    #     结束，该行之后的一行或多行代码构成代码组。
    #
    # 我们将首行及后面的代码组称为一个子句(clause)。
    expression = True
    uint = False
    if expression:
        print("expression")
    elif uint:
        print("uint")
    else:
        print("life is short i use python")
    print("你好你好")

    # -*- coding: UTF-8 -*-
    # print "你好，世界";
    # print('100 + 200 =', 100 + 200);
    # name = input()
    # print('hello,', name)

    # py中一些输出的格式
    print('i love u')
    print("'i love u'")
    print("'i \"love u'")
    # r''表示转义符失效
    print(r"'i \"love u'")
    print('------------------------------------------------r-----------------------------------------------------')
    print(r'''hello,\n
    world''')
    # '''...'''代表多行展示
    print('''
    line1
    line2
    line3''')

    # 布尔值
    # 在py中布尔值 用首字母大写标识 True  False
    print(True)
    print(False)
    print(2 > 3)
    print(1 == 1)
    print('hallo' == 'hallo')

    # 布尔值可以用and、or和not运算。
    # and运算是与运算，只有所有都为True，and运算结果才是True：
    print(True and True, True and False)
    print(True or True, True or False)
    print(not True, not False)

    # 空值
    # 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
    # 此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。

    # 变量
    # 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
    # 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，比如：

    a = 123
    b = 0.111
    c = 'haha'
    print(a)
    print(b)
    print(c)
    # print a + c

    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)

    # python中也有常量 但是他不像java中final可以限定死 所以就格式上与众不同而已  通常位大写
    PI = 3

    # 这里来一个 小插曲 python的运算符
    print(9 / 3)
    print(10 / 3)
    print(10 // 3)
    print(10 % 3)
    l1 = r'''Hello,\'
    Lisa!'''
    l2 = '''Hello,\'
    Lisa!'''
    l3 = r'Hello, "Bart"'
    l4 = 'Hello, "Bart"'
    print(l1)
    print(l2)
    print(l3)
    print(l4)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 下午4:51
# @Author  : Aries
# @Site    :
# @File    : odd_test.py
# @Software: PyCharm

# todo python中面向对象的高级编程
from com.hrx.ood.Test import Ood_test1, Ood_test


class Ood_Height:
    def __init__(self):
        pass

    # 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
    #
    # __slots__我们已经知道怎么用了，__len__()
    # 方法我们也知道是为了能让class作用于len()
    # 函数。
    #
    # 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

    print("------------------------------------__str__-----------------------------------------------------")
    # __str__类似于java中的toString  用于输出 类的一系列信息
    t = Ood_test("lily")
    print(t)
    # 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()
    # 返回用户看到的字符串，而__repr__()
    # 返回程序开发者看到的字符串，也就是说，__repr__()
    # 是为调试服务的。
    #
    # 解决办法是再定义一个__repr__()。但是通常__str__()
    # 和__repr__()
    # 代码都是一样的，所以，有个偷懒的写法：

    # todo 在终端 进行输出时候  不加 print  直接输出对象是有问题的 所以 一般定义 __str__时候 应该定义__repr__  这里__repr__=__str__就好
    t = Ood_test("xte")
    print(t)

    print("------------------------------------__iter__-----------------------------------------------------")
    # __iter__ 就是把一个类变成一个可被迭代的对象  如list/tuple 当然需要定义__next__ 这样才符合可迭代对象的特性
    for item in t:
        print(item)

    print("------------------------------------__getitem__-----------------------------------------------------")
    # 虽然 __iter__可以满足list遍历的特性但是 如果要 取对应索引的元素 还是不行的  所以 我们要使用__getitem__
    print(t[5])
    # 接着实现切片
    print(t[1:9])
    # 也没有对负数作处理，所以，要正确实现一个__getitem__()
    # 还是有很多工作要做的。
    #
    # 此外，如果把对象看成dict，__getitem__()
    # 的参数也可能是一个可以作key的object，例如str。
    #
    # 与之对应的是__setitem__()
    # 方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()
    # 方法，用于删除某个元素。
    #
    # 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，
    # 不需要强制继承某个接口。

    # todo  __getitem__做为唯一输出口  所以 __setitem__/__delitem__必须配合__getitem__使用
    t1 = Ood_test1()
    t1["lili"] = 18
    t1["momo"] = 30
    print(t1["lili"])
    del t1["lili"]
    print(t1["momo"])

    # todo 需要注意一下  __str__ __repr__类似于java的toString  输出obj时候 调用
    # todo __iter__调用 for...in  时候 被调用 __next__就是调用next
    # todo 这几个方法作用于可迭代对象  __setitem__设置元素  __delitem__删除元素 __getitem__获取元素
    # todo 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。其实就是一个容错处理

    print("------------------------------------__getattr__-----------------------------------------------------")

    # 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
    #
    # 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，
    # 我们就要按照约定，抛出AttributeError的错误：

    print(t1.name)
    print(t1.abc)
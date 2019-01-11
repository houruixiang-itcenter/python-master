#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 上午10:49
# @Author  : Aries
# @Site    :
# @File    : Student.py
# @Software: PyCharm

''' 类和实例  访问限制 '''


# 定义 类 类名首字母大写  --- python同样是面向对象的语言
class Student(object):
    pass

    # def __init__(self):
    #     pass

    # 类似于java中的构造方法  self是java中的this  可以自己构造参数
    # todo 注意python中不可以有多个构造  这是因为python的函数比较强大 一个函数 可以代替java中的多构造
    # todo 之前 有提到 位置参数 默认参数 可变参数 命名关键字参数
    # todo 这里 我们使用默认参数 来实现 java的多构造
    def __init__(self, name='hrx', age='26'):
        # 当然 既然本来提供了操作内部数据的API即方法 当然
        # todo 1.保证内部数据的安全性  外部不可对当前类进行修改 2.是外部调用简单 解耦
        # todo  这时候是否会怀念java中private修饰符 当然在python中是没有private的  但是只需要在变量前面加__即可
        # todo 但是需要注意一点 这里__ 也不是真的不能访问  只不过python把__name变量改成了_Student__name  确实有点假
        # 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
        # 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
        #
        # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
        # 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
        # todo 如下所示
        self.__name = name
        self.__age = age
        pass

    #  数据封装
    # 其实就是 当前类使用一些 function组成一些数据封装  为其他类暴露相应API 进行调用
    # 这样即方便调用  数据也比较安全
    # todo 当然 外部想要获取属性  可以通过set-get方法来获取修改
    # todo 这样做的目的 是为了封装解耦 也可以看做是一种OOD编程的习惯  这样set/get来设置/输出数据 可以根据需求定制化一些需求 如写一些钩子等
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # 这里可以封装一堆对外提供的API
    def print_std(std):
        print('%s: %s' % (std.__name, std.__score))

    # 既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数
    # ，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：

    # 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
    #
    # 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
    #
    # 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
    #
    # 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

    # 注意再python中与类关联起来 对类中数据进行相应的操作  对外而言就行类似API的暴露 这种函数被称为方法

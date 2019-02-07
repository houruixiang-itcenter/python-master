#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/7 下午12:31
# @Author  : Aries
# @Site    : 
# @File    : pick.py
# @Software: PyCharm

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，
# marshalling，flattening等等，都是一个意思。

# todo 正如java中一样 有些数据不支持sp存储,或者不支持传输,所以我们需要序列化之后再存储或者传输,然后通过反序列化取出,python也是如此
# todo python中序列化 pickling  反序列化是unpickling
import json
import pickle

print(
    "------------------------------------------**序列化**------------------------------------------------")

# todo 第一种 不需要写入文件
d = dict(id='1', name='tony')
# 将数据序列化为只有python认识的字符串
p_str = pickle.dumps(d)
# 将序列化后得到的字符串 反序列化为python的原始数据结构
print(pickle.loads(p_str))

# todo 第二种 写入文件
# open时候  没有文件会自动创建
# todo 序列化
l = ['1', '2', '3']
f = open('dump.txt', 'wb')
pickle.dump(l, f)
f.close()

# todo 反序列化
f = open('dump.txt', 'rb')
print(pickle.load(f))
f.close()

# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
#
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

print("------------------------------------------**JSON --- 通用**------------------------------------------------")
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
# 因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，
# 并且比XML更快，而且可以直接在Web页面中读取，非常方便。
# todo 如果对传输效率 有要求可以使用google的pb协议 要比json 快10倍左右吧
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

# JSON类型	    Python类型
# {}	        dict
# []	        list
# "string"	    str
# 1234.56	    int或float
# true/false	True/False
# null	        None

# todo python 内置de json模块就实现 python对象 --> json  / json --> python对象之间的转换
d = {'name': 'lily', 'age': 18, 'sex': '男'}
# python对象序列化为json 字符串
json_str = json.dumps(d)
print(json_str)
# json字符串反序列化为python对象
print(json.loads(json_str))\

# 同样可以使用 json.dump(x,f)/json.load(f)这种写入文件的形式进行json的序列化和反序列化


# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
#
# import json
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('Bob', 20, 88)
# print(json.dumps(s))
# 运行代码，毫不留情地得到一个TypeError：
#
# Traceback (most recent call last):
#   ...
# TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
# 错误的原因是Student对象不是一个可序列化为JSON的对象。
#
# 如果连class的实例对象都无法序列化为JSON，这肯定不合理！
#
# 别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
#
# https://docs.python.org/3/library/json.html#json.dumps
#
# 这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
#
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
#
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
#
# >>> print(json.dumps(s, default=student2dict))
# {"age": 20, "name": "Bob", "score": 88}
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
#
# print(json.dumps(s, default=lambda obj: obj.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
#
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
#
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
# 运行结果如下：
#
# >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# >>> print(json.loads(json_str, object_hook=dict2student))
# <__main__.Student object at 0x10cd3c190>
# 打印出的是反序列化的Student实例对象。



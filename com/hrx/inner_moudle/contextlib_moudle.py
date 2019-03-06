#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 下午7:25
# @Author  : Aries
# @Site    :
# @File    : contextlib_moudle.py
# @Software: PyCharm

# todo contextlib上下文管理器
# 在python中,像读写资源这样的操作,操作完后必须关闭他们
from contextlib import contextmanager

try:
    f = open('hallo.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 当然 可以简化 try...finally  是不是很熟悉
with open('hallo.txt', 'r') as f:
    print(f.read())


# todo 可以看到这种try...finally的方式 可以避免使用完  忘记close的风险 这样的模式类似java中的代理类 可以在使用前后进行行为的插入
# todo 这里需要用到__enter__和__exit__下面来看

class Person(object):

    def __init__(self):
        print("init")
        pass

    def __enter__(self):
        print("Begin")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('END')

    def run(self):
        print('hello ,I am lily')


with Person() as p:
    p.run()


# 从上面来看这样 重写方法还是有一点麻烦 所以我们可以进一步优化使用contextlib中的注解@contextmanager实现上面的效果
class Anim(object):

    def __init__(self):
        pass

    def run(self):
        print('haha')


@contextmanager
def open():
    print('Begin')
    a = Anim()
    yield a
    print('END')


with open() as a:
    a.run()

print('-----------------------------------------------------------------------------------------------------------')


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

# 代码的执行顺序是：
#
# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。
# 因此，@contextmanager让我们通过编写generator来简化上下文管理。

print('----------------------------------------------@closing-----------------------------------------------------')
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
# 它的作用就是把任意对象变为上下文对象，并支持with语句。
#
# @contextlib还有一些其他decorator，便于我们编写更简洁的代码。
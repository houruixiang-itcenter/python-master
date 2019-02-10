#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/9 下午9:37
# @Author  : Aries
# @Site    : 
# @File    : treadlocal.py
# @Software: PyCharm

# 在线程中 每一个线程会有自己的数据 所以每个线程会使用一个局部变量来存储当前线程的数据 全局变量的使用必须加锁 所以不予以使用
# 但是 这样的话局部变量就要在每个线程所调用的func中做为参数一直传递下去  那么如果调用100的方法 就要传递100次参数 显然不合理

# todo 那么我们可以定义一个全局的dict,通过key-value的形式存储 key:thread value:data
import threading

from com.hrx.processThread.Person import Person

global_dict = {}


def do_task1():
    print(global_dict[threading.current_thread()])
    pass


def do_task2():
    pass


def p_thread(name):
    p = Person(name)
    global_dict[threading.current_thread()] = p
    print(" ", threading.current_thread())
    do_task1()
    do_task2()


p_thread("libai")

# 这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。
#
# 有没有更简单的方式？
#
# ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事
print("-----------------------------------------------thraeadlocal--------------------------------------------------")

data_local = threading.local()


def run_task(name):
    data_local.name = name
    print("hallo Mr %s (in %s)" % (data_local.name, threading.current_thread().name))


t1 = threading.Thread(target=run_task, args=("hrx",))
t2 = threading.Thread(target=run_task, args=("syf",))
t1.start()
t2.start()
t1.join()
t2.join()

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，
# 但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
#
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
#
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。


# 小结
# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

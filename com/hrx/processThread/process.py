#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/8 下午9:23
# @Author  : Aries
# @Site    :
# @File    : process.py
# @Software: PyCharm

# 要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
# unix/linux提供了一个fork()系统调用,用来fork出子进程;fork一次会有两次调用,有两次回调,当前进程通过fork()复制一份子进程

# todo 进程可以类比与高架桥 可能进程间通讯会麻烦一点  开销也会大一点   但是不会巧夺cpu  而且每个任务线之间是完全解耦的
# todo 线程可以必须成红绿灯 可以在一定程度上保证多任务 但是共享一个内存 进行抢夺 并不可以完全解耦 即使加锁也不能完全保证并行

# todo 需要注意的是  fork一次 会返回两次的pid   子进程返回的是0  父进程返回的是 fork的子进程
import os

# 获取当前进程 :getpid()  获取当前进程的父进程 :getppid()
# import random
# import time
# from multiprocessing import Process
# from multiprocessing.pool import Pool
import os
import time
from multiprocessing import Process, Queue
from multiprocessing.pool import Pool
from random import random

# print("当前进程开始...", os.getpid())
# pid = os.fork()
# if pid == 0:
#     print("fork出的子进程为  %s  其父进程为 %s" % (os.getpid(), os.getppid()))
# elif pid != 0:
#     print("原始进程为 %s 通过fork产出的子进程为 %s" % (os.getpid(), pid))

# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，
# 推荐大家用Mac学Python！
#
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，
# 每当有新的http请求时，就fork出子进程来处理新的http请求。


print("----------------------------------------------multiprocessing--------------------------------------------------")


# 在linux下 子进程是通过fork出来的  但是在windows下开发python该怎么进行创建新进程呢
# 在windows下通过python提供的一个模块 multiprocessing 中Process的构造来创建一个新的进程
# 类似于java多线程中的tunnable
def run_thread(name):
    print("run  current process :name = %s ,pid = %s" % (name, os.getpid()))


if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_thread, args=("test",))
    print("process create success")
    p.start()
    p.join()
    print("process run end...")

# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     s = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     s.start()
#     s.join()
#     print('Child process end.')


print("----------------------------------------------pool--------------------------------------------------")


# 同样的如果要创建多个子进程  需要创建进程池   好拗口 其实和线程池是一个作用
def run_pool(name):
    print("run  current process :name = %s ,pid = %s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 2)
    end = time.time()
    print("current process run time: %s" % (end - start))


# 创建进程池
print('Parent process %s.' % os.getpid())
p = Pool(4)
print(range(5))
for i in range(5):
    p.apply_async(run_pool, args=(i,))
print("please waitting for all task")
p.close()
p.join()
print("all task end ...")

print("=========")
# 代码解读：
#
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
# 因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
#
# p = Pool(5)
# 就可以同时跑5个进程。
#
# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

print("----------------------------------------------子进程--------------------------------------------------")
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
#
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#
# 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print("======================================================================================================")

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

print("---------------------------------------------进程间的通讯--------------------------------------------------")

# python中的进程间通讯 通过Queue Pipes进行数据交换
print("-----------------------------------------**进程间的通讯 -- Queue**----------------------------------------------")


def write(q):
    print("process(%s) to  write" % os.getpid())
    for i in ['hrx', 'xte', 'ljp', 'lf']:
        print("put %s to queue" % i)
        q.put(i)


def read(q):
    print("process(%s) to  read" % os.getpid())
    while True:
        var = q.get(True)
        print("get %s form queue" % var)


q = Queue()  # 其实就是存取而已
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))
pw.start()
pr.start()
pw.join()
# read中是死循环 所以需要强行停止
pr.terminate()

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，
# multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

# todo  在unix/linux下 子进程是os模块直接fork出来
# todo  multiprocessing封装了fork的过程 我们不需要太在意 windows下不能fork但是multiprocessing模块会模拟fork 所以也不需要care
# todo 进程间的通讯是序列化之后的传输


# 小结
# 在Unix/Linux下，可以使用fork()调用实现多进程。
#
# 要实现跨平台的多进程，可以使用multiprocessing模块。
#
# 进程间通信是通过Queue、Pipes等实现的。

#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 下午9:21
# @Author  : Aries
# @Site    : 
# @File    : Coroutine_moudel.py
# @Software: PyCharm

# todo 子程序 就是函数,栈式调用
# todo 首先协程是在一个线程中执行 这样就节约了线程切换的开销  多线程越多协程的优势就越明显
# 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
def consumer():
	n = ''
	while True:
		i = yield n
		if not i:
			return
		print('consumer...')
		n = '200 OK'


def produce(c):
	c.send(None)
	for i in range(5):
		i = i + 1
		print('producer pro  ', i)
		r = c.send(i)
		print("return ", r)
	c.close()

# 返回的是一个迭代器
c = consumer()
produce(c)

# 注意到consumer函数是一个generator，把一个consumer传入produce后：
#
# 首先调用c.send(None)启动生成器；
#
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
#
# produce拿到consumer处理的结果，继续生产下一条消息；
#
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
#
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
#
# 最后套用Donald Knuth的一句话总结协程的特点：
#
# “子程序就是协程的一种特例。”




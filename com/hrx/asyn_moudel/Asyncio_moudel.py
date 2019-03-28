#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 下午10:26
# @Author  : Aries
# @Site    :
# @File    : Asyncio_moudel.py
# @Software: PyCharm


# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
#
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
#
# 用asyncio实现Hello world代码如下：

# todo  使用asyncio实现hello  world
# todo 需要注意一下 这个库是为协程服务的  单线程的异步框架   由于python中多线程意义不大  所以建议多进程+协程
import asyncio
import threading


@asyncio.coroutine
def hello():
	print("Hello world!", threading.currentThread())
	# 异步调用sleep 1s
	r = yield from asyncio.sleep(1)
	print("hello  end", threading.currentThread())


# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。

# hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
# 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
# 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
#
# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

# 我们用Task封装两个coroutine试试：
#
# 获取eventloop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print('---------------------------------通过asyncio异步网络来连接sina,sohu和163的网页---------------------------------------')


@asyncio.coroutine
def wget(host):
	print('wget %s...' % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	writer.close()


loop1 = asyncio.get_event_loop()
tasks1 = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop1.run_until_complete(asyncio.wait(tasks1))
loop1.close()


# 可见3个连接由一个线程通过coroutine并发完成。
#
# 小结
# asyncio提供了完善的异步IO支持；
#
# 异步操作需要在coroutine中通过yield from完成；
#
# 多个coroutine可以封装成一组Task然后并发执行。

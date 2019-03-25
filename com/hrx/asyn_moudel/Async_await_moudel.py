#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 下午11:12
# @Author  : Aries
# @Site    : 
# @File    : Async_await_moudel.py
# @Software: PyCharm

# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
#
# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
#
# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#
# todo 把@asyncio.coroutine替换为async；
# todo 把yield from替换为await。


# 让我们对比一下上一节的代码：
import asyncio


@asyncio.coroutine
def hello():
	print("Hello world!")
	r = yield from asyncio.sleep(1)
	print("Hello again!")


# 用新语法重新编写如下：
# todo  其实下面的代码 更加容易被我们理解  毕竟我是一个 javer

async def hello():
	print("Hello world!")
	r = await asyncio.sleep(1)
	print("Hello again!")
# 剩下的代码保持不变。
#
# 小结
# Python从3.5版本开始为asyncio提供了async和await的新语法；
#
# 注意新语法只能用在Python 3.5以及后续版本，如果使用3.4版本，则仍需使用上一节的方案。
#
# 练习
# 将上一节的异步获取sina、sohu和163的网站首页源码用新语法重写并运行。

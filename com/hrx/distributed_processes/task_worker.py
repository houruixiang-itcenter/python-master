#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 下午10:02
# @Author  : Aries
# @Site    :
# @File    : task_master.py.py
# @Software: PyCharm
# todo 分布式 子进程

# todo 发送任务的队列
import queue
import random
import time
from multiprocessing.managers import BaseManager


# todo 前提 创建QueueManager
class QueueManager(BaseManager):
    pass


# todo 第一步 注册QueueManager 这时候只需要注册名字即可 因为主进程已经创建好 所以这里只是为从网络上获取queue进行网络会话
QueueManager.register('get_task_send_queue')
QueueManager.register('get_result_response_queue')

# todo 第二步连接服务器  就是task_master
server_addr = '127.0.0.1'
print('worker: Connect to server %s ...' % server_addr)
manager = QueueManager(address=(server_addr, 5000), authkey=b'123')
manager.connect()

# todo 第三步  连接完成之后 获取queue 进行相应的消息发送
task = manager.get_task_send_queue()
result = manager.get_result_response_queue()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('worker: run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Queue.Empty:
        print('worker: task queue is empty.')
# 处理结束:
print('worker: worker exit.')

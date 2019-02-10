#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 下午10:02
# @Author  : Aries
# @Site    :
# @File    : task_master.py.py
# @Software: PyCharm


# todo 发送任务的队列
import queue
import random
from multiprocessing.managers import BaseManager

task_send_queue = queue.Queue()

# todo 接收任务的队列

result_response_queue = queue.Queue()


# todo 前提 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# todo 分布式进程之间的通信只要是依赖baseManager的封装
# todo 第一步 注册---QueueManager关联queue
QueueManager.register('get_task_send_queue', callable=lambda: task_send_queue)
QueueManager.register('get_result_response_queue', callable=lambda: result_response_queue)

# todo 第二步 绑定端口5000 设置验证码  这里设置验证码是为了特定分布式进程之间通信不被其他进程干预
manager = QueueManager(address=('', 5000), authkey=b'123')
# todo 第三步 启动queue
manager.start()
# todo 第四步 通过网络访问Queue对象
task = manager.get_task_send_queue()
result = manager.get_result_response_queue()
# todo 第五步 执行任务
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('master: Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('master: Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('master:  Result: %s' % r)

# todo 第六步 关闭
manager.shutdown()
print('master: master exit.')


# 这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十
# 台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
#
# Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：
#
#                                              │
# ┌─────────────────────────────────────────┐     ┌──────────────────────────────────────┐
# │task_master.py                           │  │  │task_worker.py                        │
# │                                         │     │                                      │
# │  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
# │  result = manager.get_result_queue()    │     │  result = manager.get_result_queue() │
# │              │                          │  │  │              │                       │
# │              │                          │     │              │                       │
# │              ▼                          │  │  │              │                       │
# │  ┌─────────────────────────────────┐    │     │              │                       │
# │  │QueueManager                     │    │  │  │              │                       │
# │  │ ┌────────────┐ ┌──────────────┐ │    │     │              │                       │
# │  │ │ task_queue │ │ result_queue │ │<───┼──┼──┼──────────────┘                       │
# │  │ └────────────┘ └──────────────┘ │    │     │                                      │
# │  └─────────────────────────────────┘    │  │  │                                      │
# └─────────────────────────────────────────┘     └──────────────────────────────────────┘
#                                              │
#
#                                           Network
# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个
# 名字，比如get_task_queue。
#
# authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey不一致，
# 肯定连接不上。
#
# 小结
# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
#
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，
# 而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。



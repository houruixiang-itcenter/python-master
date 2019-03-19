#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 下午10:57
# @Author  : Aries
# @Site    : 
# @File    : TcpClient.py
# @Software: PyCharm
import socket

s = socket.socket()
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'ljp ',b'xte ',b'hrx ']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()


# 小结
# 用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，
# 对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。
#
# 同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 下午11:04
# @Author  : Aries
# @Site    : 
# @File    : UdpService.py
# @Software: PyCharm

# 建立socket
import socket
# SOCK_DGRAM就是UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
# todo  注意UDP 不需要监听即来即答的模式
print('already bind the  9999')
# recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
# todo  这样就省下来多线程  我觉得最好 还是开多线程好一点   这样线程安全
while True:
	data,addr = s.recvfrom(1024)
	print('recever client %s,   %s' % (data,addr))
	s.sendto(b'hello,  %s' % data,addr)


	

#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 下午11:11
# @Author  : Aries
# @Site    : 
# @File    : Tcp_moudle.py
# @Software: PyCharm

# todo Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
# todo ，再指定协议类型即可。   注意ip用来标识计算机,而端口用来标识每一个计算机上的不同ap

# 客户端

# 首先创建一个基于Tcp连接  socket
# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
# 答案是作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，
# 因为80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，
# 等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用
# todo 注意参数是一个tuple,包含地址和端口号
s.connect(('www.sina.com.cn', 80))
# socket.AF_INET:是指ipv4,如果要用更先进的IPv6，就指定为AF_INET6,socket.SOCK_STREAM指TCP


# 到此为止 我们就已经与新浪的服务器建立
# 接着 向新浪服务器发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
# 例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。
#
# 发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了：
# todo 其实建立TCP连接后  客户端和服务端 可以互相通信  但是为了协调,客户端要先向服务端发请求,然后服务端做出回应

# 接收数据
# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，
# 在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。

buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
print(data)

# 最后关闭链接
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
# 通过标识符 进行截断
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'w') as f:
	f.write(html.decode('utf-8'))

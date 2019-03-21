#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 下午9:14
# @Author  : Aries
# @Site    : 
# @File    : pop3_moudel.py
# @Software: PyCharm

# todo 前面有讲SMTP发送邮件,那么如何收取邮件呢
# todo 收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。

# python中内置了一个poplib模块,实现了pop3的协议,可以直接用来收邮件
# pop3协议接收的不是一个已经可以阅读的邮件本身,而是邮件的原始文本  所以pop3接收的文本要想变成可以阅读的邮件,还需要用email模块提供的各种类来
# 来解析原始文本


# todo 收取邮件  1.用poplib把邮件的原始文本下载到本地   2.用email解析源文件,还原为邮件对象
import poplib
from email.parser import Parser

from com.hrx.email_moudel.PopParser import print_info

email = input('email: ')
pwd = input('pwd: ')
pop3_server = input('pops server: ')

# 连接到pop3的服务器
server = poplib.POP3(pop3_server)
# 打开关闭调试信息
server.set_debuglevel(1)
# todo  打印pop3的服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

# todo 身份认证
server.user(email)
server.pass_(pwd)

# todo stat()返回邮件的数量和占用空间
print('messages:  $s, Size: %s' % str(server.stat()))

# todo list()返回所有邮件的编号
resp, list, octets = server.list()
print('resp: %s \r\n list: %s \r\n octets: %s' % (resp, list, octets))

# todo 获取最近一封邮件
index = len(list)
resp, lines, octets = server.retr(index)
# todo 输出当前邮件
print('Cuurent E-mail: \r\n resp: %s \r\n list: %s \r\n octets: %s' % (resp, lines, octets))

# todo lines存储了原始文本的每一行   下面来获取原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
with open('pop.txt','w') as f:
	f.write(msg_content)
msg = Parser().parsestr(msg_content)
print('----------------------------------------以下是正文--------------------------------------------------------')
print_info(msg)
	
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()








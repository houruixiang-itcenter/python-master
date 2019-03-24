#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 下午4:53
# @Author  : Aries
# @Site    : 
# @File    : hello.py
# @Software: PyCharm


# todo  实现web应用程序处理WSGI处理函数

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	print(environ)
	body = '<h1>hello, %s<h1>' % (environ['PATH_INFO'][1:] or 'web')
	print(environ['PATH_INFO'][1:])
	print(environ['PATH_INFO'][1:].encode('utf-8'))
	return [body.encode('utf-8')]



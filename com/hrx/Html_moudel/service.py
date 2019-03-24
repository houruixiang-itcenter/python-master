#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 下午4:53
# @Author  : Aries
# @Site    : 
# @File    : service.py
# @Software: PyCharm


# todo 负责启动 WSGI服务器,加载 application


from com.hrx.Html_moudel.hello import application
from wsgiref.simple_server import make_server

# todo 创建一个服务器,IP地址为空,端口:8000,处理函数application:

server = make_server('', 8000, application)
print('Server HTTP on port 8000...')
# 监听client的Http请求,也就是监听当前端口:
server.serve_forever()

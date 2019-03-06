#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 下午8:54
# @Author  : Aries
# @Site    :
# @File    : urllib_moudle.py
# @Software: PyCharm

# todo urllib 提供一系列用于操作url的功能


# todo  get请求
from urllib import request, parse

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
    print('Data: ', data.decode('utf-8'))

print('---------------------------------------------模拟iphone6请求豆瓣首页------------------------------------------------')

# todo 下面我们来看一个 需要添加请求头的get请求
# todo 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，
# todo 我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, '
                             'like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    data = f.read()
    print('status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
    print('Data: ', data.decode('utf-8'))

print('---------------------------------------------post请求模拟微博登录------------------------------------------------')

# todo post 请求
print('login to weibo.cn...')
email = input('Email: ')
pwd = input('password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', pwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
























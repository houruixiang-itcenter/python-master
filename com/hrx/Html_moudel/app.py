#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 下午5:45
# @Author  : Aries
# @Site    : 
# @File    : app.py.py
# @Software: PyCharm


#  todo  首先来定义接口  如下所示:

# GET /：首页，返回Home；
# GET /signin：登录页，显示登录表单；
# POST /signin：处理登录表单，显示登录结果。

# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，所以，我们写出来的代码就像这样：
# todo  Flask类似于 java的spring boot的注解关联
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
	# 需要从request对象中读取表单内容:
	if request.form['username'] == 'houruixiang' and request.form['password'] == 'HRX552299':
		return '<h3>Hello,%s!</h3>' % request.form['username']
	return '<h3>用户名或者密码错误</h3>'

#
# if __name__ == '__main__':
# 	app.run()
#
#
# 实际的Web App应该拿到用户名和口令后，去数据库查询再比对，来判断用户是否能登录成功。
#
# 除了Flask，常见的Python Web框架还有：
#
# Django：全能型Web框架；
#
# web.py：一个小巧的Web框架；
#
# Bottle：和Flask类似的Web框架；
#
# Tornado：Facebook的开源异步Web框架。
#
# 当然了，因为开发Python的Web框架也不是什么难事，我们后面也会讲到开发Web框架的内容。
#
# 小结
# 有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。
#
# 在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。
# Flask通过request.form['name']来获取表单的内容。
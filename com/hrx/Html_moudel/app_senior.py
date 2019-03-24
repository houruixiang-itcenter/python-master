#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 下午6:25
# @Author  : Aries
# @Site    : 
# @File    : app_senior.py
# @Software: PyCharm
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST6'])
def home():
	return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
	usrname = request.form['username']
	pwd = request.form['password']
	if usrname == 'houruixiang' and pwd == 'HRX552299':
		return render_template('signin-ok.html', usrname=usrname)
	return render_template('form.html', message='Bad username or password', username=usrname)


if __name__ == '__main__':
	app.run()

# Flask通过render_template()
# 函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2，所以我们先直接安装jinja2：
# todo $ pip install jinja2



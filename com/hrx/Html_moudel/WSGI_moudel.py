#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 下午4:42
# @Author  : Aries
# @Site    :
# @File    : WSGI_moudel.py
# @Software: PyCharm

# 了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：
# 浏览器发送一个HTTP请求；
# 服务器收到请求，生成一个HTML文档；
# 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
# 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
# 所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、
# Lighttpd等这些常见的静态服务器就是干这件事情的。
# 如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，
# 还没开始写动态HTML呢，就得花个把月去读HTTP规范。
# 正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，
# 所以，需要一个统一的接口，让我们专心用Python编写Web业务。
# 这个接口就是WSGI：Web Server Gateway Interface。
# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：


# todo 其实中间过程不需要我们考虑 我们需要的是:如何发送request   如何反馈reponse即可 其他不需要关心


# 就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。start_response()函数接收两个参数，
# 一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
#
# 通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。
#
# 然后，函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。
#
# 有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body。
#
# 整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了。
#
# 不过，等等，这个application()函数怎么调用？如果我们自己调用，两个参数environ和start_response我们没法提供，返回的bytes也没法发给浏览器。
#
# 所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。但是现在，
# 我们只想尽快测试一下我们编写的application()函数真的可以把HTML输出到浏览器，所以，要赶紧找一个最简单的WSGI服务器，把我们的Web应用程序跑起来。
#
# 好消息是Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，
# 但是不考虑任何运行效率，仅供开发和测试使用。

# todo 运行WSGI服务
# 详见 hello.py and  service.py

# todo 在server端 http处理函数中的environ中包含http请求的信息 我们可以从中获取 我们想要的来构建response
# 小结
# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
#
# 复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。


print('--------------------------------------------使用web框架----------------------------------------------------')
# todo 首先如果请求很多 然后逻辑积压在application这个func中 显然不合理  而且很难维护
# def application(environ, start_response):
#     method = environ['REQUEST_METHOD']
#     path = environ['PATH_INFO']
#     if method=='GET' and path=='/':
#         return handle_home(environ, start_response)
#     if method=='POST' and path='/signin':
#         return handle_signin(environ, start_response)
#     ...


# 代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比较低级，
# 我们需要在WSGI接口之上能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。
#
# 由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，
# 直接选择一个比较流行的Web框架——Flask来使用。


# todo  首先用flask来写app 要比WSGI要好很多
# todo  那么我们来写一个 app  详见app.py

print('--------------------------------------------使用模板----------------------------------------------------')
# todo  作为一个webApp  不仅仅要care  server端的接口能力 还要写html  而作为程序的入口 html的展示也是极为重要的
# todo  所以单纯 像我们之前的通过return 来拼接html 显然对于复杂的前端页面是不可以的 所以我们需要使用模板来优雅实现


# 这就是传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”。
#
# todo Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
#
# todo 包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
#
# todo MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。

# 详见 app_senior.py


# 通过MVC，我们在Python代码中处理M：Model和C：Controller，而V：View是通过模板处理的，这样，我们就成功地把Python代码和HTML代码最大限度地分离了。
#
# 使用模板的另一大好处是，模板改起来很方便，而且，改完保存后，刷新浏览器就能看到最新的效果，这对于调试HTML、CSS和JavaScript的前端工程师来说实在是太重要了。
#
# 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
#
# 比如循环输出页码：
#
# {% for i in page_list %}
#     <a href="/page/{{ i }}">{{ i }}</a>
# {% endfor %}
# 如果page_list是一个list：[1, 2, 3, 4, 5]，上面的模板将输出5个超链接。
#
# 除了Jinja2，常见的模板还有：
#
# Mako：用<% ... %>和${xxx}的一个模板；
#
# Cheetah：也是用<% ... %>和${xxx}的一个模板；
#
# Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
#
# 小结
# 有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。



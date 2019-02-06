#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/6 下午11:43
# @Author  : Aries
# @Site    : 
# @File    : os-operation.py
# @Software: PyCharm

# 我们可以在终端使用命令行实现环境变量的查看 以及文件的查看 增删等
# todo  在python中os也可以像终端一样操作系统提供的接口函数
import os

# 当前系统
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)

# 当前系统的详细信息
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
print(os.uname())

# 环境变量
print(os.environ)

# 获取某个环境变量
print(os.environ.get('PATH'))
print(os.environ.get('HOME', 'hi'))

# 查看当前文件的绝对路径
print(os.path.abspath('.'))

# 创建文件夹
os.mkdir("/Users/houruixiang/python/python-master/c")

# 删除文件夹
os.rmdir("/Users/houruixiang/python/python-master/c")

# 合并目录
print(os.path.join("/Users/houruixiang/python/python-master/com", "c"))

# 分割目录  文件夹路径 + 文件名
print(os.path.split("/Users/houruixiang/python/python-master/c"))

# 分割后缀
print(os.path.splitext("/Users/houruixiang/python/python-master/c"))

# 文件重命名  注意  第一个参数是删除文件 第二个是创建文件并拷贝原始文件的内容
# os.rename("/Users/houruixiang/python/python-master/cc.txt", "/Users/houruixiang/python/python-master/bb.txt")

# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


# 小结
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。

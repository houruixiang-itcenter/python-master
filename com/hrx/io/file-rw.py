#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/6 下午10:26
# @Author  : Aries
# @Site    : 
# @File    : file-rw.py
# @Software: PyCharm

# 读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
#
# 读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
# 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

# todo 普通程序不允许直接操作磁盘,读文件---请求打开磁盘,通过接口读取数据 写文件---请求打开磁盘,通过接口写入数据\
# params file mode(r  ro w)
# 第一步  打开文件  第二步 读取文件  第三步 关闭文件
from io import StringIO, BytesIO

f = open('/Users/houruixiang/python/python-master/a.txt', 'r')
s = f.read()
# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，
# 并且操作系统同一时间能打开的文件数量也是有限的
f.close()
print(s)

# 进一步 简化  由于  每次操作完关闭文件  步骤有一点繁琐 再者close的时候文件一定会全部写入  如果不close文件有一定几率写入不完全
# 而且可能会忘记 读完之后  忘记close  所以 python做了一些简化
# Python引入了with语句来自动帮我们调用close()方法：
with open('/Users/houruixiang/python/python-master/a.txt', 'r') as f:
    print(f.read())

# 像下面 这样如果是读取不存在  则会抛出IO异常  所以我们需要注意在异常情况下 也应该关闭文件流
try:
    f = open('/Users/houruixiang/python/python-master/b.txt', 'r')
    f.read()
finally:
    f.close()

# 进一步 简化  由于  每次操作完关闭文件  步骤有一点繁琐 再者close的时候文件一定会全部写入  如果不close文件有一定几率写入不完全
# 而且可能会忘记 读完之后  忘记close   所以 python做了一些简化
# todo 还有比较重要的一点 当操作文件异常的情况下 也需要close文件  而 try...finally...又太繁琐所以:
# Python引入了with语句来自动帮我们调用close()方法：
with open('/Users/houruixiang/python/python-master/a.txt', 'r') as f:
    print(f.read())

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
#
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。


# todo 这是前提到的鸭子模型  在多态中有用到


# todo read()读取的是所有内容
# todo 但是python规定 一次读取不能操作 10G  所以可以 无限调用read(size)
# todo 在python中还可以一行 一行的读取
print("------------------------------------------多方式读取文件---------------------------------------------------")

with open('/Users/houruixiang/python/python-master/b.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open('/Users/houruixiang/python/python-master/b.txt', 'r') as f:
    print(f.read(2))

# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
#
# >>> f = open('/Users/michael/test.jpg', 'rb')
# >>> f.read()
# b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
#
# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# >>> f.read()
# '测试'
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
#
# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')


# 写文件 mode - w 如果已经存在就覆盖原来的
with open('/Users/houruixiang/python/python-master/a.txt', 'w') as f:
    f.write("哈哈哈")

# 写文件 mode - a 如果已经存在就在原来的基础上追加  append
with open('/Users/houruixiang/python/python-master/a.txt', 'a') as f:
    f.write("\n嘿嘿嘿")

print("------------------------------------------**StringIO和BytesIO**------------------------------------------------")
# StringIO就是 在内存中读写str  注意!  是str
s = StringIO()
s.write("hello")
print("===", s.getvalue())

# 当然初始化StringIO  时候做为参数可以写入内容
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO就是 在内存中读写byte  注意!  是byte

b = BytesIO()
b.write("中文".encode('utf-8'))
print("===", b.getvalue())


# 小结
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。


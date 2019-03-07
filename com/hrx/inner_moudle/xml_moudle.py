#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 下午9:12
# @Author  : Aries
# @Site    : 
# @File    : xml_moudle.py
# @Software: PyCharm

# 解析xml有两种方式: DOM和SAX
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，
# 缺点是我们需要自己处理事件。
# todo eg: <a href="/">python</a>
# todo 用sax解析时候会产生3个事件
# 1.start_element事件，在读取<a href="/">时；
#
# 2.char_data事件，在读取python时；
#
# 3.end_element事件，在读取</a>时。

# r''' 转义符失效
from encodings.utf_8 import encode
from pyexpat import ParserCreate
from urllib import request

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''


# 首先先自定义一个sax的解析类
class SaxParseObj(object):

    def start_elem(self, name, attrs):
        print('start_elem---name:  %s ,attrs:  %s' % (name, str(attrs)))

    def end_elem(self, name):
        print('end_elem---name:  %s' % name)

    def char_data(self, txt):
        print('char_data:  %s ' % txt)


#  下面来使用内建模块进行解析
saxObj = SaxParseObj()
parser = ParserCreate()
parser.StartElementHandler = saxObj.start_elem
parser.EndElementHandler = saxObj.end_elem
parser.CharacterDataHandler = saxObj.char_data
print(parser.Parse(xml))
print('-------------------------------------------------------------------------------------------------------------')
# 生成xml可以使用比较简单的字符串拼接
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & data'))
L.append(r'</root>')
print(''.join(str(L)))

print('------------------------------------------查询天气--------------------------------------------------')

URL = 'https://www.yahoo.com/news/weather/'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()
print('status: ', f.status, f.reason)
for k, v in f.getheaders():
    print("%s: %s" % (k, v))
print('Data: ', data.decode('utf-8'))
# result = parseXml(data.decode('utf-8'))

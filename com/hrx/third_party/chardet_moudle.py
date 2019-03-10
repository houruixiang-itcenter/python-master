#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午8:46
# @Author  : Aries
# @Site    :
# @File    : chardet_moudle.py
# @Software: PyCharm

# 字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的str和bytes两种数据类型，
# 并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。
#
# 对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。
#
# 当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。

# todo 首先  python提供了encode编码和decode()解码 但是在不知道编码方式的情况下是不好进行转换的
import chardet

print('-------------------------------------------使用chardet----------------------------------------------------')
# todo 使用chardet可以检测编码,这样转化为str 就是知道怎么转了
s = chardet.detect(b'hallo my son')
print(s)

# data = '你好,丽丽'.encode('gbk')
# todo  有误差
data = '今天吃的油焖大虾'.encode('gbk')
s1 = chardet.detect(data)
print(s1)


data1 = '今天吃的油焖大虾'.encode('utf-8')
s2 = chardet.detect(data1)
print(s2)

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))


# 可见，用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。
#
# chardet支持检测的编码列表请参考官方文档Supported encodings。
#
# 小结
# 使用chardet检测编码非常容易，chardet支持检测中文、日文、韩文等多种语言。

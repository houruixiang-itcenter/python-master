#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午8:32
# @Author  : Aries
# @Site    :
# @File    : base64_moudle.py
# @Software: PyCharm

# 摘要算法

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
#
# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。


#  计算MD5
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果作用的串特别长  md5可以分块进行
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# todo SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
#
# todo 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
#
# todo 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。
# todo 这种情况称为碰撞，比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，
# todo 并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。


# todo 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
# todo 摘要算法的应用,在数据库中同时要存储用户名和密码 密码通过md5加密 ,每次输入密码进行md5转换  从而进行login的登录检查


# todo  md5是不可逆加密,所以是没有办法 进行反推的  所以即使运维人员拿到摘要也是没有办法反推的,但是黑客截获之后可以通过彩虹表进行验证,为了防止
# todo 这个现象发生,所以需要加盐  即可逆+不可逆加密结合  或者pwd 后面加一串字符串(salt),比如对密码加密可以密码+用户名,然后整体进行md5加密

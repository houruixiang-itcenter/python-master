#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 下午9:34
# @Author  : Aries
# @Site    : 
# @File    : hmac_moudle.py
# @Software: PyCharm


# 通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值，例如，判断用户口令是否正确，我们用保存在数据库中的password_md5对比计算md5(password)
# 的结果，如果一致，用户输入的口令就是正确的。
#
# 为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，需要增加一个salt来使得相同的输入也能得到不同的哈希，这样，大大增加了黑客破解的难度。
#
# 如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(
#     message + salt)。但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。
#
# 这实际上就是Hmac算法：Keyed - Hashing
# for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
#
# 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA - 1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
#
# Python自带的hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希。
#
# 我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：
#
# >> > import hmac
# >> > message = b'Hello, world!'
# >> > key = b'secret'
# >> > h = hmac.new(key, message, digestmod='MD5')
# >> >  # 如果消息很长，可以多次调用h.update(msg)
# >> > h.hexdigest()
# 'fa4ee7d173f2d97ee79022d1a7355bcf'
# 可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。

# 小结
# Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash


# todo 其实随机的salt是在注册之前是这样的,而且不同的用户的salt不同,所以一个用注册成功之后,每次登录的salt是相同的用来反推数据库
# todo 注册成功之后  用户名密码 是明文传输的
import hashlib
import hmac

message = b'hello world!'
key = b'12345'


class hmac_moudle:

    def __init__(self) -> None:
        super().__init__()

    print("haha" + "lala")

    # md5  字符串之间 也可以相加
    md5 = hashlib.md5()
    md5.update(key + message)
    print(md5.hexdigest())
    h = hmac.new(key, message, digestmod='MD5')
    print(h.hexdigest())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 下午9:17
# @Author  : Aries
# @Site    : 
# @File    : struct_moudle.py
# @Software: PyCharm


# 把一个32位无符号整数编程字节 ,也就是4个长度的bytes
#  直接写 其实我有一点看不懂


# 好了直接跳过  使用python内置的struct模块进行转换
# todo 首先介绍下 n字节无符号整数
# 无符号（1字节） 0到255
# 有符号（1字节）-128到127
# 无符号（2字节） 0到65535
# 有符号（2字节） -32768到32765
# 无符号（4字节） 0到4294967295
# 有符号（4字节）-2147483648到2147483647


# 转换 --- struct 的pack函数把任意数据类型转换为bytes
import struct

print(struct.pack('>I', 10240099))

# 还原
print(struct.unpack('>I', b'\x00\x9c@c'))

# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
#
# 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。

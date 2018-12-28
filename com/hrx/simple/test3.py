#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/22 下午4:17
# @Author  : Aries
# @Site    :
# @File    : test3.py
# @Software: PyCharm

"""
1.字符串和编码
2.使用list和tuple
3.条件判断
4.循环
5.使用dict和set

"""

from __future__ import print_function


class test3:
    def __init__(self):
        pass


'''
1.字符串和编码 :

1.1字符编码和反编码
'''
print('----------------------------字符串和编码 -----------------------------------------')
print('包含中文的str')

# 单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
# chr() arg not in range(256)
# ord() expected a character, but string of length 3 found
print(ord('a'))
# a = ord('中')
# print(a)
# b = chr(25991)
# print(b)


a = '\u4e2d\u6587'
print(a)

# s = 'Python-中文'
# print(s)
# b = s.encode('utf-8')
# print(b)
# print(b.decode('utf-8'))
print(chr(65))

a, b, c = 1, 2, "john"
print(a, b, c)

'''
1.2python的格式化
其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
'''
# 在这里%和d之间可以指定位数 当然在指定位数之前可以指定是否补0
print('%03d-%08d' % (3, 8))
print('%.3f' % 1)
print('hi,%s,this is RMB %d' % ('Marry', 1000))

'''
python另一种格式化方式 format
类似列表一样是有索引的
但是 相较于%是比较麻烦的
'''
a = 'Hello, {0}, 成绩提升了 {1:.1f}%,平均成绩{2:2d},'.format('小明', 17.125, 90)
print(a)

'''
2.使用list和tuple :

2.1 list
'''
print('----------------------------使用list -----------------------------------------')

# 创建list 类比java中的ArrayList
classList = ['ljp', 'gh', 'lf']
l = len(classList)
l0 = classList[0]
l1 = classList[1]
l2 = classList[2]
print(l, l0, l1, l2)

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classList[-1], classList[-2], classList[-3])


#  this is my first function
def getItem(classList):
    for item in classList:
        if classList.index(item) == len(classList) - 1:
            print(item)
        else:
            print(item, end='  ')


# list具备如下 操作
# 增加
classList.append('hrx')
getItem(classList)

# 插入
classList.insert(1, '哈哈')
classList.insert(1, '嘿嘿')
getItem(classList)

# 删除
classList.pop()
classList.pop(0)
getItem(classList)

#  修改
classList[0] = '李际鹏'

#  list中元素类型 不确定
list = [0, '哈哈', 'hallo', [1, 2]]
getItem(list)

print('----------------------------使用tuple -----------------------------------------')
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

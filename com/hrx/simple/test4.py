#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 下午10:47
# @Author  : Aries
# @Site    : 
# @File    : test4.py
# @Software: PyCharm


class test4:
    print('-------------------------------条件判断------------------------------------------')

    age = 20
    if age >= 18:
        print('your age is', age)
        print('adult')

# elif是else
# if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
#
# if < 条件判断1 >:
# 	< 执行1 >
# elif < 条件判断2 >:
# 	< 执行2 >
# elif < 条件判断3 >:
# 	< 执行3 >
# else:
# 	< 执行4 >

# 注意input()返回的是str  所以要做处理
# while True:
# 	record = int(input('请输入你的分数: '))
# 	if record > 90:
# 		print('优秀')
# 	elif 60 < record < 90:
# 		print('还不错')
# 	else:
# 		print('不及格!')


print('-------------------------------循环------------------------------------------')
# 如果要计算1-100的整数之和，从1写到100有点困难，
# 幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。


# todo for -- 相当于  java中的fore
sum = 0
for i in list(range(10)):
    sum = sum + i
print(sum)

print('-------------while------------------')

# todo while
a = 1
while a < 10:
    print('curIndex: %s' % a)
    a = a + 1

# break/continue
# 注意 python中
# python 组合字符串时不要用 a+b ，
# 应该是 print "Game over. Your secret number was:%s" % (p,)
print('-------------break------------------')
b = 0
while b < 10:
    b = b + 1
    if b == 3:
        break
    print('curIndex: %s' % b)
    pass

print('-------------continue------------------')
c = 0
while c < 10:
    c = c + 1
    if c == 3:
        continue
    print('curIndex: %s' % c)
    pass

# 循环是让计算机做重复任务的有效的方法。
#
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
#
# 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
#
# 有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
#
# 请试写一个死循环程序。

print('-------------------------------dict------------------------------------------')
# dict就是python中的字典  同java中的map
d = {'数学': 90, '语文': 88, '英语': 72}
print(d['数学'])

# 为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
#
# 第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
#
# dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
#
# 你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。

# todo  dict 元素的存储
# 元素的替换  重复赋值 会取最后一次赋值
d['数学'] = 88
d['数学'] = 77
d['数学'] = 66
print(d['数学'])
print(d)

# 判断字典中是否有相应的key
isExit = d.get('哈哈')
print(isExit)

isExit = d.get('哈哈', 1)
print(isExit)

isExit = d.get('哈哈', 'stupid')
print(isExit)

isExit = '哈哈' in d
print(isExit)

# None
# 1
# stupid
# False

# 删除元素
d.pop('数学')
# 增加元素
d['历史'] = 98
print(d)

print('-------------------------------set------------------------------------------')
# set相当于 java中的set只能存储key  不能重复
# set初始化 看起来是一个list放入 其实并不是list
# set是存储一堆key  所以不可以放入可变元素
s = set([1, 2, 3, 5, 6, 7, 8, 9, 10])
# s1 = set([[1], 2, 3, 5, 6, 7, 8]) -- error set
i = 0
while i < 10:
    print(s)
    i += 1
# 不可重复性
s1 = set([1, 1, 1, 2, 2, 2])
print(s1)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
a1 = set([1, 2, 3])
a2 = set([2, 3, 4])

print(a1 & a2)
print(a1 | a2)


l1 = set([(1, 2, 3), 3, 4])
l2 = set([(1, [2, 3]), 3, 4])

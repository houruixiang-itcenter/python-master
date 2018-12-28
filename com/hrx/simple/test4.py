#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 下午10:47
# @Author  : Aries
# @Site    : 
# @File    : test4.py
# @Software: PyCharm

from __future__ import print_function


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

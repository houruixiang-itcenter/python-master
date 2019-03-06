#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 下午2:40
# @Author  : Aries
# @Site    : 
# @File    : regular.py
# @Software: PyCharm

#
# 字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。比如判断一个字符串是否是合法的Email地址，
# 虽然可以编程提取@前后的子串，再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用。
#
# 正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，
# 凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。
#
# 所以我们判断一个字符串是否是合法的Email的方法是：
#
# 创建一个匹配Email的正则表达式；
#
# 用该正则表达式去匹配用户的输入来判断是否合法。
#
# 因为正则表达式也是用字符串表示的，所以，我们要首先了解如何用字符来描述字符。
#
# 在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：
#
# '00\d'可以匹配'007'，但无法匹配'00A'；
#
# '\d\d\d'可以匹配'010'；
#
# '\w\w\d'可以匹配'py3'；
#
# .可以匹配任意字符，所以：
#
# 'py.'可以匹配'pyc'、'pyo'、'py!'等等。
# 要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，
# 用{n}表示n个字符，用{n,m}表示n-m个字符：
#
# 来看一个复杂的例子：\d{3}\s+\d{3,8}。
#
# 我们来从左到右解读一下：
#
# \d{3}表示匹配3个数字，例如'010'；
#
# \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
#
# \d{3,8}表示3-8个数字，例如'1234567'。
#
# 综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
#
# 如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。
#
# 但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。

# todo \d --- 数字  \w --- 字母  . --- 匹配任意字符
# todo * --- 表示任意个字符  + --- 表示至少一个字符  ? --- 表示0个或1个字符 {n} --- 表示n个字符  {n,m} --- 表示n到m个字符
# todo 特殊字符 --- 要用/来转义

# 进阶
# 要做更精确地匹配，可以用[]表示范围，比如：
#
# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
#
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
#
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
#
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
#
# todo A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
#
# todo ^表示行的开头，^\d表示必须以数字开头。
#
# todo $表示行的结束，\d$表示必须以数字结束。
#
# 你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
import re

print("---------------------------------------------------re模块----------------------------------------------------")
# 有了准备知识，我们就可以在Python中使用正则表达式了。Python提供re模块，包含所有正则表达式的功能。
# 由于Python的字符串本身也用\转义，所以要特别注意：
s = 'ABC\\001'
print(s)

# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
s = r'ABC\001'
print(s)

# todo 使用re模块  进行正则表达式的匹配
# 匹配成功 返回一个 Match对象
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# 匹配失败 返回None
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

s = '010-12345'
if re.match(r'^\d{3}\-\d{3,8}$', s):
    print('ok')
else:
    print('fail')

# todo 注意一下  if 后面可以跟True/False  同时也可以跟数字和字符串或者对象
# todo  数字 不为0--True 0 ---False     字符串或者对象 不为空---True 为空---False
print("---------------------------------------------------切分字符串----------------------------------------------------")
s = "a b    c"
print(re.split(r'\s+', s))  # 这个正则表示 切分的标准是一个或者多个空格
print("---------------------------------------------------分组----------------------------------------------------")
# todo 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
# todo 利用re模块 的match方法 返回Match对象  然后利用group来提取分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 来一个 相对复杂的分组
t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m.groups())
print("---------------------------------------------------贪婪匹配----------------------------------------------------")
# 正则表达式的匹配 默认是贪婪匹配  也就是说 会尽量匹配最多的可能
m1 = re.match(r'^(\d+)(0*)$', '123000')
print(m1.groups())
# 加? 之后 变为非贪婪匹配 就是说要兼顾后面的匹配
m2 = re.match(r'^(\d+?)(0*)$', '123000')
print(m2.groups())

print("---------------------------------------------------编译----------------------------------------------------")
# todo re模块在进行匹配时候 会干两件事情 1.检查正则表达式本身是否合法 2.用编译后的正则表达式 去匹配字符串
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-80086').groups())

# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
# todo java 是解释型语言---首次运行编译成字节码文件 (机器识别的机器码)   然后下次运行时候无需编译
# todo  python 是解释型语言  运行时直接翻译成目标机器码   下次 运行需要重新编译
#  Python 解释器，你写的每一行 Python 代码都是由它负责执行，解释器由一个编译器和一个虚拟机构成，编译器负责将源代码转换成字节码文件，
# 而虚拟机负责执行字节码，所以，解释型语言其实也有编译过程，只不过这个编译过程并不是直接生成目标代码，而是中间代码（字节码），
# 然后再通过虚拟机来逐行解释执行字节码。


# 小结
# 正则表达式非常强大，要在短短的一节里讲完是不可能的。要讲清楚正则的所有内容，可以写一本厚厚的书了。如果你经常遇到正则表达式的问题，你可能需要一本正则表达式的参考书。
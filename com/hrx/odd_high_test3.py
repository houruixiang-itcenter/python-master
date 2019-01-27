# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 下午4:51
# @Author  : Aries
# @Site    :
# @File    : odd_test.py
# @Software: PyCharm

# todo python中面向对象的高级编程
from enum import Enum, unique

from com.hrx.odd_high_test import Ood_Height
from com.hrx.ood.Dog import Dog
from com.hrx.ood.MyList import MyList
from com.hrx.ood.ORM import Usr
from com.hrx.ood.Test import Ood_test1, Ood_test, Chain, TT, Doctor, Gender


class Animal(object):
	TIGER = 0
	LION = 1
	BRID = 2


class Animal(object):
	TIGER = 0
	LION = 1
	BRID = 2


class Ood_Height:
	def __init__(self):
		pass
	
	print("-------------------------------------------------Enum------------------------------------------------------")
	# 同java 一样  python中也有一些常量  比如 Animal的动物类别   有时会这样定义  一般value是  int/str
	# 初步估计 python中 不加修饰的成员属性 是随着类被加载 就存在的
	
	print(Animal.TIGER)
	print(Animal.LION)
	print(Animal.BRID)
	
	# todo  常量固然可以 但是相比于Enum  Enum是创建一个枚举类  而每个常量是当前class的唯一实例  这样就是说 key不同 value也固然不同
	# todo  所以 枚举的优势 就是 唯一性
	#  创建枚举的方式一
	Mouth = Enum('Mouth', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
	for name, item in Mouth.__members__.items():
		print(name, '=>', item, ',', item.value)
	
	# 可以 看出 Enum的value确实是 唯一实例  value是从1开始自增的
	#  创建枚举的方式二
	
	# @unique装饰器可以帮助我们检查保证没有重复值。
	@unique
	class Weekday(Enum):
		Sun = 0  # Sun的value被设定为0
		Mon = 1
		Tue = 2
		Wed = 3
		Thu = 4
		Fri = 5
		Sat = 6
	
	for name, item in Weekday.__members__.items():
		print(name, '=>', item, ',', item.value)
	# 可以把Enum看成 key-value
	print(Weekday.Sun.name)
	print(Weekday.Sat.value)
	
	print("------------------------------------------Enum-test------------------------------------------------------")
	# 测试:
	bart = Doctor('Bart', Gender.Male)
	if bart.gender == Gender.Male:
		print('测试通过!')
	else:
		print('测试失败!')
	
	# 小结
	# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
	print("------------------------------------------使用元类------------------------------------------------------")
	
	print("------------------------------------------type------------------------------------------------------")
	
	# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
	# todo 动态语言 编译时定义函数和类及一些引用  运行时 分配内存    像py这种动态语言 则是全部再运行时定义
	# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
	# todo 之前有提到 type作为一个 函数可以判断成员的类型
	# todo  python是在运行时生成的  那么是怎么生成的呢? !!!!是通过type生成的
	
	# 要创建一个class对象，type()
	# 函数依次传入3个参数：
	#
	# class的名称；
	# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
	# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
	# 通过type()
	# 函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()
	# 函数创建出class。
	#
	# 正常情况下，我们都用class
	# Xxx...来定义类，但是，type()
	# 函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，
	# 必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
	# def fn(self,name = ""):
	def fn(self, name):
		print(name)
	
	Hello = type('Hello', (object,), dict(hello=fn))
	h = Hello()
	h.hello("lililili")
	# 通过类名调用方法 self作为参数 也必须传入
	Hello.hello(Hello(), "hahhah")
	
	print("------------------------------------------metaclass------------------------------------------------------")
	# metaclass
	# 除了使用type()
	# 动态创建类以外，要控制类的创建行为，还可以使用metaclass。
	#
	# metaclass，直译为元类，简单的解释就是：
	#
	# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
	#
	# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
	#
	# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
	#
	# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
	#
	# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况
	# ，所以，以下内容看不懂也没关系，因为基本上你不会用到。
	#
	# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
	
	# todo 首先初次接触 metaclass  可能会觉得 比较于type太繁琐了  但是自然有其道理
	l = MyList()
	l.add(1)
	print(l)
	
	# todo  metaclass更多的作用于ORM
	# todo ORM全称“Object Relational Mapping”，即对象-关系映射  就是把数据库中的一行映射为一个对象 一个表映射为一个类
	# todo 这样操作数据库 就不需要写SQL语句  直接操作数据映射而来的对象即可
	#  sql  增删改查
	
	u = Usr(id=0, name="Bob", age=18, sex="man")
	u.save()

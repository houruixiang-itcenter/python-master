#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 下午4:51
# @Author  : Aries
# @Site    :
# @File    : odd_test.py
# @Software: PyCharm

# todo python中面向对象的高级编程
from com.hrx.ood import Student
from com.hrx.ood.Doctor import Docter
from com.hrx.ood.Dog import Dog
from com.hrx.ood.Person import Person
from com.hrx.ood.Screen import Screen


class Ood_Height:
    def __init__(self):
        pass

    # 在前面 我们有提到实例属性和类属性
    # python是动态语言 他优于java等静态语言的一点是: 可以随意绑定 属性和方法 也就是无中生有

    # 说到绑定属性  实例对象的绑定属性 只对当前 实例生效   其他实例属于一个平行于当前实例的新对象 所以不生效
    # 但是 类的绑定属性 对于任何实例都生效

    p = Person()
    p.name = 'lihua'
    print(p.name)
    p1 = Person()
    try:
        print(p.name)
    except AttributeError as e:
        print('AttributeError')

    # Person.name = 'mm'
    # print(Person().name)
    # print(Person().name)
    # print(Person().name)

    # todo 在python中可以限制 类的属性绑定 如 : 我们在person中使用__slots__来限制绑定属性

    # try:
    #     Person.name = 'mm'
    #     print(Person().name)
    #     Person.sex = 'man'
    #     print(Person().sex)
    # except AttributeError as e:
    #     print('AttributeError')

    pp = Person()
    pp.age = '15'
    print(pp.age)

    pp1 = Person()
    pp1.age = '16'
    print(pp1.age)

    # 注意 通过类变量赋值完之后 会变为read-only  之后实例化对象后  不可以再操作当前属性
    pp2 = Person()
    pp2.name = 'hou'
    print(pp2.name)

    try:
        pp = Person()
        pp.name = 'mm'
        print(pp.name)
        # pp.sex = 'man'
        # print(pp.sex)
    except AttributeError as e:
        print('AttributeError')

    Dog.name = '1111'
    d = Dog()
    d.name = '222'

    # 注意 被__slots__修饰后的属性 通过类变量赋值完之后 会变为read-only  之后实例化对象后  不可以再操作当前属性  所以下面 代码 会报错
    # Person.name = 'hi'
    # ppp = Person()
    # ppp.name = 'halo'

    # todo __slots__
    # todo 1.__slots__关键字仅仅对类的实例调用有约束作用,类直接调用绑定属性时候 这个关键字失效
    # todo 2.被__slots__修饰的类属性,如果先被类直接调用 则会变为read-only的属性 后续的类实例调用会失败
    # todo 3.__slots__仅作用于当前类 其子类不起作用

    dc = Docter()
    dc.name = 'lily'
    dc.sex = '男'

    print('----------------------------使用@property -----------------------------------------')
    # 在实际中,有时候我们要通过set/get来操作属性 这样出于解耦封装的考虑 其作用之一就是可以检查属性
    # 但是调用起来显然没有xx.属性开起来没关方便 那么有没有调用方便 又具备set/get有点的方法呢
    # 那么 我们接着看@property  这是一个装饰器  类似之前打log时用到的装饰器decorator

    dc.score = 99
    # dc.score = 'hahah'  # 由于内部的检查这行会报错

    # 小结
    # @property广泛应用在类的定义中
    # ，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

    print('----------------------------使用@property-test -----------------------------------------')
    # 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
    # 测试:
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')

    print('----------------------------多重继承 -----------------------------------------')
    # todo java中单一继承 对于一些扩展功能 使用impletements 进行实现接口
    # todo python中不存在接口实现  取而代之的是多继承的原则
    #            ┌───────────────┐
    #            │    Animal     │
    #            └───────────────┘
    #                    │
    #       ┌────────────┴────────────┐
    #       │                         │
    #       ▼                         ▼
    # ┌─────────────┐           ┌─────────────┐
    # │   Mammal    │           │    Bird     │
    # └─────────────┘           └─────────────┘
    #       │                         │
    # ┌─────┴──────┐            ┌─────┴──────┐
    # │            │            │            │
    # ▼            ▼            ▼            ▼
    # ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
    # │  Lion   │  │   Bat   │  │ Parrot  │  │ Ostrich │
    # └─────────┘  └─────────┘  └─────────┘  └─────────┘

    # 哺乳类：能跑的哺乳类，能飞的哺乳类；
    # 鸟类：能跑的鸟类，能飞的鸟类。

    # MixIn
    # 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
    # 通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
    #
    # 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，
    # 你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：

    # Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
    #
    # 比如，编写一个多进程模式的TCP服务，定义如下：
    #
    # class MyTCPServer(TCPServer, ForkingMixIn):
    #     pass
    #
    # 编写一个多线程模式的UDP服务，定义如下：
    #
    # class MyUDPServer(UDPServer, ThreadingMixIn):
    #     pass
    #
    # 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
    #
    # class MyTCPServer(TCPServer, CoroutineMixIn):
    #     pass
    #
    # 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
    #
    # 小结
    # 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
    #
    # 只允许单一继承的语言（如Java）不能使用MixIn的设计。



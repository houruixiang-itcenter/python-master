#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 下午4:51
# @Author  : Aries
# @Site    :
# @File    : odd_test.py
# @Software: PyCharm
import types

from com.hrx.ood.Animal import Animal
from com.hrx.ood.Cat import Cat
from com.hrx.ood.Dog import Dog
from com.hrx.ood.Pig import Pig
from com.hrx.ood.Student import Student
from com.hrx.ood.Tiger import Tiger
from com.hrx.simple.function import command


class Ood:
    def __init__(self):
        pass

    s = Student('小明', '18')
    print(s.get_age())
    print(s.get_name())

    s1 = Student()
    print(s1.get_age())
    print(s1.get_name())

    # 当子类和父类都存在相同的run()
    # 方法时，我们说，子类的run()
    # 覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()

    #  run_twice这个function中,参数只要 是Animal的子类,或者其他含有run方法的实例即可
    # 你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，
    # 任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
    command.run_twice(cat)
    command.run_twice(dog)
    # 当添加tiger这个类的时候 由于其继承自Animal 所以所关系的只是正确重写 run方法 其他不需要关心
    # 从架构角度来说其实就是解耦 符合著名的"开闭]原则"

    # 对扩展开放：允许新增Animal子类；
    #
    # 对修改封闭：不需要修改依赖Animal类型的run_twice()
    # 等函数。
    command.run_twice(Tiger())

    # 静态语言vs动态语言
    # 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()
    # 方法。
    #
    # 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()
    # 方法就可以了：
    # todo 也就是说 在java等静态语言中 由于有强类型的约束 所以只能传入Animal的子类型
    # todo 而对于python这样的动态语言 可以传入Animal的子类型 当然也可以传入类Animal的类 即该类中正确实现run方法即可

    # 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
    #
    # Python的“file - like
    # object“就是一种鸭子类型。对真正的文件对象，它有一个read()
    # 方法，返回其内容。但是，许多对象，只要有read()
    # 方法，都被视为“file - like
    # object“。许多函数接收的参数就是“file - like
    # object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()
    # 方法的对象。
    #
    # 小结
    # 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
    #
    # 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

    print('----------------------------获取对象信息--type -----------------------------------------')
    #  type 判断函数/对象的类型
    print(type(Dog))
    print(type(Dog()))
    print(type(Animal()))
    print(type(123))
    print(type('123'))
    print(type(command.count_1()))

    def fn(self):
        pass

    # types判断  方法的类型
    var = type(abs) == types.BuiltinFunctionType
    var1 = type((x for x in range(10))) == types.GeneratorType
    var2 = type(lambda x: x) == types.LambdaType
    var3 = type(fn) == types.FunctionType
    print(var, '   ', var1, '   ', var2, '   ', var3)

    print('----------------------------获取对象信息--isinstance -----------------------------------------')
    # 总是优先使用isinstance()
    # 判断类型，可以将指定类型及其子类“一网打尽”。
    # 当然 type可以判断 也可以使用isinstance
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    # 也可以判断 当前实例是不是 一个类型集合中的一个
    print(isinstance([1, 2, 3], (list, tuple)))

    # 做为 一个 javaer 一下这个函数是以前 没有接触到的
    # todo python中的dir()获取一个对象 所有的属性和方法
    # todo hasattr()-- 判断一个对象是否有这个属性或者方法  setattr--设置属性或者方法  getattr或者这个对象的属性或者方法

    print(dir(dog))
    # 设置属性
    print('has attr: ', hasattr(dog, 'color'), 'set attr: ', setattr(dog, 'color', 'yellow'), 'get attr: ',
          getattr(dog, 'color', 'red'))
    # todo  getattr(dog, 'color', 'red')  第一个参数:操作的对象 第二个参数:get属性的属性名
    # todo 第三个参数:当前属性名如果get不到,默认为'red' 如果不设置 defult  会抛出异常 AttributeError的错误：

    # 当然对于已知的属性 直接 obj.x 没必要 set/get  当然出于解耦和封装的实际考虑 使用时候 需要三思

    # 小结
    # 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
    #
    # sum = obj.x + obj.y
    # 就不要写：
    #
    # sum = getattr(obj, 'x') + getattr(obj, 'y')
    # 一个正确的用法的例子如下：
    #
    # def readImage(fp):
    #     if hasattr(fp, 'read'):
    #         return readData(fp)
    #     return None
    #
    # 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()
    # 就派上了用场。
    #
    # 请注意，在Python这类动态语言中，根据鸭子类型，有read()
    # 方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()
    # 方法返回的是有效的图像数据，就不影响读取图像的功能。
    print('----------------------------实例属性和类属性 -----------------------------------------')
    # todo python是动态语言  在python中 有类和实例之分  其实就是对应 的java中静态和非静态属性
    # todo 还有一个 区别  在实例化之后获取到对象  可以任意set类中并没有声明的属性  也可以 随时del掉

    #  eg  :Dog
    d = Dog()
    # 注意 这个 voice是原有类中没有属性
    d.voice = '汪汪'
    print(d.voice)
    try:
        print(Dog.voice)
    except AttributeError as e:
        print('当前类---没有这个属性')

    del d.voice
    try:
        print(d.voice)
    except AttributeError as e:
        print('当前对象---没有这个属性')

    # 当类属性 被实例重新赋值之后 会被覆盖
    d.name = 'aden'
    print(d.name)
    print(dog.name)
    del d.name
    print(d.name)
    print('----------------------------实例属性和类属性 -- test -----------------------------------------')
    # 为了统计Dog数，可以给dOG类增加一个类属性，每创建一个实例，该属性自动增加：
    i = 0
    while i < 10:
        Pig()
        i = i + 1

    print(Pig.count)

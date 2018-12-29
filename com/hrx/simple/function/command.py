# -*-coding:utf-8-*-
import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def my_abs_check(x):
    # 类型检查
    if not isinstance(x, (int, float)):
        raise TypeError('哈哈哈')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值
# math 机型  angle是默认参数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# todo 函数定义默认参数、可变参数和关键字参数

# 位置参数  -- 就是普通的参数
# 计算 x² 函数1
def power_1(x):
    return x * x


# 计算 x三次方 函数2
def power_2(x, n):
    i = 1
    while n > 0:
        n = n - 1
        i = i * x
    return i


# todo 默认参数  -- 降低函数调用的难度   对于没有特殊要求的使用默认的参数 有需求自己传入相关参数
# 如兼容函数1 函数2  即同时支持  1个参数和两个参数的调用

def power_common(x, n=2):
    i = 1
    while n > 0:
        n = n - 1
        i = i * x
    return i


def print_person_info(name, age, city='北京'):
    print('姓名: %s' % name)
    print('年龄: %s' % age)
    print('所在城市: %s' % city)


def print_error(tag=[]):
    tag.append('end')
    print(tag)


def print_curr(tag=None):
    print(tag)


# todo 可变参数  -- 降低函数调用的难度   对于没有特殊要求的使用默认的参数 有需求自己传入相关参数
def calc(numbers):
    sum = 0
    for item in numbers:
        sum = sum + item * item
    return sum


def calc_command(*numbers):
    sum = 0
    for item in numbers:
        sum = sum + item * item
    return sum


# 这里的other就是 关键字参数   其实也可以传入 tuple或者list
def print_person_info2(name, age, **kwargs):
    print('name: ', name, 'age: ', age, 'other: ', kwargs)


# 命名关键字参数--关键字参数 key被限制为 city job
def person(name, age, *, city, job):
    print('name: ', name, 'age: ', age, 'other: ', city, job)


def person_defult(name, age, *args, city='shanghai', job='cooker'):
    print('name: ', name, 'age: ', age, 'other: ', city, job)

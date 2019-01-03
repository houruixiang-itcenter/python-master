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


# todo 定义函数的test
# todo 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0 的两个解。
def quadratic(a, b, c):
    if a == 0:
        raise TypeError('二元一次方程参数不能为0')
    # 类型检查
    if not isinstance(a, (int, float)) \
            or not isinstance(b, (int, float)) \
            or not isinstance(c, (int, float)):
        raise TypeError('参数必须为整数')
    defult = math.pow(b, 2) - 4 * a * c
    if defult < 0:
        raise TypeError('这个方程无解')
    return (-b + math.sqrt(defult)) / (2 * a), (-b - math.sqrt(defult)) / (2 * a)


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


# todo 可变参数  -- 降低函数调用的难度   对于没有特殊要求的使用默认的参数 有需求自己传入相关参数

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)


def fact_init(n):
    return fact_later(n, 1)


def fact_later(n, param):
    if n == 1:
        return param
    return fact_later(n - 1, n * param)


# 递归实现汉诺塔
# 利用递归函数移动汉诺塔:
def hnt_move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        hnt_move(n - 1, a, c, b)
        hnt_move(1, a, b, c)
        hnt_move(n - 1, b, a, c)


# 利用切片实现 字符串的空格截取
def trim(var):
    if var == '':
        return ''
    low = 0
    high = len(var) - 1
    temp = ' '
    while low < len(var) and high > 0:
        if low > high:
            return ''
        if var[low] == ' ':
            low = low + 1
        if var[high] == ' ':
            high = high - 1
        if var[low] != ' ' and var[high] != ' ':
            temp = var[low:high + 1]
            break
    return temp


# todo 请使用迭代查找
# if command.findMinAnd一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(list):
    if list == []:
        return (None, None)
    min = list[0]
    max = list[0]
    for item in list:
        if item <= min:
            min = item
        elif item > max:
            max = item
    return (min, max)


# 斐波那契数列
def fib(years):
    n, pre, cur = 0, 0, 1
    while n < years:
        print(cur)
        pre, cur = cur, pre + cur
        n = n + 1
    return 'end'


def generator_fib(years):
    n, pre, cur = 0, 0, 1
    while n < years:
        yield cur
        pre, cur = cur, pre + cur
        n = n + 1
    return 'end'


# 杨辉三角形
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \

# 1  2   4   8   16

def triangles(clum):
    n, l = 0, [1]
    while n < clum:
        yield l
        # append 会修改本身   返回值为None  和java中不同
        l.append(int(math.pow(2, n + 1)))
        n = n + 1
    return 'end'

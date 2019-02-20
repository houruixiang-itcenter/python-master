#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 下午7:43
# @Author  : Aries
# @Site    : 
# @File    : datetime_moudle.py
# @Software: PyCharm
# todo Python之所以自称“batteries included”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用。
from datetime import datetime, timedelta, timezone

from com.hrx.inner_moudle.collections_moudle import haha

print("-------------------------------------------获取当前的日期和时间----------------------------------------------------")
# todo datetime是Python处理日期和时间的标准库。注意需要引入的是datetime模块的datetime类  如果仅仅import datetime
# todo 则需要使用datetime.datetime

now = datetime.now()
print(now)
# 验证之前说的 datetime.datetime的猜想
print(type(now))

print("-------------------------------------------获取指定日期和时间----------------------------------------------------")
# todo 其实就是对目标日期的一个格式化 类似于java中的date.formate  这里直接使用datetime的构造即可
date = datetime(2017, 6, 6, 6, 6)  # params:年月日 时分秒....
print(date)
print("-------------------------------------------datetime转换为timestamp----------------------------------------------")
# todo 为了时间的统一性 在不同的语言中 均使用timestamp来进行同步的记录 注意timestamp可以理解为是一个数字 和时区无关
# todo datetime  和时区有关系的----是我们所看到的时间
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# todo 可以这样理解时间是从1970年开始的  UTC代表时区  所以把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time,即为新纪元时间
# todo 由于时区不同 那么 epoch time 对应的北京时间 就是1970年1月1日 08:00:00 UTC+8:00

# 下面进行转化
dt = datetime(2017, 7, 9, 8, 0)
time = dt.timestamp()
print(time)
# todo 需要注意的是python中timestamp是一个浮点数 而java和js是int型 py中这个浮点型小数位代表毫秒数 所以java/js中的timesamp/1000就是
# todo python这个浮点数
print("-------------------------------------------timestamp转换为datetime----------------------------------------------")
ts = datetime.fromtimestamp(time)  # 自动转化为本地的datetime
ts_utc = datetime.utcfromtimestamp(time)  # 转化为utc 格林威次标准时间
print(ts)
print(ts_utc)

print("-------------------------------------------str转换为datetime----------------------------------------------")
# 有时候我们需要转换  把str转化为datetime --- strptime
# params: 需要转化的字符串 转化后的格式
d1 = datetime.strptime('2017-6-1 18:8:8', '%Y-%m-%d %H:%M:%S')
print(d1)
# todo str转化为datetime 一定要注意格式  Ymd HMS 当然转化后的是没有时区信息的
print("-------------------------------------------datetime转换为str----------------------------------------------")
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，
# 同样需要一个日期和时间的格式化字符串：
print(now.strftime('%a, %b %d %H:%M'))
# 注意在格式转化过程中 不能随便乱定义字母 要参照python文档
print("-------------------------------------------datetime加减----------------------------------------------")
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
print(now - timedelta(hours=1))
print(now - timedelta(days=1))
print(now - timedelta(days=1, hours=12))

print("-------------------------------------------本地时间转换为UTC时间----------------------------------------------")
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
#
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
tz_utc_8 = timezone(timedelta(hours=8))
utc_time = now.replace(tzinfo=tz_utc_8)
print(utc_time)

print("-------------------------------------------时区转化----------------------------------------------")
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
# utc_dt = datetime.utcnow().replace(timezone.utc)
# print(utc_dt)
# # astimezone()将转换时区为北京时间:
# utc_dt_bj = datetime.astimezone(timezone(timedelta(hours=8)))
# print(utc_dt_bj)
# # astimezone()将转换时区为东京时间:
# utc_dt_dj = datetime.astimezone(timezone(timedelta(hours=9)))
# print(utc_dt_dj)

# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
#
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
#
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
#
# 小结
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。


print("---------------------------------------------------------------------------------")
print(haha())
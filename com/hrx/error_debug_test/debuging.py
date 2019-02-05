#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/5 下午11:09
# @Author  : Aries
# @Site    : 
# @File    : debuging.py
# @Software: PyCharm

# todo 调试
# todo 第一种 把有问题的参数 全部print() 然后 一一排查


# todo 第二种是 断言 assert
import logging

logging.basicConfig(level=logging.INFO)

# def foo(s):
#     i = int(s)
#     assert i != 0, "i is zero"
#     return 10 / i
#
#
# foo('0')
# 断言的意思就是说i!=0则程序没有异常  反之抛出"i is zero"
# 这种断言的方式其实也是比较粗暴的 不过 启动Python解释器时可以用-O参数来关闭assert：  其实同样很瓜皮 这里不推荐


# todo  第三种 就是打log的方式
print("------------------------------------------记录问题---------------------------------------------------")


# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，
# logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
# todo log关键字优先级 warn info debug error....

def foo(s):
    i = int(s)
    logging.info("i = %s" % i)
    logging.debug("i = %s" % i)
    logging.warning("i = %s" % i)
    logging.error("i = %s" % i)
    return 10 / i


foo('0')

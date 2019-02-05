#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/5 下午10:54
# @Author  : Aries
# @Site    : 
# @File    : err_logging.py
# @Software: PyCharm
import logging

print("------------------------------------------记录问题---------------------------------------------------")


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()

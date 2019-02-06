#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/6 下午2:23
# @Author  : Aries
# @Site    : 
# @File    : MyDict.py
# @Software: PyCharm
import logging


class MyDict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            logging.info("the dict has no attrs %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

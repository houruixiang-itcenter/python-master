#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 下午6:01
# @Author  : Aries
# @Site    : 
# @File    : Animal.py
# @Software: PyCharm
from com.hrx.ood.Animal import Animal
from com.hrx.ood.Bird import Bird
from com.hrx.ood.MixIn.FlyableMixIn import FlyableMixIn


class Parrot(Bird,FlyableMixIn):
    pass

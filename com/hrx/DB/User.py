# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 下午2:00
# @Author  : Aries
# @Site    :
# @File    : User.py
# @Software: PyCharm

# todo  创建对象的基类
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
	
	
	# 表的名字:
	__tablename__ = 'user'
	
	# 表结构
	id = Column(String(20), primary_key=True)
	name = Column(String(20))



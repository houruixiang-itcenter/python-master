#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 下午8:18
# @Author  : Aries
# @Site    : 
# @File    : SQLAlchemyOperation.py
# @Software: PyCharm

# todo SQLAlchemy
# python DB-API 会返回这样的结果
# [
#     ('1', 'Michael'),
#     ('2', 'Bob'),
#     ('3', 'Adam')
# ]

# todo 基于SQLAlchemy ORM框架的数据库增删改查的操作类
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from com.hrx.DB.User import User

engine = create_engine('mysql+mysqlconnector://root:HRX552299@localhost:3306/test')
# todo 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()

for i in range(1, 10):
	usr = User(id=str(i), name='mm %d' % random.randint(100, 200))
	session.add(usr)
	session.commit()
# usr = User(id='1', name='mm %d' % random.randint(100,200))
# session.add(usr)
# session.commit()
# user = User(id='1', name='ljp')
# session.add(user)
# session.commit()

usr = session.query(User).filter(User.id == '1').all()
print(list(usr))
session.close()

# 可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。
#
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
#
# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下：
#
# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')
#
# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))
# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。
#
# 小结
# ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
#
# 正确使用ORM的前提是了解关系数据库的原理

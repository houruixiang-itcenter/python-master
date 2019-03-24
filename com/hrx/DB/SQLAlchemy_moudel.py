#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 下午8:15
# @Author  : Aries
# @Site    : 
# @File    : SQLAlchemy_moudel.py
# @Software: PyCharm

# todo SQLAlchemy
# python DB-API 会返回这样的结果
# [
#     ('1', 'Michael'),
#     ('2', 'Bob'),
#     ('3', 'Adam')
# ]

# todo SQLAlchemy  其实就是python中的orm框架

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# todo 初始化数据库连接
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
# todo '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
from com.hrx.DB.User import User

engine = create_engine('mysql+mysqlconnector://root:HRX552299@localhost:3306/test')
# todo 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# todo ok到此为止  ORM的模型已经创建成功
# todo  下面开始sql的操作  添加一条记录 :注意 在orm中 xxx类就是一个数据库表  xxx对象就对应的一行数据  每个字段对象类中的一个变量
# todo 创建session对象 就是python代码与数据库的会话层
session = DBSession()
# 创建uesr对象
user = User(id='0', name='ljp')
# todo 创建表结构
user.metadata.create_all(engine)
# 添加到session中
# todo 这里的session相当于DB-API中cursor
session.add(user)
session.commit()
session.close()

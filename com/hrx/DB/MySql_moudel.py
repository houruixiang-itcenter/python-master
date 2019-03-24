#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 下午6:21
# @Author  : Aries
# @Site    :
# @File    : MySql_moudel.py
# @Software: PyCharm


# todo Mysql使用前须知
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。
# MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
import mysql.connector

# todo 注意在mysql中占位符 只能是%s
# try:
# 	conn = mysql.connector.connect(user='root', password='HRX552299', database='test')
# 	cor = conn.cursor()
# 	cor.execute('create table person (id int(20) primary key,name varchar(20),age varchar(20),sex varchar(20))')
# 	for i in range(10):
# 		cor.execute('insert into person (id,name,age,sex) values (%s,%s,%s,%s)', (i, 'gh %s' % i, '18', 'null'))
# 	conn.commit()
# finally:
# 	conn.close()
# 	cor.close()

# todo 下面进行 mysql的查询logic
# todo 注意在mysql中占位符 只能是%s 可以理解为就是一个通配符而已
try:
	conn = mysql.connector.connect(user='root', password='HRX552299', database='test')
	cor = conn.cursor()
	cor.execute(r"select * from person where id > 2 and id < 8")
	values = cor.fetchall()
	print(values)
finally:
	conn.close()
	cor.close()

# 由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。
# 小结
# 执行INSERT等操作后要调用commit()提交事务；
#
# MySQL的SQL占位符是%s。

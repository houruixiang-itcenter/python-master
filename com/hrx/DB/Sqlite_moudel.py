#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 下午10:04
# @Author  : Aries
# @Site    :
# @File    : Sqlite_moudel.py
# @Software: PyCharm

# SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
#
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
#
# 在使用SQLite前，我们先要搞清楚几个概念：
#
# 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
#
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
#
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
#
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
#
# 由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。


# todo  下面来实践一下sqlite
import sqlite3

# todo 首先来连接数据库  如果不存在则会自己创建
conn = sqlite3.connect('test.db')
# todo 创建一个游标来取数据
cursor = conn.cursor()
# todo 执行sql语句来创建usr表
try:
	cursor.execute('create table usr (id varchar(20) primary key, name varchar(20),age varchar(20))')
except:
	print('the usr already create')
# todo 继续执行sql语句插入一条数据
cursor.execute('insert into usr (id,name) values (\'1\',\'hrx\')')

# todo 关闭 cursor
cursor.close()
# todo 提交事务
conn.commit()
# todo 关闭连接
conn.close()

print('----------------------------------------------下面进行查询数据库--------------------------------------------------')
# todo 查询过程中  继续使用cursor进行增删改查
conn = sqlite3.connect('test.db')
cor = conn.cursor()
cor.execute('select * from usr where id=?', ('1',))
# todo 获取查询之后的数据集
values = cor.fetchall()
print(str(values))
cor.close()
conn.close()

# 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
#
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
#
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
#
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
#
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
# SQLite支持常见的标准SQL语句以及几种常见的数据类型。具体文档请参阅SQLite官方网站。

# 小结
# 在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
#
# 要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
#
# 如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。
print('--------------------------------------------sqlite test-------------------------------------------------------')
# 初始数据:
conn = sqlite3.connect('test1.db')
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()
try:
	con = sqlite3.connect('test1.db')
	csr = con.cursor()
	csr.execute(r"select * from user where score >= 70 and score <= 90")
	print(str(csr.fetchall()))
finally:
	csr.close()
	con.close()
	






























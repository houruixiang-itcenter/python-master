# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 下午3:15
# @Author  : Aries
# @Site    :
# @File    : Custom_DB.py
# @Software: PyCharm
import asyncio
import logging

import aiomysql as aiomysql

logging.basicConfig(level=logging.INFO)


# todo pythin3-webapp 数据库封装

# todo 创建复连接池
# 连接池好处就是不需要频繁的打开和关闭数据库连接,而且可以频繁的进行复用
# todo 连接池由全局变量__pool 存储,缺省情况下编码设置为'utf-8' 然后自动提交事务


@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(host=kw.get('host', 'localhost'),
                                             port=kw.get('port', 3306),
                                             user=kw['user'],
                                             password=kw['password'],
                                             db=kw['db'],
                                             charset=kw.get('charset', 'utf8'),
                                             autocommit=kw.get('autocommit', True),
                                             maxsize=kw.get('maxsize', 10),
                                             minsize=kw.get('minsize', 1),
                                             loop=loop

                                             )


# todo 查询select
# SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。注意要始终坚持使用带参数的SQL，而不是自己拼接SQL字符串，这样可以防止SQL注入攻击。
#
# 注意到yield from将调用一个子协程（也就是在一个协程中调用另一个协程）并直接获得子协程的返回结果。
#
# 如果传入size参数，就通过fetchmany()获取最多指定数量的记录，否则，通过fetchall()获取所有记录
@asyncio.coroutine
def select(sql, args, size=None):
    logging.info(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)  # type:aiomysql.Cursor
        yield from conn.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs


# todo insert/update/delete
def execute(sql,args):
    logging.info(sql, args)
    # with (yield from __pool) as conn:









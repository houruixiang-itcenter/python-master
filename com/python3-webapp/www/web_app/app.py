#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 下午2:24
# @Author  : Aries
# @Site    : 
# @File    : app.py
# @Software: PyCharm
import asyncio
import logging
# 指定终端面板展示log的级别  *必须
logging.basicConfig(level=logging.INFO)

from aiohttp import web


def index(request):
    # 需要注意的是 不加headers会默认为下载
    return web.Response(body=b'<h1>this is home page</h1>', headers={'content-type': 'text/html'})


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    # 进行并发操作
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
loop.close()

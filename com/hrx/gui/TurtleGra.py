#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 下午5:58
# @Author  : Aries
# @Site    : 
# @File    : TurtleGra.py
# @Software: PyCharm

from turtle import *

# 这些Api是Turtle中的api

# # 设置笔刷宽度
# width(4)
#
# # 前进
# forward(200)
# # 右转90度
# right(90)
#
# # 笔刷颜色
# pencolor('red')
# forward(100)
# right(90)
#
# # 笔刷颜色
# pencolor('green')
# forward(200)
# right(90)
#
# # 笔刷颜色
# pencolor('blue')
# forward(100)
#
# #  调用done()使得窗口等待被关闭,否则将立即关闭窗口;
# done()


# https://docs.python.org/3.3/library/turtle.html#turtle-methods turtle官网
# pencolor('blue')
#
#
# def drawStar(x, y):
#     pu()
#     goto(x, y)
#     pd()
#     # set heading: 0
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)
#
#
# for x in range(0, 255, 50):
#     drawStar(x, 0)
#
# done()


# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)


def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)


speed("fastest")

draw_tree(l, 4)

done()

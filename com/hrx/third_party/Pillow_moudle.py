#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 下午6:30
# @Author  : Aries
# @Site    :
# @File    : Pillow_moudle.py
# @Software: PyCharm


# todo 操作图像

# 打开一个png图片
import random

from PIL import Image, ImageFilter, ImageFont, ImageDraw

# 这里记录一个bug:pip: command not found
# 主要是有3种可能的原因吧:
# todo 1.pip没有安装
# todo  2.pip已经安装 但是没有指明path  可以echo $PATH进行路径的查看
# todo 3.还有一种可能  你安装的pip3 不是pip 所以你需要甄别  是pip 的命令还是 pip3的命令   可以使用which pip/pip3来看你到底安装了哪一种pip


im = Image.open('test.png')  # type: Image.Image
w, h = im.size
print('当前的size %s ,%s' % (w, h))
# 缩放 50%
im.thumbnail((w / 2, h / 2))
im.save('test1.png', 'png')

# 加滤镜 --- 应用模式滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('test2.png', 'png')


# todo 绘制验证码
# 仅仅是大写字母
def rnChar():
	return chr(random.randint(65, 90))


def rnBgColor():
	return random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)


def rnFontColor():
	return random.randint(30, 100), random.randint(30, 100), random.randint(30, 100)


w = 240
h = 60
image = Image.new('RGB', (w, h), (255, 255, 255))
# 创建一个font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 开始绘制背景的每一个像素点
for x in range(w):
	for y in range(h):
		draw.point((x, y), fill=rnBgColor())
# 开始绘制文字
for i in range(4):
	draw.text((60 * i + 10, 10), rnChar(), fill=rnFontColor(), font=font)
# 模糊处理
image = image.filter(ImageFilter.BLUR)
image.save('varcode.jpg', 'jpeg')

# 小结
# PIL提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理。

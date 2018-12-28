# -*-coding:utf-8-*-
import math


class common:

    def my_abs(x):
        if x >= 0:
            return x
        else:
            return -x

    def my_abs_check(x):
        # 类型检查
        if not isinstance(x, (int, float)):
            raise TypeError('哈哈哈')
        if x >= 0:
            return x
        else:
            return -x

    # 返回多个值
    # math 机型
    def move(x, y, step, angle=0):
        nx = x + step * math.cos(angle)
        ny = y - step * math.sin(angle)
        return nx, ny

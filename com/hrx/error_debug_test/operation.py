#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/5 上午11:35
# @Author  : Aries
# @Site    :
# @File    : operation.py
# @Software: PyCharm


class Operation(object):

    def __init__(self):
        pass

    # 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，
    # 返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回 - 1。

    # 错误码需要在代码中添加一部分判断 进行返回   再者错误码 必须有明确的错误返回码文档才可以
    # todo  当然 我觉得错误码返回于情于理也是可以的   但是我们还是可以 的
    # todo  但是同java  一般  python 也会有try...except...finally...的错误机制

    # todo 1.首先执行try中的代码块  2.执行异常在except中进行捕获  3.finally 不管执行是否有异常最后终会被走到
    try:
        # print(10 / 0)
        print(10 / int('b'))
    except ZeroDivisionError as e:
        print("error type: ", e)
    except UnicodeError as e:
        print('UnicodeError')
    except ValueError as e:
        print('ValueError')
    except  BaseException as e:
        print("error type: unknow")
    else:
        print("no error")
    finally:
        print("done")

    # todo 由上来看  try是执行当前代码块  异常时候依次走except 如果except有对应的错误类型 则会被捕获掉
    # todo 如果有异常但是没有对应异常类型 则会走到Exception 因为BaseException是所有异常的子类 如果前面没有捕获则会在BaseException中进行捕获
    # todo 如果没有捕获则会走 else  不管是否有异常 都会走到finally中执行   其中的代码块
    # todo 继承关系 -- https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    print("------------------------------------------except跨层抛出---------------------------------------------------")

    # 在类中定义function 如果是空参必须传入 self
    def foo(self, s):
        return 10 / int(s)

    def bar(self, s):
        return self.foo(s) * 2

    def main(self):
        try:
            self.bar('c')
        except Exception as e:
            print('Error:', e)
        finally:
            print('finally...')


o = Operation()
o.main()

# todo  在try...except时候 调用位置很重要  不需要每次异常都进行调用

print("------------------------------------------调用栈---------------------------------------------------")


# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：
# todo 通过调用栈来定位error位置
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()

# todo 错误信息如下
# todo  下面 这一行告诉我们是错误跟踪信息
# Traceback (most recent call last):
# todo 下面两行告诉我们是main()出错了 位置在operation.py的第84行
#   File "/Users/houruixiang/python/python-master/com/hrx/error_debug_test/operation.py", line 84, in <module>
#   main()
# todo 下面两行告诉我们是bar('0')出错了 位置在operation.py的第81行
#   File "/Users/houruixiang/python/python-master/com/hrx/error_debug_test/operation.py", line 81, in main
#     bar('0')
# todo 下面两行告诉我们是 return foo(s) * 2出错了 位置在operation.py的第77行
#   File "/Users/houruixiang/python/python-master/com/hrx/error_debug_test/operation.py", line 77, in bar
#     return foo(s) * 2
# todo 下面三行告诉我们是 return 10 / int(s)出错了 位置在operation.py的第73行 根据错误类型ZeroDivisionError，
# todo 我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。
#   File "/Users/houruixiang/python/python-master/com/hrx/error_debug_test/operation.py", line 73, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero



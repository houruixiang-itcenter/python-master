#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/6 下午3:04
# @Author  : Aries
# @Site    : 
# @File    : unit1.py
# @Software: PyCharm
# todo 导入单元测试的包
import unittest

from com.hrx.unit_test.MyDict import MyDict

# 小结
# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
#
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
#
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
#
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。


class TestDict(unittest.TestCase):

    # 调用一个测试方法前调用
    def setUp(self):
        print('setUp...')

    # 调用一个测试方法后调用
    def tearDown(self):
        print('tearDown...')

    # 初始化测试
    def test_init(self):
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    # key值测试 判断通过key取出的value  是否正确
    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    # 属性测试 属性测试  1.判断是否有key属性  2.判断通过key取出的value  是否正确
    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    # key-error 异常测试 当通过d['empty']取value  key不存在时候 断言会抛出异常KeyError
    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    # 属性异常测试  当通过d.empty取value  key不存在时候 断言会抛出异常AttributeError
    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty


print("------------------------------------------启动单元测试---------------------------------------------------")
if __name__ == '__main__':
    unittest.main()

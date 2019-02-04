# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 下午10:27
# @Author  : Aries
# @Site    :
# @File    : ORM.py
# @Software: PyCharm

# 字段base定义
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s:%s>' % (self.__class__.__name__, self.name, self.column_type)


# 定义str类型的字段
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


# 定义int类型的字段
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class BDModelMetaclass(type):
    def __new__(cls, name, base, attrs):
        if name == 'BDModel':
            return type.__new__(cls, name, base, attrs)
        print("found model is %s" % name)
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("found cur field :%s ,%s" % (k, v))
                mapping[k] = v
        # 做一个容错 防止属性冲突
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mapping
        attrs['__table_name__'] = name
        return type.__new__(cls, name, base, attrs)


class BDModel(dict, metaclass=BDModelMetaclass):
    def __init__(self, **kw):
        super(BDModel, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            print('found key is error', key)

    def __setattr__(self, key, value):
        self[key] = value

    # save  保存数据库
    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join('%s' % item for item in args))
        print('SQL: %s' % sql)


class Person(BDModel):
    id = IntegerField('id')
    name = StringField('name')
    age = IntegerField('age')

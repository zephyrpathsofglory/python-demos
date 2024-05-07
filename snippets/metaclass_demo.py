#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Michael"


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        # In Python 3, the super(Square, self) call is equivalent to the parameterless super() call.
        super(StringField, self).__init__(name, "varchar(100)")


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, "bigint")


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print(cls)
        if name == "Model":
            print("Model class")
            return type.__new__(cls, name, bases, attrs)
        print("Found model: %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings  # 保存属性和列的映射关系
        attrs["__table__"] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = "insert into %s (%s) values (%s)" % (
            self.__table__,
            ",".join(fields),
            ",".join(params),
        )
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))


# testing code:


class User(Model):
    id = IntegerField("uid")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")


u = User(id=12345, name="Michael", email="test@orm.org", password="my-pwd")
u.save()

import inspect


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print(cls, __class__)
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Son(Singleton):
    a = 1


a = Son()
b = Son()

print(a, b)


class Singleton2(object):
    _state = {"kao": "fuck"}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class Son2(Singleton2):
    var = 1


c = Son2()
d = Son2()

print(c.__dict__, d.__dict__)
print(c, d)


def singleton(cls):
    instance = {}
    print(cls)

    def getsssinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getsssinstance


@singleton
class MyClass(object):
    a = 1


e = MyClass()
f = MyClass()

print(e, f)


class Singleton3(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance


class Son4(metaclass=Singleton3):
    a = 1


g = Son4()
h = Son4()

print(g)
print(h)
print(type(Son4))
print(type(g))


class Person:
    name=[]


p1=Person()
p2=Person()
p1.name.append(1)
print(p1.name)  # [1]
print(p2.name)  # [1]
print(dir(Person))

print(inspect.getmembers(p1))
print(inspect.getmembers(p2))
print(inspect.getmembers(Person))

print(Person.name)  # [1]
num = 5


class A(object):
    num = 0

    def __init__(self, lst=[]):
        print(id(lst))
        self.lst = lst

    def add(self, value):
        num = value
        self.lst.append(value)


class B(A):
    def __init__(self, *args):
        super(B, self).__init__(*args)


def print_lst(obj):
    print(num, obj.num, obj.lst, id(obj.lst))


a = A()
B.num = 1
a.add(2)
b = B()
b.add(3)
print_lst(a)
print_lst(b)
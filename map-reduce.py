from functools import reduce


def trans(s):
    return s.lower().title()


def prod(x, y):
    return x * y


def is_odd(num):
    return num % 2 == 0

a = map(trans, ['adam', 'LISA', 'barT'])
print(a)
print(tuple(a))
print(list(a)) # iterator iterated
print(set(a))

print(reduce(prod, [1, 2, 3, 4, 5, 6]))

print(tuple(filter(is_odd, [1, 2, 3, 4, 5, 6])))
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))
print(set(filter(is_odd, [1, 2, 3, 4, 5, 6])))
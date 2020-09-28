from collections import Iterable, Iterator
import sys
a = [1, 3, 5]

b = iter(a)

c = list(b)

d = list(b) # iterator iterated


print(a, b, c, d)
print(id(a), id(c))

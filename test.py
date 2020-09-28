# l default value refer to a fixed address

def f(x,l=[]):
    print(id(l))
    for i in range(x):
        l.append(i*i)
    print(id(l))
    print(l)

# f(2)
# f(3,[3,2,1])
# f(3)
# f(3)
# f(2,[3,2,1])

def g(x, l=None):
    print(id(l))
    l = []
    for i in range(x):
        l.append(i*i)
    print(id(l))
    print(l)
    
g(2)
g(3,[3,2,1])
g(3)
g(3)
g(2,[3,2,1])
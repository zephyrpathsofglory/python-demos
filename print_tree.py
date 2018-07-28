class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n0.left = n1
n0.right = n2
n1.left = n3
n2.right = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8


def print_tree():
    cache = [n0]
    while len(cache) > 0:
        length = len(cache)
        cache_extend = []
        cache_print = []
        for i in range(length):
            popped = cache.pop(0)
            cache_print.append(popped)
            if popped.left is not None:
                cache_extend.append(popped.left)
            if popped.right is not None:
                cache_extend.append(popped.right)
        for item in cache_print:
            print(item.value, end=' ')
        print()
        cache.extend(cache_extend)
        yield


a = print_tree()
while True:
    try:
        next(a)
    except Exception:
        exit()


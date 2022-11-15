# _*_coding=utf-8 _*_

# 重点：子进程创建时会复制父进程中的所有变量
import time
from multiprocessing import Process

l = [1]


def add(n):
    a = 3 + 4j
    print(type(a))
    l.append(n)
    time.sleep(5)
    print(l)


p1 = Process(target=add, args=(2,))
p2 = Process(target=add, args=(3,))
p1.daemon = True
p2.daemon = True

p1.start()
p2.start()
p1.join()
p2.join()

l.append(0)
print(p1.is_alive(), p2.is_alive())
time.sleep(10)

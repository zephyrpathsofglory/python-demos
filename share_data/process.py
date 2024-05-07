import multiprocessing
from multiprocessing import Process


def f(n, a):
    print(multiprocessing.current_process().name)
    print(multiprocessing.parent_process().name)
    print("f", n, a)
    print(id(n), id(a))

    n = 3.14

    for i in range(len(a)):
        a[i] = -a[i]
    print("f", n, a)

    print(id(n), id(a))


if __name__ == "__main__":
    print(multiprocessing.current_process().name)
    num = 0.0
    arr = list(range(5))
    print(id(num), id(arr))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num, arr)

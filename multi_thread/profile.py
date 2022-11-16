# _*_ coding:utf-8 _*_
import threading
import time


def decrement(n):
    while n > 0:
        n -= 1


def testMainThread():
    print("main thread")
    start = time.time()
    decrement(100000000)
    cost = time.time() - start
    print(cost)


def testSingleThread():
    print("single thread")
    start = time.time()
    t = threading.Thread(target=decrement, args=[50000000])
    t.start()
    t.join()
    cost = time.time() - start
    print(cost)


def testMultiThread():
    print("multi thread")
    start = time.time()

    t1 = threading.Thread(target=decrement, args=[50000000])
    t2 = threading.Thread(target=decrement, args=[50000000])

    t1.start()  # 启动线程，执行任务
    t2.start()  # 同上
    t1.join()  # 主线程阻塞，直到t1执行完成，主线程继续往后执行
    t2.join()  # 同上

    cost = time.time() - start
    print(cost)


if __name__ == "__main__":
    testMainThread()
    testSingleThread()
    testMultiThread()

# _*_ coding:utf-8 _*_
import threading
import time


def decrement(n):
    while n > 0:
        n -= 1


# single-threading
# start = time.time()
# decrement(100000000)
# cost = time.time() - start
# print(cost)


# multi-thread
start = time.time()

t1 = threading.Thread(target=decrement, args=[50000000])
t2 = threading.Thread(target=decrement, args=[50000000])

t1.start()  # 启动线程，执行任务
t2.start()  # 同上
print("start")
t1.join()  # 主线程阻塞，直到t1执行完成，主线程继续往后执行
print("2")
t2.join()  # 同上
print("end")

cost = time.time() - start
print(cost)

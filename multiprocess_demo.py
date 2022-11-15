from multiprocessing import Pool
import os
import time
import random
import multiprocessing


def task(name):
    print('run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 5 + 1)
    end = time.time()
    print('task %s run %0.f seconds' % (name, end - start))


if __name__ == '__main__':
    print('parenet process: %s' % os.getpid())
    p = Pool(processes=4)
    print('pool size: %s' % p._processes)
    p._processes = 6

    print('pool size: %s' % p._processes)

    for i in range(5):
        p.apply_async(task, args=(i,))
    print('waiting for all processes done....')
    p.close()

    p.join()
    print('all process done.')

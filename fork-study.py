import os
import time
from multiprocessing import Process
import threading
import subprocess


print(os.getpid())


# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# time.sleep(10)
# os.system('sleep 10')


def run_proc(name):
    print('run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('parenet pid: %s', os.getpid())
    p = Process(target=run_proc, args=('test_code',))
    print('child process will starts')
    p.start()
    p.join()
    print('child process stopped.')
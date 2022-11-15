import os
import sys
import time
from multiprocessing import Process

# worker process 也执行了这个文件，下面的打印了2次，为什么？
print("my pid:")
print(os.getpid())


def worker():
    print("I am worker!")
    time.sleep(1)
    sys.exit(1)


def main():
    Process(target=worker, args=()).start()


if __name__ == "__main__":
    main()

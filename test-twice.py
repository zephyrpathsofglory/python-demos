import sys
from multiprocessing import Process
import time

now = time.time()
print(now)

fr = [1, 2, 3]
for i in fr:
    print(3)

print(1)


def worker():
    print('worler line')
    time.sleep(1)
    sys.exit(1)


def main():
    print('start worker')
    Process(target=worker, args=()).start()
    print('main line')


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('duration:', end - start)
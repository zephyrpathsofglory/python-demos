import sys


def fibonacci(n):
    print('enter function')
    a, b, counter = 0, 1, 0
    while True:
        print("enter while")
        if counter > n:
            return
        yield a
        print("after yield")
        a, b = b, a+b
        counter += 1


f = fibonacci(10)

while True:
    try:
        print('before next')
        print(next(f), end=" ---- ")
    except StopIteration:
        sys.exit()

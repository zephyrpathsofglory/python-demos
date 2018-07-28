lst = [lambda x: i * x for i in range(4)]
print([m(2) for m in lst])
# zenm dayin [0, 2 ,4 ,6]

def generator():
    print('aaa')
    yield 'bbb'
    print('ccc')


def func(g):
    try:
        print('start')
        i = next(g)
        print(i)
    except Exception:
        print('error')
    else:
        print('ok')
    finally:
        print('end')

print(func.__closure__)

g = generator()
func(g)
func(g)
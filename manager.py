# manager is used for sharing data between processes

from multiprocessing import Process, Manager


def f(d, l):
    d[1] = 'l'
    d['2'] = 2
    d[0.24] = None
    l.reverse()


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d, l)
import asyncio


def func_1(end_time, loop):
    print("func1 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_2, end_time, loop)
    else:
        loop.stop()


def func_2(end_time, loop):
    print("func2 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_3, end_time, loop)
    else:
        loop.stop()


def func_3(end_time, loop):
    print("func3 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_1, end_time, loop)
    else:
        loop.stop()


def func_4(end_time, loop):
    print("func4 called")

    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_4, end_time, loop)
    else:
        loop.stop()


main_loop = asyncio.get_event_loop()

end_loop_time = main_loop.time() + 9.0
main_loop.call_soon(func_1, end_loop_time, main_loop)
print("start run")
main_loop.run_forever()
print("end run")
main_loop.close()

# _*_ coding=utf-8 _*_


def print_msg():
    # print_msg 是外围函数
    msg = "zen of python"
    value = 'books'
    print(id(msg), id(value))

    def printer():
        # printer 是嵌套函数
        print(msg)
        print(value)
    print(id(printer))
    return printer

print(type(print_msg))

print(print_msg.__closure__)

another = print_msg()
print(another)
print(type(another))
print(another.__closure__)
# 输出 zen of python
another()
print(print_msg.__closure__)

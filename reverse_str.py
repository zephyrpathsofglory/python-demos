# reverse a string using recursion


def reverse(s):
    if len(s) > 1:
        return s[-1] + reverse(s[0: -1])
    else:
        return s


r = reverse('abcdefg')
print(r)

def replace_str(str1, str2):
    if len(str1) > len(str2):
        replace_same(str2, str1)
    else:
        replace_same(str1, str2)


def replace_same(shorter, longer):
    for c in shorter:
        print(c)
        if longer.find(c) != -1 and c != "_":
            print('contains')
            shorter = shorter.replace(c, "_")
            longer = longer.replace(c, "_")


s1 = 'acbef2'
s2 = 'bfgirls'
replace_str(s1, s2)
print(s1, s2)
print()

s3 = 'asdfsdf'
s4 = s3.replace('sd', '_')
print(s4)

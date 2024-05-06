"""
题目描述

给定一个字符串 s，最多只能进行一次变换，返回变换后能得到的最小字符串(按照字典 序进行比较)变换规则:
交换字符串中任意两个不同位置的字符

输入描述

一串小写字母组成的字符串 s

输出描述

按照要求进行变换得到的最小字符串。

用例1

输入abcdef输出abcdef说明abcdef已经是最小字符串，不需要交换。用例2

输入bcdefa输出acdefb说明a和b进行位置交换，可以得到最小字符串
"""


def result(s):
    min_arr = list(s)
    min_arr.sort()  # 先排序一把
    # 边界判断
    if s == "".join(min_arr):  # 这里因为minArr已经是list了。
        return s
    s_arr = list(s)  # 把s搞成list
    # 然后一个个来对比。
    for i in range(len(s)):
        # 因为已经拍好序了，所以第一个出现不同的就要把他揪出来。
        if s_arr[i] != min_arr[i]:
            # 把sArr[i] 存好，
            tmp = s_arr[i]
            # 把sArr[i]替换成minArr[i]
            s_arr[i] = min_arr[i]
            # 接下来就要找tmp 在sArr的位置了。从右边开始找。
            swap_idx = s.rindex(min_arr[i])
            s_arr[swap_idx] = tmp
            # 找到了就break结束循环
            break
    return "".join(s_arr)


assert result("aabbdfe") == "aabbdef"

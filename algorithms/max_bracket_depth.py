"""
现有一字符串仅由"("，")", "{","}", "[", "]"六种括号组成。若字符串满足以下条件之一，

则为无效字符串:任一类型的左右括号数量不相等

存在未按正确顺序(先左后右)闭合的括号输出括号的最大嵌套深度，若字符串无效则输出0。

0<=字符串长度<=100000

输入描述

一个只包括(，’)’，’{‘，”}”，[，”]”的字符串

输出描述

整数，最大的括号深度

"""


def result(s: str):
    depth = 0
    maxDepth = 0
    stack = []
    map = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if map.get(char) is not None:
            if len(stack) == 0:
                return 0

            if map[char] == stack[-1]:
                depth -= 1
                stack.pop()
            else:
                return 0
        else:
            stack.append(char)
            depth += 1
            if depth > maxDepth:
                maxDepth = depth

    if len(stack) > 0:
        return 0

    return maxDepth


assert result("(((){{()[]}}))") == 5
assert result(")(") == 0
assert result("(]") == 0
assert result("([)]") == 0
assert result("[]") == 1
assert result("([]{()})") == 3

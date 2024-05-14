"""
给定一组int类型的数据，表示客人的按摩时间，服务完一个客人之后需要休息（不能服务连续的2个客人），如何帮按摩师选择客人来打到最大的总按摩时间
示例：
1,2,3,1 (1,3) 4
2,7,9,3,1 (2,9,1) 12
2,1,4,5,3,1,1,3(2,4,3,3) 12
"""

from typing import List


# 递归，数组size大了之后就会出现深堆栈，容易超时，而且要占用更多内存
class Solution:
    def answer(self, nums: List[int]) -> int:
        def f(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]

            if len(nums) == 2:
                return max(nums[0], nums[1])

            # 动态规划，选择第一个，下一次从第三个开始，不选择第一个，从第二个开始，2种情况取最大值
            return max(nums[0] + f(nums[2 : len(nums)]), f(nums[1 : len(nums)]))

        return f(nums)


assert Solution().answer([1, 2, 3, 1]) == 4
assert Solution().answer([2, 7, 9, 3, 1]) == 12
assert Solution().answer([2, 1, 4, 5, 3, 1, 1, 3]) == 12


class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            first, second = second, max(first + nums[i], second)

        return second


assert Solution2().rob([1, 2, 3, 1]) == 4
assert Solution2().rob([2, 7, 9, 3, 1]) == 12
assert Solution2().rob([2, 1, 4, 5, 3, 1, 1, 3]) == 12

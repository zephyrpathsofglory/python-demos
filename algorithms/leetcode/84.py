"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

输入： heights = [2,4]
输出： 4
"""

from typing import Deque, List


class Solution:
    def largest_rect(self, heights: List[int]) -> int:
        mono_stack = Deque([0])
        heights.append(0)
        heights.insert(0, 0)
        max_area = 0

        for idx in range(1, len(heights)):
            while 1:
                if heights[idx] >= heights[mono_stack[-1]]:
                    break
                else:
                    last_idx = mono_stack.pop()
                    last = heights[last_idx]
                    prev = mono_stack[-1]

                    max_area = max(max_area, last * (idx - prev - 1))

            mono_stack.append(idx)

        return max_area


assert Solution().largest_rect([2, 1, 5, 6, 2, 3]) == 10
assert Solution().largest_rect([2, 1, 5, 6, 2, 3, 2, 3]) == 12
assert Solution().largest_rect([2, 1, 5, 5, 6, 2, 3]) == 15
assert Solution().largest_rect([2, 4]) == 4
assert Solution().largest_rect([1, 3, 4, 500, 2, 7, 4]) == 500
assert Solution().largest_rect([1, 3, 4, 5, 2, 7, 4]) == 12

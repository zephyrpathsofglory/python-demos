"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lastIdx = len(height) - 1
        li = 0
        ri = lastIdx

        maxArea = height[0]

        while li != ri:
            size = min(height[li], height[ri]) * (ri - li)
            maxArea = max(maxArea, size)
            if height[li] > height[ri]:
                ri -= 1
            else:
                li += 1

        return maxArea


assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution().maxArea([1]) == 1
assert Solution().maxArea([4, 3, 2, 1, 4]) == 16
assert Solution().maxArea([1, 1]) == 1
assert Solution().maxArea([1, 2, 1]) == 2

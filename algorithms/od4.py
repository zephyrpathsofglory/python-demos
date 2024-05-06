"""
数组water表示一排瓶子的水位高度。小明往这些瓶子内浇水，1次操作可以使1个瓶子的水位增加1。给定一个整数cnt，
表示小明想通过浇水获得cnt个水位高度一致的瓶子。求最少需要浇水多少次？
返回的结果需要对1000000007取模。
输入：
water = [7,1,9,10]
cnt = 3
输出：
4
"""

from typing import List


class Solution:
    def minWatering(self, heights: List[int], cnt: int) -> int:
        heights.sort()
        delta = []

        for i in range(len(heights) - 1):
            delta.append(heights[i + 1] - heights[i])

        min_watering = -1
        for i in range(len(delta) - 1):
            tmp = delta[i] + 2 * delta[i + 1]
            if min_watering == -1:
                min_watering = tmp
            else:
                min_watering = min(min_watering, tmp)

        return min_watering


assert Solution().minWatering([7, 1, 9, 10], 3) == 4
assert Solution().minWatering([7, 1, 9, 9, 10], 3) == 2
assert Solution().minWatering([7, 1, 9, 10, 10], 3) == 1
assert Solution().minWatering([7, 1, 9, 9, 9, 10], 3) == 0

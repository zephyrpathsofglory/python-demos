"""
二维接雨水
给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
"""

from typing import List


# 错误的 Solution
class Solution:
    def _max_containing_water_one_dimension(self, heights: List[int]) -> List[int]:
        states = [[i] for i in heights]
        max = 0
        lenz = len(heights)

        for idx in range(lenz):
            height = heights[idx]
            if height > max:
                max = height

            states[idx].append(max)

        max = 0
        idx = lenz - 1
        while idx >= 0:
            height = heights[idx]
            if height > max:
                max = height

            states[idx].append(max)
            idx -= 1

        waters = []
        for state in states:
            waters.append(min(state[2], state[1]) - state[0])

        return waters

    def max_containing_water_two_dimension(self, heights: List[List[int]]) -> int:
        waters = [self._max_containing_water_one_dimension(hs) for hs in heights]
        one_dimension_lenz = len(heights[0])
        veticle_waters = []
        for i in range(one_dimension_lenz):
            hs = [item[i] for item in heights]
            ws = self._max_containing_water_one_dimension(hs)
            veticle_waters.append(ws)

        total = 0
        for i in range(len(heights)):
            for j in range(one_dimension_lenz):
                total += min(waters[i][j], veticle_waters[j][i])

        return total


assert (
    Solution().max_containing_water_two_dimension(
        [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    )
    == 4
)

assert (
    Solution().max_containing_water_two_dimension(
        [
            [3, 3, 3, 3, 3],
            [3, 2, 2, 2, 3],
            [3, 2, 1, 2, 3],
            [3, 2, 2, 2, 3],
            [3, 3, 3, 3, 3],
        ]
    )
    == 10
)

### 错误用例，表明 水高度 等于 横竖 2个方向 的 一维维度 水高度中的 min 值，是错误的，其中 值为 4 的横竖2个方向都应该接 9 个雨水，但是
### 雨水会从下一层的右侧流出 1 个单位，即 [2][3] 坐标的位置流出。
assert (
    Solution().max_containing_water_two_dimension(
        [
            [12, 13, 1, 12],
            [13, 4, 13, 12],
            [13, 8, 10, 12],
            [12, 13, 12, 12],
            [13, 13, 13, 13],
        ]
    )
    == 14
)

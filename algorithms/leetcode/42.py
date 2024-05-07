"""
接雨水
"""

from typing import List


class Solution:
    def max_containing_water(self, heights: List[int]) -> int:
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

        return sum(waters)


assert Solution().max_containing_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert Solution().max_containing_water([4, 2, 0, 3, 2, 5]) == 9

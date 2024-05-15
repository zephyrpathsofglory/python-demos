"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]
 
提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

import heapq
from typing import List


class Solution:
    def sliding_max(self, nums: List[int], k: int) -> List[int]:
        hp = []
        for i in range(k):
            heapq.heappush(hp, (nums[i] * -1, i))

        res = []

        for i in range(len(nums) - k + 1):
            while True:
                num, idx = heapq.heappop(hp)
                if idx < i:
                    continue

                num *= -1
                res.append(num)

                if i + k >= len(nums):
                    return res

                heapq.heappush(hp, (nums[i + k] * -1, i + k))
                if idx > i:
                    heapq.heappush(hp, (num * -1, idx))

                break

        return res


assert Solution().sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert Solution().sliding_max([1], 1) == [1]

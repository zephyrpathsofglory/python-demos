"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 
提示：
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List


# 递归，数组size大了之后就会出现深堆栈，容易超时，而且要占用更多内存
class Solution:
    def rob(self, nums: List[int]) -> int:
        lenz = len(nums)
        if lenz == 1:
            return nums[0]

        if lenz == 2:
            return max(nums[0], nums[1])

        return max(nums[0] + self.rob(nums[2:lenz]), self.rob(nums[1:lenz]))


assert Solution().rob([1, 2, 3, 1]) == 4
assert Solution().rob([2, 7, 9, 3, 1]) == 12
assert Solution().rob([2, 1, 4, 5, 3, 1, 1, 3]) == 12


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

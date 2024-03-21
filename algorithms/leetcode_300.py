# Dynamic programming.

# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


assert Solution().lengthOfLIS([10, 9, 4, 5, 3, 7, 21, 18]) == 4

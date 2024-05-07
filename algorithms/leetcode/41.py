"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

示例 1：

输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。
示例 2：

输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。
 

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

"""

from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        lenz = len(nums)
        for i in range(1, lenz + 1):
            idx = i - 1
            num = nums[idx]

            while num != i and 1 <= num <= lenz:
                tmp = nums[num - 1]
                nums[num - 1] = num
                nums[idx] = tmp
                num = nums[idx]

        res = lenz + 1
        for i in range(1, lenz + 1):
            if nums[i - 1] != i:
                res = i
                break

        return res


assert Solution().first_missing_positive([3, 4, -1, 1]) == 2
assert Solution().first_missing_positive([1, 2, 0]) == 3
assert Solution().first_missing_positive([7, 8, 9, 11, 12]) == 1

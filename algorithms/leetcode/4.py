"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import Deque, List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = Deque(nums1), Deque(nums2)
        while len(nums1) + len(nums2) > 2:
            # pop 一个最小值
            if len(nums1) == 0:
                nums2.popleft()
            elif len(nums2) == 0:
                nums1.popleft()
            else:
                if nums1[0] < nums2[0]:
                    nums1.popleft()
                else:
                    nums2.popleft()

            # pop 一个最大值
            if len(nums1) == 0:
                nums2.pop()
            elif len(nums2) == 0:
                nums1.pop()
            else:
                if nums1[-1] > nums2[-1]:
                    nums1.pop()
                else:
                    nums2.pop()

        nums1 += nums2

        if len(nums1) == 1:
            return nums1.pop()
        else:
            return (nums1.pop() + nums1.pop()) / 2.0


assert Solution().find_median_sorted_arrays([1, 3], [2]) == 2
assert Solution().find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
assert Solution().find_median_sorted_arrays([1], []) == 1
assert Solution().find_median_sorted_arrays([], [1]) == 1
assert Solution().find_median_sorted_arrays([1], [1]) == 1
assert Solution().find_median_sorted_arrays([1], [2]) == 1.5

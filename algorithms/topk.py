"""
给定一个长度为 n 的无序数组 nums ，请返回数组中最大的 k 个元素。
"""

import heapq
from typing import List


# heapq 实现最小堆，底层是完全二叉树存储，树的根节点是最小值， 任意节点的子节点都比其要大
# 最大堆 与 最小堆 性质相反，同样可以通过 heapq 实现，push 元素是将元素 * -1， 取出时 再通过 * -1 恢复原始值，通过此方式 wraparound 实现最大堆
class Solution:
    def top(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k):
            heapq.heappush(heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])

        return heap


assert set(Solution().top([1, 7, 6, 3, 2], 3)) == set([3, 6, 7])
assert set(Solution().top([7, 6, 1, 3, 2], 3)) == set([7, 6, 3])

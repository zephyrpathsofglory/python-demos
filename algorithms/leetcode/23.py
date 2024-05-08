"""
给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]
 
提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按升序排列,lists[i].length 的总和不超过 10^4
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.val = value
        self.next = next


# 最小堆，push 的 item 为元组时， 元组的每一项都必须是 可以比较大小 的类型
class Solution:
    def merge_k_sorted_lists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        moving = dummy

        min_heap = []
        for idx in range(len(lists)):
            l = lists[idx]
            if l == None:
                continue

            heapq.heappush(min_heap, (l.val, idx))

        while len(min_heap) > 0:
            _, idx = heapq.heappop(min_heap)
            moving.next = lists[idx]
            moving = moving.next
            lists[idx] = moving.next
            n = lists[idx]
            if n is not None:
                heapq.heappush(min_heap, (n.val, idx))

        return dummy.next


ls1 = [
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(2, ListNode(6)),
]
t = Solution().merge_k_sorted_lists(ls1)
arr = []
while t is not None:
    arr.append(t.val)
    t = t.next

assert arr == [1, 1, 2, 3, 4, 4, 5, 6]

assert Solution().merge_k_sorted_lists([]) == None
assert Solution().merge_k_sorted_lists([None]) == None

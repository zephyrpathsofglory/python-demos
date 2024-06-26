"""
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 
如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

示例 1:

输入: root = [3,2,3,null,3,null,1]
输出: 7 
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
示例 2:

输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 当嵌套层数过多之后，有用例超时，因为每次递归涉及到了树的3层
class Solution(object):
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        x, y = 0

        if root.left is not None:
            x += self.rob(root.left)
            y += self.rob(root.left.left) + self.rob(root.left.right)

        if root.right is not None:
            x += self.rob(root.right)
            y += self.rob(root.right.left) + self.rob(root.right.right)

        return max(x, root.val + y)


class Solution2:
    def rob(self, root: Optional[TreeNode]) -> int:
        def _rob(root):
            if not root:
                return 0, 0

            ls, ln = _rob(root.left)  # ls 左子节点，偷； ln 左子节点，不偷
            rs, rn = _rob(root.right)  # rs 右子节点，偷； rn 右子节点，不偷

            return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))

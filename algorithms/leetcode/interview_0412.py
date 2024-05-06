# https://leetcode.cn/problems/paths-with-sum-lcci/description/

"""
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。
注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
提示：

节点总数 <= 10000
"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def path_sum(self, root: TreeNode, sum: int) -> int:
        def rootSum(root: TreeNode, sum):
            if root is None:
                return 0

            ret = 0
            if root.val == sum:
                ret += 1

            ret += rootSum(root.left, sum - root.val)
            ret += rootSum(root.right, sum - root.val)

            return ret

        ret = rootSum(root, sum)

        if root is None:
            return ret
        ret += self.path_sum(root.left, sum)
        ret += self.path_sum(root.right, sum)

        return ret


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

assert Solution().path_sum(root, 22) == 3


class Solution2:
    def path_sum(self, root: TreeNode, sum: int):
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root: TreeNode, curr: int):
            if root is None:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - sum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)


assert Solution2().path_sum(root, 22) == 3

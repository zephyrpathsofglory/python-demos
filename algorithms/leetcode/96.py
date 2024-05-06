"""
https://leetcode.cn/problems/unique-binary-search-trees/description/

给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的
二叉搜索树的种数。

给定一个有序序列 1⋯n，为了构建出一棵二叉搜索树，我们可以遍历每个数字 i，将该数字作为
树根，将 1⋯(i−1) 序列作为左子树，将 (i+1)⋯n 序列作为右子
树。接着我们可以按照同样的方式递归构建左子树和右子树。

"""


class Solution:
    def num_trees(self, n: int) -> int:
        states = [0] * (n + 1)
        states[0], states[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                states[i] += states[j - 1] * states[i - j]

        return states[n]


assert Solution().num_trees(3) == 5

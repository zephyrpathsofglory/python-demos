"""
https://www.hello-algo.com/chapter_dynamic_programming/edit_distance_problem/#1

输入两个字符串 s和t，返回将 s 转换 t 为所需的最少编辑步数。

你可以在一个字符串中进行三种编辑操作：插入一个字符、删除一个字符、将字符替换为任意一个字符。

eg:
将 kitten 转换为 sitting 需要编辑 3 步，包括 2 次替换操作与 1 次添加操作；将 hello 转换为 algo 需要 3 步，包括 2 次替换操作和 1 次删除操作。
"""


class Solution:
    def edit_distance_dp(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i][j - 1]: insert
                    # dp[i - 1][j]: delete
                    # dp[i - 1][j - 1]: update
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[n][m]


assert Solution().edit_distance_dp("hello", "algo") == 3
assert Solution().edit_distance_dp("kitten", "sitting") == 3

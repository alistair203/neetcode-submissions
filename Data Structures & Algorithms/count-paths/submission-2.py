class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        for j in range(m):
            for i in range(n):
                if i > 0:
                    dp[i] += dp[i - 1]
        return dp[n - 1]
        
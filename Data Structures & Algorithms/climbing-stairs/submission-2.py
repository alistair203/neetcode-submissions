class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for k in range(2, n):
            dp[k] = dp[k - 1] + dp[k - 2]
        return dp[n - 1]
        
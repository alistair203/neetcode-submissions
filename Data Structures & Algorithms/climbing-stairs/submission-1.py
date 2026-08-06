class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        if n == 1:
            return 1
        dp[0], dp[1] = 1, 2
        def rec(k):
            if dp[k - 1] > 0:
                return dp[k - 1]
            res = rec(k - 1) + rec(k - 2)
            dp[k - 1] = res
            return res
        return rec(n)
        
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [101] * (len(cost) + 1)
        dp[0], dp[1] = 0, 0
        for k in range(2, len(cost) + 1):
            dp[k] = min(dp[k - 1] + cost[k - 1], dp[k - 2] + cost[k - 2])
        return dp[len(cost)]
        
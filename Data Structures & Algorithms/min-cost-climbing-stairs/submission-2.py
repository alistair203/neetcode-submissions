class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for k in range(2, len(cost) + 1):
            a, b = b, min(b + cost[k - 1], a + cost[k - 2])
        return b
        
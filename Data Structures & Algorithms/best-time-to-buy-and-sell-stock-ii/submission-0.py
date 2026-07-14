class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        differences = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        return sum([d for d in differences if d > 0])
        
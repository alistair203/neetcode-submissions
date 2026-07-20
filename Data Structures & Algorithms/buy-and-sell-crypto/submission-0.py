class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = prices[0], prices[0]
        for i in range(len(prices)):
            if prices[i] > sell:
                sell = prices[i]
                res = max(sell - buy, res)
            elif prices[i] < buy:
                buy = prices[i]
                sell = buy
        return res

        
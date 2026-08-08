class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        q = deque()
        q.appendleft(0)
        depth = 0
        while q:
            for i in range(len(q)):
                amt = q.pop()
                for c in coins:
                    if amt + c == amount:
                        return depth + 1
                    if amt + c < amount and depth + 1 < dp[amt + c]:
                        dp[amt + c] = depth + 1
                        q.appendleft(amt + c)
            depth += 1
        return dp[amount] if dp[amount] < float("inf") else -1
        

        
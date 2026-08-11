class Solution:
    def integerBreak(self, n: int) -> int:
        res = 1
        for k in range(2, n):
            q = n // k
            r = n - q * k
            res = max(res, q**(k - r) * (q + 1)**r)
        return res

        
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            time = sum([ceil(p / m) for p in piles])
            if time <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
        
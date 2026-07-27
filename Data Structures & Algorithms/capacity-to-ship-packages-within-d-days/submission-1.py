class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            time = 1
            current_weight = 0
            for i in range(len(weights)):
                if current_weight + weights[i] > capacity:
                    current_weight = weights[i]
                    time += 1
                    if time > days:
                        return False
                else:
                    current_weight += weights[i]
            return True
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            if can_ship(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

        
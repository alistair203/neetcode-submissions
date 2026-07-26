class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        curmax = 0
        for i in range(n):
            curmax = max(height[i], curmax)
            max_left[i] = curmax
        curmax = 0
        for i in range(n):
            curmax = max(height[n - i - 1], curmax)
            max_right[n - i - 1] = curmax
        res = 0
        for i in range(1, n - 1):
            space = min(max_left[i - 1], max_right[i + 1])
            res += max(space - height[i], 0)
        return res
        




        
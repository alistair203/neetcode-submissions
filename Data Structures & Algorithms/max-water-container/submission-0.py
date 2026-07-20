class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                water = min(heights[i], heights[j]) * (j - i)
                res = max(res, water)
        return res        
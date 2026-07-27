class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while True:
            m = (l + r) // 2
            if m == r:
                min_idx = m
                break
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            adj_m = (m + min_idx) % n
            if nums[adj_m] == target:
                return adj_m
            if nums[adj_m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
            
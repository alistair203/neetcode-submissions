class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while True:
            m = (l + r) // 2
            if m == r:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
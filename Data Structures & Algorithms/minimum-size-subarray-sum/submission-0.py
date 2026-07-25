class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        l, r = 0, 0
        res = len(nums)
        window_sum = nums[0]
        while l <= r and r < len(nums):
            if window_sum < target:
                if r == len(nums) - 1:
                    break
                r += 1
                window_sum += nums[r]
            else:
                res = min(res, r - l + 1)
                window_sum -= nums[l]
                l += 1
        return res
        
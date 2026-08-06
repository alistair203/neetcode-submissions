class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = [0] * len(nums)
        didnt_rob = [0] * len(nums)
        robbed[0] = nums[0]
        for i in range(1, len(nums)):
            robbed[i] = max(didnt_rob[i - 1] + nums[i], robbed[i - 1])
            didnt_rob[i] = max(didnt_rob[i - 1], robbed[i - 1])
        return max(robbed[len(nums) - 1], didnt_rob[len(nums) - 1])
        
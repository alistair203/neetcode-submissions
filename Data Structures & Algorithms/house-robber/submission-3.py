class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = nums[0]
        didnt_rob = 0
        for i in range(1, len(nums)):
            robbed, didnt_rob = max(didnt_rob + nums[i], robbed), max(didnt_rob, robbed)
        return max(robbed, didnt_rob)
        
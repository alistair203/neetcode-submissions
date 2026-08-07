class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        robbed, didnt_rob = nums[0], 0
        for i in range(1, len(nums) - 1):
            robbed, didnt_rob = max(didnt_rob + nums[i], robbed), max(robbed, didnt_rob)
        res1 = max(robbed, didnt_rob)
        robbed, didnt_rob = nums[1], 0
        for i in range(2, len(nums)):
            robbed, didnt_rob = max(didnt_rob + nums[i], robbed), max(robbed, didnt_rob)
        return max(res1, max(robbed, didnt_rob))
        
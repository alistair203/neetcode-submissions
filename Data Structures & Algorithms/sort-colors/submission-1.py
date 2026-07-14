class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counts = {0:0, 1:0, 2:0}
        for num in nums:
            counts[num] += 1
        nums[0: counts[0]] = [0] * counts[0]
        nums[counts[0]: counts[0] + counts[1]] = [1] * counts[1]
        nums[counts[0] + counts[1]: counts[0] + counts[1] + counts[2]] = [2] * counts[2]
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, p2 = 0, 1
        k = 1
        if len(nums) == 1:
            return k
        while p2 < len(nums):
            while p2 < len(nums) and nums[p1] == nums[p2]:
                nums.pop(p2)
            p1 = p2
            p2 = p1 + 1
            k += 1
        i = 0
        return k


        
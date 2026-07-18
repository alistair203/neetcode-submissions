class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, p2 = 0, 1
        k = 1
        n = len(nums)
        if n == 1:
            return k
        removed_indices = []
        while p2 < n:
            while p2 < n and nums[p1] == nums[p2]:
                nums[p2] = -101
                removed_indices.append(p2)
                p2 += 1
            p1 = p2
            p2 = p1 + 1
            k += 1
        i = 0
        while i < len(nums):
            if nums[i] == -101:
                nums.pop(i)
            else:
                i += 1
        return k


        
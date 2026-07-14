class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Save indices of values to remove 
        indices = [] 
        for i in range(len(nums)):
            if nums[i] == val: 
                indices.append(i)

        # Loop backwards to remove vals
        for i in sorted(indices, reverse = True):
            del nums[i]

        return len(nums)

        
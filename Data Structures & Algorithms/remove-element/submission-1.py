class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Save indices of values to remove 
        indices = [] 
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                del nums[i]

        return len(nums)

        
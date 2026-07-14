class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_unique = []
        for num in nums:
            if num in num_unique: 
                return True 
            num_unique.append(num)
        return False



        
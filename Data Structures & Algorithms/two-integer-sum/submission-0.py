class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} 
        for i in range(len(nums)): 
            for key, value in dict.items(): 
                if value == nums[i]: 
                    return [key, i]
            dict[i] = target - nums[i]
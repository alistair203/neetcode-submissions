class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} # value : index
        for i in range(len(nums)):
            diff = target - nums[i]
            if dict.get(diff, -1) + 1:
                return [dict[diff], i] 
            dict[nums[i]] = i



        
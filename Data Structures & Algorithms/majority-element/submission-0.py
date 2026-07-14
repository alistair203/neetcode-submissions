class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {} 
        for num in nums: 
            if num in counts: 
                counts[num] += 1 
            else: 
                counts[num] = 1

        threshold = len(nums) // 2

        for (k, v) in counts.items(): 
            if v > threshold: 
                return k   

        
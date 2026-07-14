class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {} 
        for num in nums: 
            counts[num] = 1 + counts.get(num, 0)

        threshold = len(nums) // 2

        for (k, v) in counts.items(): 
            if v > threshold: 
                return k   

        
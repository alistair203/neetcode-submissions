class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        res = []
        for k, v in counts.items():
            if v > len(nums) // 3:
                res.append(k)
        return res
        
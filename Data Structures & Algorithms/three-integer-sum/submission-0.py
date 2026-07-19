class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = set()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.add((nums[l], nums[r], nums[i]))
                    l += 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
        res = list(res)
        return [list(_) for _ in res]

        
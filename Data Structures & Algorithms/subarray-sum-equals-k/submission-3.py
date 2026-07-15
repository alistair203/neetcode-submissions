class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sums = {0:1}
        n = len(nums)
        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            res += prefix_sums.get(cur_sum - k, 0)
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
        return res

        
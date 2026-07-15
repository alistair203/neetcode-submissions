class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        solution_set = set(i + 1 for i in range(n))
        for i in range(n):
            if abs(nums[i]) in solution_set:
                if nums[abs(nums[i]) - 1] == 0:
                    nums[abs(nums[i]) - 1] = -1 * (n + 1)
                else:
                    nums[abs(nums[i]) - 1] = -1 * abs(nums[abs(nums[i]) - 1])
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return n + 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_s = sorted(nums)
        n = len(nums)
        i = 0

        longest_seq = 1
        current_seq = 1

        while i < n - 1:
            if nums_s[i] + 1 == nums_s[i + 1]:
                current_seq += 1
            elif nums_s[i] == nums_s[i + 1]:
                pass
            else:
                longest_seq = max(current_seq, longest_seq)
                current_seq = 1
            i += 1
        longest_seq = max(current_seq, longest_seq)
        return longest_seq


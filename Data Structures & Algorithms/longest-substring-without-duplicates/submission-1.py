class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx = {}
        res = 0
        L = 0
        for R in range(len(s)):
            if s[R] in last_idx:
                L = max(last_idx[s[R]] + 1, L)
            last_idx[s[R]] = R
            res = max(res, R - L + 1)
        return res


        
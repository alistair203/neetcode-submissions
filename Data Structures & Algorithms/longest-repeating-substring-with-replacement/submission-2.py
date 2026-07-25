class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = list(set(s))
        res = 1
        for c in chars:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while l <= r and r - l + 1 - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res


        
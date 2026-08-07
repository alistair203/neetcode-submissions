class Solution:
    def longestPalindrome(self, s: str) -> str:
        res1 = res2 = ""
        for i in range(len(s)):
            l = r = i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res1):
                    res1 = s[l:(r + 1)]
                l -= 1
                r += 1
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res2):
                    res2 = s[l:(r + 1)]
                l -= 1
                r += 1
        return res1 if len(res1) > len(res2) else res2
        

        
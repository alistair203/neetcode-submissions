class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        if len1 > len(s2):
            return False
        chars = {}
        for c in s1:
            chars[c] = chars.get(c, 0) + 1
        l, r = 0, len1 - 1
        window = {}
        for i in range(len1):
            window[s2[i]] = window.get(s2[i], 0) + 1
        if window == chars:
            return True
        while r < len(s2) - 1:
            if window[s2[l]] == 1:
                window.pop(s2[l])
            else:
                window[s2[l]] -= 1
            l += 1
            r += 1
            window[s2[r]] = window.get(s2[r], 0) + 1
            if window == chars:
                return True
        return False


        
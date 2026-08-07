class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        for i in range(len(s)):
            for j in reversed(range(0, i + 1)):
                if s[i] == s[j] and (i - j < 3 or dp[i - 1][j + 1]):
                    dp[i][j] = True
                    res += 1
        # print(dp)
        return res
        
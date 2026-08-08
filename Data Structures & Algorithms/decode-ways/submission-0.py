class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] == "0":
                if s[i - 2] not in ["1", "2"]:
                    return 0
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1]
                if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] in [str(j) for j in range(1, 7)]):
                    dp[i] += dp[i - 2]
        return dp[len(s)]


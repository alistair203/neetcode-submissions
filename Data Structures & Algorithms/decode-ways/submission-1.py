class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        a, b = 1, 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] in ["1", "2"]:
                    a, b = b, a
                else:
                    return 0
            else:
                temp = b
                if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] in ["1", "2", "3", "4", "5", "6"]):
                    temp += a
                a, b = b, temp
        return b
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if is_palindrome(s):
            return True
        for i in range(len(s)):
            s_removed = "".join([s[j] for j in range(len(s)) if j != i])
            if is_palindrome(s_removed):
                return True
        return False


def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

        
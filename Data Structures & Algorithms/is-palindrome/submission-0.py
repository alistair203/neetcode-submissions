class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = "".join([c for c in s if c.isalnum()])
        alnum_s = alnum_s.lower()
        l, r = 0, len(alnum_s) - 1
        while l < r:
            if alnum_s[l] != alnum_s[r]:
                return False
            l += 1 
            r -= 1
        return True
        
        
        
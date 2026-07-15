class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        skipped_l = False
        skip_l_fail = False
        while l < r:
            if s[l] != s[r]:
                if not skipped_l:
                    l_0, r_0 = l, r
                    skipped_l = True
                    l += 1
                    continue
                else:
                    skip_l_fail = True 
                    break
            l += 1
            r -= 1
        if not skip_l_fail:
            return True
        l, r = l_0, r_0 - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            


        
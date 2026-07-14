class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        def count_letters(s: str): 
            letter_list = {} 
            for i in range(len(s)): 
                if s[i] not in letter_list: 
                    letter_list[s[i]] = 1 
                else: 
                    letter_list[s[i]] += 1 
            return letter_list

        if count_letters(s) == count_letters(t):
            return True 
        return False

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from string import ascii_lowercase
        
        counts1, counts2 = {}, {}

        for char in ascii_lowercase: 
            counts1[char] = 0 
            counts2[char] = 0

        for char in s: 
            counts1[char] += 1 

        for char in t: 
            counts2[char] +=1

        return counts1 == counts2
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0 
        for i in range(len(strs[0])): 
            try:
                for str in strs: 
                    if str[i] != strs[0][i]: 
                        if l == 0: 
                            return ""
                        return strs[0][0: l]
            except IndexError:
                return strs[0][0:l]

            l += 1 

        return strs[0]


        
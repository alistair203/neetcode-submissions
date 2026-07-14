class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_letters(string): 
            letters = {} 
            for c in string:
                letters[c] = letters.get(c, 0) + 1 
            return tuple(sorted(letters.items())) 

        # dictionaries are not hashable so we use a sorted tuple instead

        letters_dictionary = [(str, count_letters(str)) for str in strs]

        output = {}   

        for key, value in letters_dictionary: 
            if value not in output: 
                output[value] = []
            output[value].append(key)

        return list(output.values())



        
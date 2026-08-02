class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        positions = {order[i]: i for i in range(len(order))}
        for i in range(len(words) - 1):
            p = 0
            word1, word2 = words[i], words[i + 1]
            while True:
                if (p < len(word1) and p >= len(word2)):
                    return False
                if (p >= len(word1) and p < len(word2)) or positions[word1[p]] < positions[word2[p]]:
                    break
                if positions[word1[p]] > positions[word2[p]]:
                    return False
                else:
                    p += 1
        return True
                

        
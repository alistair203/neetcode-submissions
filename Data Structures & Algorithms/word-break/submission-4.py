class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        stack = [0]
        bad_starts = [0] * len(s)
        while stack:
            start = stack.pop()
            if bad_starts[start]:
                continue
            test = ""
            for i in range(start, len(s)):
                test = test + s[i]
                if test in wordDict:
                    if i == len(s) - 1:
                        return True
                    stack.append(i + 1)
            bad_starts[start] = 1
        return False



        
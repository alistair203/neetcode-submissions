class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        stack = [0]
        bad_starts = set()
        while stack:
            start = stack.pop()
            if start in bad_starts:
                continue
            test = ""
            for i in range(start, len(s)):
                test = test + s[i]
                if test in wordDict:
                    if i == len(s) - 1:
                        return True
                    stack.append(i + 1)
            bad_starts.add(start)
        return False



        
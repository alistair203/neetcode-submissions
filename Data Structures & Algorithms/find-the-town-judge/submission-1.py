class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusters_count = [0] * n
        trusts_count = [0] * n
        for t in trust:
            trusts_count[t[0] - 1] += 1
            trusters_count[t[1] - 1] += 1
        for i in range(n):
            if trusters_count[i] == n - 1 and trusts_count[i] == 0:
                return i + 1
        return -1

        
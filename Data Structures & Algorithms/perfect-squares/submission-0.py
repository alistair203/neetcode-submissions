class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt, floor
        squares = [i**2 for i in range(1, floor(sqrt(n)) + 1)]
        dp = [i for i in range(n)]
        q = deque()
        q.appendleft(0)
        depth = 0
        while q:
            for i in range(len(q)):
                num = q.pop()
                for sq in squares:
                    if num + sq == n:
                        return depth + 1
                    if num + sq < n and depth + 1 < dp[num + sq]:
                        dp[num + sq] = depth + 1
                        q.appendleft(num + sq)
            depth += 1

        
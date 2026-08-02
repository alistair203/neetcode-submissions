class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        i, j = 0, 0
        row, col = len(grid), len(grid[0])
        while grid[i][j] == 0:
            i += 1
            if i == len(grid):
                i = 0
                j += 1
        q = deque()
        q.appendleft((i, j))
        visited = set()
        res = 0
        while q:
            i, j = q.pop()
            if (i, j) not in visited:
                if (not (0 <= i < row and 0 <= j < col)) or grid[i][j] == 0:
                    res += 1
                else:
                    visited.add((i, j))
                    q.appendleft((i - 1, j))
                    q.appendleft((i + 1, j))
                    q.appendleft((i, j + 1))
                    q.appendleft((i, j - 1))
        return res
        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.appendleft((i, j))
        minute = 0
        if fresh == 0:
            return 0
        while q:
            for _ in range(len(q)):
                i, j = q.pop()
                if (
                    ((i, j) not in visited) and
                    ((0 <= i < len(grid) and 0 <= j < len(grid[0]))) and
                    grid[i][j] > 0
                ):
                    if grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                    visited.add((i, j))
                    for nbr in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                        q.appendleft(nbr)
            if fresh == 0:
                return minute
            minute += 1
        return -1


        
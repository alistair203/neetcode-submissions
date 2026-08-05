class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.appendleft((i, j))
        traversed = set()
        dist = 0
        while q:
            for _ in range(len(q)):
                x, y = q.pop()
                if (
                    (0 <= x < len(grid) and 0 <= y < len(grid[0])) and
                    ((x, y) not in traversed) and 
                    grid[x][y] >= 0
                ):
                    traversed.add((x, y))
                    grid[x][y] = dist
                    for node in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        q.appendleft(node)  
            dist += 1
        return
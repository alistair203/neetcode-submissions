class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        treasures = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasures.append((i, j))
        def bfs(i, j):
            q = deque()
            traversed = set()
            q.appendleft((i, j))
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
                        if grid[x][y] >= dist:
                            grid[x][y] = dist
                            for node in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                                q.appendleft(node)  
                dist += 1
        for k in range(len(treasures)):
            i, j = treasures[k]
            bfs(i, j)

        return
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        to_traverse = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    to_traverse.add((i, j))
        q = deque()
        res = 0
        while to_traverse:
            q.appendleft(to_traverse.pop())
            area = 1
            while q:
                i, j = q.pop()
                for coord in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if coord in to_traverse:
                        area += 1
                        q.appendleft(coord)
                        to_traverse.remove(coord)
            res = max(res, area)
        return res
        
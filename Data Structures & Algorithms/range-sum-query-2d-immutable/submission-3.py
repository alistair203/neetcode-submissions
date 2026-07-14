class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = defaultdict(int)
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                self.sums[(i, j)] = matrix[i][j] + self.sums[(i - 1, j)] + self.sums[(i, j - 1)] - self.sums[(i - 1, j - 1)]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sums[(row2, col2)] 
            - self.sums[(row1 - 1, col2)] 
            - self.sums[(row2, col1 - 1)]
            + self.sums[(row1 - 1, col1 - 1)]
        )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
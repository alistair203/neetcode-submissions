class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            m = (l + r) // 2
            i, j = (m // n, m - (m // n) * n)
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                l = m + 1
            else:
                r = m - 1
        return False
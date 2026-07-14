class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{i: 0 for i in range(9)} for _ in range(9)]
        cols = [{i: 0 for i in range(9)} for _ in range(9)]
        boxes = {(a, b): {i:0 for i in range(9)} for a in range(3) for b in range(3)}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                v = int(board[i][j]) - 1
                rows[i][v] += 1
                cols[j][v] += 1
                box = (i // 3, j // 3)
                boxes[box][v] += 1
                if (
                    rows[i][v] > 1
                    or cols[j][v] > 1
                    or boxes[box][v] > 1
                ):
                    return False
        return True

        
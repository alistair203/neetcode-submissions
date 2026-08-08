class Solution:
    def solve(self, board: List[List[str]]) -> None:
        to_traverse = set((i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 'O')
        while to_traverse:
            stack = [to_traverse.pop()]
            region = []
            surrounded = True
            while stack:    
                i, j = stack.pop()
                region.append((i, j))
                if i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]:
                    surrounded = False
                for n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if n in to_traverse:
                        to_traverse.remove(n)
                        stack.append(n)
                        region.append(n)
            if surrounded:
                for node in region:
                    i, j = node
                    board[i][j] = 'X'

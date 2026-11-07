class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # nine_seen = set() # stores numbers seen when checking a row, col, or cell

        cell_coors: list[tuple] = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        for i in range(9):
            nine_seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in nine_seen:
                        return False
                    else:
                        nine_seen.add(board[i][j])

        for i in range(9):
            nine_seen = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in nine_seen:
                        return False
                    else:
                        nine_seen.add(board[j][i])


        for cell in cell_coors:
            nine_seen = set()
            for coor in cell_coors:
                i = cell[0] * 3 + coor[0]
                j = cell[1] * 3 + coor[1]
                if board[j][i] != ".":
                    if board[j][i] in nine_seen:
                        return False
                    else:
                        nine_seen.add(board[j][i])

        
        return True
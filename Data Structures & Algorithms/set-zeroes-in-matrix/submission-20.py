class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        

        wipe_row: bool = False
        wipe_col: bool = False

        # 0 1
        # 1 1 

        if matrix == [[0,1],[1,1]]:
            print_out = True


        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                wipe_col = True
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                wipe_row = True

        if matrix[0][0] == 0:
            wipe_col, wipe_row = True, True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # purge cols
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        

        if wipe_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if wipe_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

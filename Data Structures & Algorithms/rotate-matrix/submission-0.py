class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        for i in range(len(matrix)):
            for j in range(len(matrix) - i):
                matrix[i][j], matrix[-1-j][-1-i] = matrix[-1-j][-1-i], matrix[i][j]

        for i in range(len(matrix) // 2):
            for j in range(len(matrix)):
                matrix[i][j], matrix[-1-i][j] = matrix[-1-i][j], matrix[i][j]

        # vertical flip
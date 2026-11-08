class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_matrix = len(matrix) * len(matrix[0])

        l = 0
        r = len_matrix


        while r > l:
            m = (l + r) // 2

            if matrix[m // len(matrix[0])][m % len(matrix[0])] == target:
                return True
            elif matrix[m // len(matrix[0])][m % len(matrix[0])] < target:
                l = m + 1
            else: # >
                r = m

        return False
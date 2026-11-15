class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sequence = []
        # inclusive boundaries
        wall_right = len(matrix[0]) - 1
        wall_left = 0
        wall_top = 1
        wall_bottom = len(matrix) - 1

        if len(matrix[0]) == 1:
            direction = (1, 0)
        else:
            direction = (0, 1) # y, x

        y, x = 0, 0
        for i in range(len(matrix) * len(matrix[0])):
            sequence.append(matrix[y][x])
            y += direction[0]
            x += direction[1]

            # check if hit wall
            if x == wall_right and direction == (0, 1):
                direction = (1, 0)
                wall_right -= 1
            elif y == wall_bottom and direction == (1, 0):
                direction = (0, -1)
                wall_bottom -= 1
            elif x == wall_left and direction == (0, -1):
                direction = (-1, 0)
                wall_left += 1
            elif y == wall_top and direction == (-1, 0):
                direction = (0, 1)
                wall_top += 1

        return sequence
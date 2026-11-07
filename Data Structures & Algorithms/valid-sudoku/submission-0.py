def is_valid(row: list) -> bool:
    nums = [0] * 9
    for i in row:
        if i != ".":
            if nums[int(i) - 1] == 1:
                return False
            nums[int(i) - 1] = 1
    return True

def slice_square(square: List[List[str]], 
    left: int, right:int, up:int, down:int
    ) -> list:
    horizontal_crop = square[up: down]

    vertical_crop = [x[left:right] for x in horizontal_crop]

    flattened_list = []
    for i in vertical_crop:
        flattened_list.extend(i)

    return flattened_list


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not is_valid(row):
                return False

        for col in range(len(board[0])):
            if not is_valid([x[col] for x in board]):
                return False

        for y_idx in (0, 3, 6):
            for x_idx in (0, 3, 6):
                if not is_valid(slice_square(board, x_idx, x_idx + 3, y_idx, y_idx + 3)):
                    return False
        

        return True
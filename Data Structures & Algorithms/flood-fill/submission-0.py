from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        old_color = image[sr][sc]
        new_color = color

        if old_color == new_color:
            return image

        pixel_queue = deque([(sr, sc)])

        while pixel_queue:
            r, c = pixel_queue.popleft()
            image[r][c] = new_color
            if r+1 < len(image) and image[r+1][c] == old_color:
                pixel_queue.append((r+1, c))
            if r-1 >= 0 and image[r-1][c] == old_color:
                pixel_queue.append((r-1, c))
            if c+1 < len(image[0]) and image[r][c+1] == old_color:
                pixel_queue.append((r, c+1))
            if c-1 >= 0 and image[r][c-1] == old_color:
                pixel_queue.append((r, c-1))
            # 

        return image
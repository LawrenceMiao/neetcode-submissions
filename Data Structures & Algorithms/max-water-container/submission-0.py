class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer1 = 0
        pointer2 = 1
        best_volume = -1
        end = len(heights) - 1
        while True:
            volume = (pointer2 - pointer1) * min(heights[pointer1], heights[pointer2])
            if volume > best_volume:
                best_volume = volume
            pointer2 += 1
            if pointer2 > end:
                pointer1 += 1
                pointer2 = pointer1 + 1
            if pointer2 > end:
                return best_volume
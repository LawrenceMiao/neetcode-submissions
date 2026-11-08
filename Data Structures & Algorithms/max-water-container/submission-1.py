class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_volume = -1

        l = 0
        r = len(heights) - 1

        while True:
            volume = min(heights[l], heights[r]) * (r - l)
            best_volume = max(volume, best_volume)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            if l > r:
                break




        return best_volume
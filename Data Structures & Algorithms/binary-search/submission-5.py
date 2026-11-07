class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while True:
    
            middle = left + ((right - left) // 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                if left == middle:
                    return -1
                left = middle
            else:
                if right == middle:
                    return -1
                right = middle
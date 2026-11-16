class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        
        m = 0
        while r > l:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else: # m > target:
                r = m
        if nums[m] < target:
            return m+1

        return m

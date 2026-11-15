class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        
        highest = nums[0]
        m = 0
        while r > l:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > highest:
                highest = nums[m]
                l = m
            else:
                r = m

        pivot_idx = (m+1) % len(nums)


        l = 0
        r = len(nums)

        while r > l:
            m = (l + r) // 2
            
            if nums[(m + pivot_idx) % len(nums)] == target:
                return (m + pivot_idx) % len(nums)
            elif nums[(m + pivot_idx) % len(nums)] < target:
                l = m + 1
            else: # >
                r = m

        return -1
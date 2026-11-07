class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values: dict = {} # value -> index in nums
        
        for i, num in enumerate(nums):
            if target - num in seen_values:
                # we found it we need to return the indices
                return [seen_values[target - num], i]
            else:
                seen_values[num] = i
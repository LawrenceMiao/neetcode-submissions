class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = [0,1]
        while True:
            if nums[idx[0]] + nums[idx[1]] == target:
                return idx
            idx[1] += 1
            if idx[1] == len(nums):
                idx[0] += 1
                idx[1] = idx[0] + 1
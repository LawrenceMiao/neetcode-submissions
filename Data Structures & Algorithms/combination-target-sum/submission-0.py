class Solution:
    def __init__(self):
        self.out = []
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        self.func([], nums, target)
        return self.out

    def func(self, branches, nums, target):
        for num in nums:
            if len(branches) > 0 and num < branches[-1]:
                continue
            total = num + sum(branches)
            if total < target:
                self.func(branches + [num], nums, target)
            if total > target:
                pass
            if total == target:
                self.out.append(branches + [num])
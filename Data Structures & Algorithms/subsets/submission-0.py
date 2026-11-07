class Solution:
    def populateOut(self, out, nums, containing):
        if len(nums) == 1:
            out.append(containing + [nums[0]])
            out.append(containing)
            return None
        self.populateOut(out, nums[1:], containing + [])
        self.populateOut(out, nums[1:], containing + [nums[0]])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        self.populateOut(out, nums, [])
        return out

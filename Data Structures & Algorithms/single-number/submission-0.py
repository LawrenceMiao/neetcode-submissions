class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for i in nums:
            out ^= i

        return out
class Solution:
    def find(self, offset, array, value):
        for i in range(len(array)):
            if array[i] == value:
                return i + offset
        return -1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first = nums[i]
            target_second = target - first
            target_second_index = self.find(i + 1, nums[i+ 1:], target_second)
            if target_second_index != -1:
                return [i, target_second_index]
                
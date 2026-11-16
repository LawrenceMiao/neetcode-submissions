class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer = 0

        while nums[zero_pointer] != 0:
            zero_pointer += 1
            if zero_pointer == len(nums):
                return None

        num_pointer = zero_pointer

        while num_pointer < len(nums):
            while nums[num_pointer] == 0:
                num_pointer += 1
                if num_pointer == len(nums):
                    return None

            nums[zero_pointer], nums[num_pointer] = nums[num_pointer], nums[zero_pointer]

            zero_pointer += 1
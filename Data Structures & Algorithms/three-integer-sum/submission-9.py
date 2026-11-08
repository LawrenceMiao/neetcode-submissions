class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(nlogn)

        triplets = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]

            while l < r:
                Sum = nums[l] + nums[r]
                if Sum == target:
                    triplets.append((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif Sum > target:
                    r -= 1
                elif Sum < target:
                    l += 1


        return triplets
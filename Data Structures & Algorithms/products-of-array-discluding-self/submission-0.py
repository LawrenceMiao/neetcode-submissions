class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct: list[int] = []
        rightProduct: list[int] = []

        rightProduct.append(1)
        for i in reversed(nums):
            rightProduct.append(rightProduct[-1] * i)
        rightProduct.pop()

        leftProduct.append(1)
        for i in nums:
            leftProduct.append(leftProduct[-1] * i)
        leftProduct.pop()

        for i in range(len(leftProduct)):
            leftProduct[i] *= rightProduct[-1 - i]
        


        return leftProduct
        

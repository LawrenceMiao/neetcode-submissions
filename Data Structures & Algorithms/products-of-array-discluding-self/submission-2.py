class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # len(nums)

        leftProduct = [1]
        rightProduct = [1]
        product = []

        for i in range(len(nums) - 1):
            leftProduct.append(leftProduct[-1] * nums[i])

        for i in range(len(nums) - 1, 0, -1):
            rightProduct.append(rightProduct[-1] * nums[i])
            
        for i in range(len(nums)):
            product.append(leftProduct[i] * rightProduct[len(nums) - i - 1])

        

        return product
        

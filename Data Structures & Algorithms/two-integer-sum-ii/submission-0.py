class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1 

        while True:
            Sum = numbers[index1] + numbers[index2]
            if Sum == target:
                break
            if Sum < target: 
                index1 += 1
            else: # Sum > target
                index2 -= 1



        return [index1 + 1, index2 + 1]
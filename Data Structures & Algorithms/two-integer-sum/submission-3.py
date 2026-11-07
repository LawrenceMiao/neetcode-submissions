class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, v in enumerate(nums):
            diff = target - v

            if diff in visited:
                return sorted([i, visited[diff]])
            visited[v] = i
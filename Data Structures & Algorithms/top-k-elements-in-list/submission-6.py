from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        bucket_list = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freq_map[num] += 1

        for value, frequency in freq_map.items():
            bucket_list[frequency].append(value)

        top_k_list = []

        # print(bucket_list)

        for bucket in reversed(bucket_list):
            for value in bucket:
                top_k_list.append(value)

                if len(top_k_list) == k:
                    return top_k_list
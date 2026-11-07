class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        frequency_table = [[] for i in nums] # list of lists
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        for number, frequency in frequency_map.items():
            frequency_table[frequency -1 ].append(number)

        out = []
        for i in reversed(frequency_table):
            while len(i) > 0:
                out.append(i.pop())
                if len(out) == k:
                    return out


        
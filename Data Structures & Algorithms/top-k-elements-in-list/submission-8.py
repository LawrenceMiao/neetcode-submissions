from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num2freq = defaultdict(int)

        freq2num: list = [[] for i in range(len(nums) + 1)]

        for num in nums:
            num2freq[num] += 1

        for num, freq in num2freq.items():
            freq2num[freq].append(num)

        # print(num2freq.items())
        # print(freq2num)

        topk = []
        i = len(freq2num) - 1
        while k > 0:
            if freq2num[i] is not []:
                for num in freq2num[i]:
                    topk.append(num)
                    k -= 1
                    if k <= 0:
                        break
            i -= 1
        # print(topk)

        return topk


        
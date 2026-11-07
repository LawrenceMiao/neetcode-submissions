class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        s = sorted(counts.items(), key=lambda x:x[1])
        for i in range(k):
            out.append(s[-1 - i][0])
        return out
        
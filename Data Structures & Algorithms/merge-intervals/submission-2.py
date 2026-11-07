class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        newList = []

        mergedInterval = intervals[0]
        for i in range(len(intervals) - 1):
            
            if mergedInterval[1] >= intervals[i + 1][0]:
                mergedInterval = [mergedInterval[0], max(intervals[i + 1][1], mergedInterval[1]) ]
            else: # < start
                newList.append(mergedInterval)
                mergedInterval = intervals[i + 1]

        newList.append(mergedInterval)

        return newList
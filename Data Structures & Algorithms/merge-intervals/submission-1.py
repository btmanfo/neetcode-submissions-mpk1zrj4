class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        res = []
        intervals.sort(key= lambda x: x[0])
        newIntervals = [intervals[0][0], intervals[0][1]]
        n = len(intervals)

        while i< n:
            if intervals[i][0] <= newIntervals[1]:
                newIntervals[0] = min(newIntervals[0], intervals[i][0])
                newIntervals[1] = max(newIntervals[1], intervals[i][1])
                i+=1
            else:
                res.append(newIntervals)
                newIntervals = intervals[i]
                i+=1
        res.append(newIntervals)
        return res
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervalTable = []
        for i in intervals:
            intervalTable.append([i.start, i.end])
        if len(intervalTable) == 0:
            return True
        heapq.heapify(intervalTable)
        start, end = heapq.heappop(intervalTable)
        print(intervalTable)
        while len(intervalTable) > 0:
            newStart, newEnd = heapq.heappop(intervalTable)
            if end > newStart:
                return False
            start = newStart
            end = newEnd
        # for i in range(1, len(intervalTable)):
        #     if intervalTable[i-1][1] > intervalTable[i][0]:
        #         return False
        return True
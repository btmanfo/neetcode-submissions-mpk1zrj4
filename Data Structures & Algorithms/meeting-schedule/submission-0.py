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
        for i in range(1, len(intervalTable)):
            if intervalTable[i-1][1] > intervalTable[i][0]:
                return False
        return True
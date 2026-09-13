"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key = lambda x : (x.start, x.end) )

        for i in range(n-1):
            cur, nxt = intervals[i], intervals[i+1]
            if nxt.start < cur.end:
                return False
        
        return True
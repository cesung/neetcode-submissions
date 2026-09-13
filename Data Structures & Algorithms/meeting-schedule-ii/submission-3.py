"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0 or n == 1:
            return n

        intervals.sort(key = lambda x : (x.start, x.end))

        min_heap = [intervals[0].end]
        num_rooms = 1

        for i in range(1, n):
            while (
                min_heap and 
                intervals[i].start >= min_heap[0]
            ):
                heapq.heappop(min_heap)
            if (
                min_heap and 
                intervals[i].start < min_heap[0] and
                len(min_heap) == num_rooms
            ):
                    num_rooms += 1
            heapq.heappush(min_heap, intervals[i].end)

        return num_rooms
                


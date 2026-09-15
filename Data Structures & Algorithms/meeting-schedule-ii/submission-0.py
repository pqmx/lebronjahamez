"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)
        rooms = []


        for i in intervals:
            start, end = i.start, i.end
            
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, end)

        return len(rooms)
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        lastEnd = None
        for interval in intervals:
            if interval.start > interval.end:
                return False
            if lastEnd and (interval.start < lastEnd and interval.end > lastStart):
                return False
            lastStart = interval.start
            lastEnd = interval.end
            
        return True


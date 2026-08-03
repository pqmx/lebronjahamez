"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        max = 0

        for i in intervals:
            if i.start >= max:
                max = i.end
            else:
                return False
        return True
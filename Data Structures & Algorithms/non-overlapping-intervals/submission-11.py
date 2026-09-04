class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        removals = 0
        prevEnd = float("-inf")

        for start, end in intervals:
            if start < prevEnd:
                removals += 1
            else:
                prevEnd = end

        return removals
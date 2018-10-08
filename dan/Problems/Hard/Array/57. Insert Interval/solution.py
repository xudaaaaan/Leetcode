# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    #Binary search
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        l, r = 0, len(intervals) - 1
        pos = -1
        start, end = newInterval.start, newInterval.end
        while l <= r:
            mid = (l + r) / 2
            if intervals[mid].start == start:
                pos = mid
                break
            elif intervals[mid].start < start:
                l = mid + 1
            else:
                r = mid - 1
        if pos == -1:
            pos = l
            if pos == 0 and intervals[pos].start > end:
                return [newInterval] + intervals
            elif pos and intervals[pos - 1].end >= start:
                pos -= 1       
        res = intervals[:pos]
        while pos < len(intervals) and end >= intervals[pos].start:
            start = min(intervals[pos].start,start)
            end = max(intervals[pos].end, end)
            pos += 1   
        res.append([start, end])
        return res if pos >= len(intervals) else res + intervals[pos:]
    
   

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key = lambda x: x.start)
        second = intervals[0]
        res = [second]
        for i in range(1, len(intervals)):
            first, second = res[-1], intervals[i]
            if second.start <= first.end:
                res[-1] = Interval(first.start, max(second.end, first.end))
            else:
                res.append(second)
        return res

           
        
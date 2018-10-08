import heapq
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x: x.start)
        available = []
        for i in intervals:
            if not available or available[0] > i.start:
                heapq.heappush(available, i.end)
            else:
                heapq.heappushpop(available, i.end)
        return len(available)
            
            
        
        

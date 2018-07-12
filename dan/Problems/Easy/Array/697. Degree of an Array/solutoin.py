from collections import Counter
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin, end = {}, {}
        for i, v in enumerate(nums):
            begin.setdefault(v, i)
            end[v] = i
        c = Counter(nums)
        degree = sorted(list(c.values()))[-1]
        return min([end[v] - begin[v] + 1 for v in c if c[v] == degree])

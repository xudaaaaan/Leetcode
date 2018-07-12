# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion1(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while True:
            if l == r:
                return l
            m = (l + r) // 2
            mres = isBadVersion(m)
            if not mres:
                l = m + 1
            elif m == 1 or not isBadVersion(m - 1):
                return m
            else:
                r = m - 1
                
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m
        return l

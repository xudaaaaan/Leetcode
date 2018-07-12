import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = collections.Counter(nums)
        return list(zip(*sorted(c.items(), key = lambda x: x[1], reverse = True)[:k]))[0]

    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter as ct
        return [k for (k,v) in ct(nums).most_common(k)] 

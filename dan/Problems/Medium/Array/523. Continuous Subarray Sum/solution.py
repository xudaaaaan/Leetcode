class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {0:-1}
        s = 0
        for idx, n in enumerate(nums):
            s += n
            if not k == 0:
                s = s % k
            if s in d:
                if idx - d[s] > 1:
                    return True
            else:
                d[s] = idx
        return False
            

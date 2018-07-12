class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, m = 0, 0
        for ele in nums:
            if ele == 0:
                m = max(m, l)
                l = 0
            else:
                l += 1
        return max(m, l)
                
        

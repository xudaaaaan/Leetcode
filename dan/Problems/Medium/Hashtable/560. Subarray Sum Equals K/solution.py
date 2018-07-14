class Solution(object):
    #TLE
    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s == k:
                    res += 1
        return res
    
    def subarraySum(self, nums, k):
        res, dic, s = 0, {0:1}, 0
        for n in nums:
            s += n
            res += dic.get(s - k, 0)
            dic[s] = dic.get(s, 0) + 1
         
        return res
        
      

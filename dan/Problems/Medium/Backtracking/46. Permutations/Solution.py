class Solution:
    #Recursion
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, permu, res):
            if not nums:
                res.append(permu)
            for i in range(len(nums)):
                helper(nums[:i] + nums[i + 1:], permu + [nums[i]], res)
        res = []
        helper(nums, [], res)
        return res
    
        
            
        

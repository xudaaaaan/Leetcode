class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, permu, res):
            if not nums:
                res.append(permu)
                return
            s = set([])
            for i in range(len(nums)):
                if nums[i] in s:
                    continue
                helper(nums[:i] + nums[i+1:], permu + [nums[i]], res)
                s.add(nums[i])
                
        res = []
        helper(nums, [], res)
        return res
        
        

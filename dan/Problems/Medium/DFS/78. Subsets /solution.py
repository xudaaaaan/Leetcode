class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(nums, 0, [])
        return self.res
        
    def dfs(self, nums, k, temp):
        if k == len(nums):
            self.res.append(temp)
            return
        else:
            self.dfs(nums, k + 1, temp)
            self.dfs(nums, k + 1, temp + [nums[k]])
            return
        

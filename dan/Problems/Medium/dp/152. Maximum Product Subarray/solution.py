class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        dp = [None for i in range(len(nums))]
        res = nums[0]
        dp[0] = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            a, b, c = dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i]
            b, s = max(a, b, c), min(a, b, c)
            dp[i] = [b, s]
            res = max(res, b)
        return res
        

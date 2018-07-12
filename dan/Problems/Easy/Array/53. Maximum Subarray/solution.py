class Solution:
   
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cursum, maxsum = nums[0], nums[0]
        for i in range(1, len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            maxsum = max(maxsum, cursum)
            
        return maxsum
            

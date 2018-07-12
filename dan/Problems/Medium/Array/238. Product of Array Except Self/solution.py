class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for _ in range(len(nums))]
        product = 1
        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]
        return res
            
 

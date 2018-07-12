class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        if k and nums:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

        return
        

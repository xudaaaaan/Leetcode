class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for ele in nums:
            if not ele == 0:
                nums[i] = ele
                i += 1
        nums[i:] = [0 for _ in range(len(nums) - i)]
            

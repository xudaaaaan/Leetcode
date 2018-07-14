class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        begin, end = 0, len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                nums[i], nums[begin] = nums[begin], nums[i]
                begin += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                i += 1

        
        
   

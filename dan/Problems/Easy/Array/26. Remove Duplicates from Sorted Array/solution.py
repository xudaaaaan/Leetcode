class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i, j = 1, 1
        for j in range(1, len(nums)):
            if nums[j] > nums[i - 1]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return i
            

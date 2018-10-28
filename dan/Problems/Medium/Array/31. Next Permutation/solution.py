class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i > -1:
            for j in range(i + 1, len(nums))[::-1]:
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        j = len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return
        

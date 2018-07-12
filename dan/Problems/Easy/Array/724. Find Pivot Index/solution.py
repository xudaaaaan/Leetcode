class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        s, t = sum(nums), 0
        for i in range(0, len(nums)):
            if t == (s - nums[i])/2:
                return i
            else:
                t += nums[i]
        return -1

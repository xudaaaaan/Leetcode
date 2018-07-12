class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, res = sorted(nums), []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            s = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == s:
                    res.append([nums[i], nums[left], nums[right]])
                    while left + 1 < len(nums) and nums[left + 1] == nums[left]:
                        left += 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < s:
                    left += 1
                else:
                    right -= 1
        return res
        
        

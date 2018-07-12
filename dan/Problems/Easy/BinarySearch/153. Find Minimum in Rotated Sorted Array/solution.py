class Solution:
    def findMin1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = nums[0]
        while nums[0] > nums[-1]:
            t = nums[-1]
            nums = nums[:-1]
        return t
        
    def findMin2(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
        mid = len(nums) // 2
        if nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]:
            return nums[mid]
        elif nums[mid] > nums[0] and nums[mid] > nums[-1]:
            return self.findMin(nums[mid + 1:])
        elif nums[mid] < nums[0] and nums[mid] < nums[-1]:
            return self.findMin(nums[:mid])
        else:
            return nums[0]
        
    def findMin(self, nums):
        l = len(nums)
        start, end = 0, l - 1
        if nums[start] <= nums[end]:
            return nums[start]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid - 1] > nums[mid] < nums[(mid + 1) % l]:
                return nums[mid]
            elif nums[mid] <= nums[end]:
                end = mid - 1
            else:
                start = mid + 1

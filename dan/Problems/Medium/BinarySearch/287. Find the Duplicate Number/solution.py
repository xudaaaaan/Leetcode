class Solution(object):
    #Sort the list and use binary search. Relationship between index and value.
    #O(nlogn) time solution
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if (mid > 0 and nums[mid] == nums[mid - 1]):
                return nums[mid]
            elif (mid < len(nums) - 1 and nums[mid] == nums[mid + 1]):
                return nums[mid]
            elif(nums[mid] <= mid):
                right = mid - 1
            else:
                left = mid + 1
        return None
    
    #O(n) time solution
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[nums[0]]
        while not slow == fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while not slow == fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
            
               

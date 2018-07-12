class Solution:
    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

    
        l, r, length = 0, len(nums) - 1, 0
        while l <= r:
            while not nums[l] == val and l < r:
                l += 1
                length += 1
            while nums[r] == val and l < r:
                r -= 1
            if l == r:
                return length if nums[l] == val else length + 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            length += 1
        return length
    
    def removeElement(self, nums, val):
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r], r = nums[r], nums[l], r - 1
            else:
                l += 1
        return r + 1
                
        
                
                
                
        

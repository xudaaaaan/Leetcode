class Solution:
    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
           
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left > right:
            return [-1, -1]
        l, r = left, mid
   
        while l <= r:
            if r - l == 1:
                if nums[l] == target:
                    res1 = l
                
                else:
                    res1 = r
                break
            if l == r:
                res1 = l
                break
            m = l + (r - l) // 2
            if nums[m] == target:
                r = m
            else:
                l = m
        l, r = mid, right
        while l <= r: 
            if r - l == 1:
                if nums[r] != target:
                    res2 = l
                    break
                else:
                    res2 = r
                    break
            if l == r:
                res2 = l
                break
            m = l + (r - l) // 2
            if nums[m] == target:
                l = m
            else:
                r = m
        return [res1, res2] 
    
    def searchRange(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target: left = mid + 1
            elif nums[mid] > target: right = mid - 1
            else:
                l = r = mid
                while l > 0 and nums[l - 1] == target: l -= 1
                while r < n - 1 and nums[r + 1] == target: r += 1
                return [l, r]
        return [-1, -1]
                    
                
        
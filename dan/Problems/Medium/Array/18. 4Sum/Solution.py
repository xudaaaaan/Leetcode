class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(nums, target, n, res, ls):
            if not nums or n < 2 or n > len(nums) or nums[0] * n > target or nums[-1] * n < target:
                return
            if n == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        res.append(ls + [nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l < r and nums[l] == nums[l - 1]:
                            l+=1
                        while l < r and nums[r] == nums[r + 1]:
                            r-=1
                        
                    elif nums[l] + nums[r] < target:
                        l+=1
                    else:
                        r-=1
            else:
                for i in range(len(nums) - n + 1):
                    if i == 0 or (i > 0 and not nums[i] == nums[i - 1]):
                        helper(nums[i + 1:], target - nums[i], n - 1, res, ls + [nums[i]])
                
    
        res = []
        helper(sorted(nums), target, 4, res, [])
        return res

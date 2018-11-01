class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            if l < r and nums[i] + nums[l] + nums[l + 1] > target:
                res.append(nums[i] + nums[l] + nums[l + 1] - target)
                continue
            elif l < r and nums[i] + nums[r] + nums[r - 1] < target:
                res.append(nums[i] + nums[r] + nums[r - 1] - target)
                continue
                          
            while l < r:
                t = nums[l] + nums[r] + nums[i]
                res.append(t - target)
                if t == target:
                    return target
                elif t > target:
                    r -= 1              
                else:
                    l += 1
        return sorted(res, key = lambda x: abs(x))[0] + target

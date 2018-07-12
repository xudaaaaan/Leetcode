class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left, res, product = 0, 0, 1
        for right in range(len(nums)):
            product *= nums[right]
            while not product < k:
                product /= nums[left]
                left += 1
            res += (right - left + 1)
        return res
                

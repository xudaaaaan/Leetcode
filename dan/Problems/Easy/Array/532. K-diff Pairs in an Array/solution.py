import collections
class Solution(object):
    def findPairs1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums, res, slow, fast = sorted(nums), [], 0, 1
        while fast < len(nums):
            if nums[fast] - nums[slow] == k:
                res.append(nums[slow])
                fast += 1
                slow += 1
            elif nums[fast] - nums[slow] < k:
                fast += 1
            else:
                if fast - slow == 1:
                    fast += 1
                    slow += 1
                else:
                    slow += 1
        return len(set(res))
    
    def findPairs(self, nums, k):
        if k == 0:
            return sum(v > 1 for v in collections.Counter(nums).values())
        elif k > 0:
            return len(set(nums) & set([x + k for x in nums]))
        else:
            return 0

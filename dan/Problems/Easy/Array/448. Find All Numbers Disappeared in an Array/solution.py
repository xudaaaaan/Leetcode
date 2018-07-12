class Solution:
    def findDisappearedNumbers1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [i for i in range(1, len(nums) + 1)]
        flag = 0
        for i in nums:
            if not res[i - 1] == 0:
                res[i - 1] = 0
                flag += 1
        return sorted(res)[flag:]
    
    def findDisappearedNumbers(self, nums):
        return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))
        

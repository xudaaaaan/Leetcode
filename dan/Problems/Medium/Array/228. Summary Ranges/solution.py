class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        prev = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - prev[-1] == 1:
                prev.append(nums[i])
            else:
                if len(prev) == 1:
                    res.append(str(prev[0]))
                else:
                    res.append(str(prev[0]) + "->" + str(prev[-1]))
                prev = [nums[i]]
        if len(prev) == 1:
            res.append(str(prev[0]))
        else:
            res.append(str(prev[0]) + "->" + str(prev[-1]))
        return res

class Solution:
    #Time limit exceed
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visit = [0 for i in range(len(nums))]
        stack = [0]
        while stack:
            pos = stack.pop()
            if pos == len(nums) - 1 or pos + nums[pos] >= len(nums) - 1:
                return True
            if nums[pos] > 0:
                for i in range(1, min(nums[pos] + 1, len(nums) - pos)):
                    if not visit[pos + i]:
                        stack.append(pos + i)
                        visit[pos + i] = 1
        return False
    #O(n)
    def canJump(self, nums):
        max_pos = 0
        for pos, step in enumerate(nums):
            if pos > max_pos:
                return False
            if pos + step >= len(nums) - 1:
                return True
            max_pos = max(max_pos, pos + step)
        return True

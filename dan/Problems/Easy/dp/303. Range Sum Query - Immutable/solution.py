class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(nums)
        self.dp = [[0] * len(nums)] * len(nums)
        if nums:
            self.dp[0][0] = nums[0]
            for m in range(1, self.size):
                self.dp[0][m] = self.dp[0][m - 1] + self.nums[m]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums:
            return 0
        return self.dp[0][j] if i == 0 else self.dp[0][j] - self.dp[0][i - 1]
       
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

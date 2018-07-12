class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1] 
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        x1 = 1
        x2 = 2
        for i in range(2, n):
            x1, x2 = x2, x1 + x2
        return x2
        

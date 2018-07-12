class Solution:
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # n * m
        if not m or not n:
            return 0
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]   



class Solution(object):
    def maximalSquare1(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for i in range(c)] for j in range(r)]
        res = 0
        for i in range(r):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                res = 1
        for j in range(c):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1:
                res = 1
        for i in range(1, r):
            for j in range(1, c):                   
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i][j] == "1" else 0
                res = max(res, dp[i][j])
        return res * res
    
    
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        r, c = len(matrix), len(matrix[0])   
        dp = [int(i) for i in matrix[0]]
        res = max(dp)
        for i in range(1, r):
            for j in range(c):
                if j == 0:
                    tmp = int(matrix[i][0])
                else:
                    tmp = min(dp[j], dp[j - 1], pre) + 1 if matrix[i][j] == "1" else 0
                pre = dp[j]
                dp[j] = tmp
                res = max(res, dp[j])
        return res * res
        

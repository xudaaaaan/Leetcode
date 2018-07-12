class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1 for j in range(i + 1)] for i in range(numRows)]
        if numRows < 3:
            return res
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

        return res
        

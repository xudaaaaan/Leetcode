class Solution(object):
    def setZeroes1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        row, col = len(matrix), len(matrix[0])
        
        def set_0(r, c):
            for j in range(col):
                if matrix[r][j]:
                    matrix[r][j] = "*"
            for i in range(row):
                if matrix[i][c]:
                    matrix[i][c] = "*"
                
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    set_0(i, j)
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
        return
   

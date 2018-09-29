class Solution(object):
    def isToeplitzMatrix1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        dic = {}
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if (i - j) not in dic:
                    dic[i - j] = matrix[i][j]
                elif not matrix[i][j] == dic[i - j]:
                    return False
        return True
    
    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if not matrix[i][j] == matrix[i+1][j+1]:
                    return False
        return True
                    
                
        

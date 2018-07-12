class Solution(object):
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n, r, c = len(matrix), len(matrix[0]), 0, len(matrix[0]) - 1
        while r < m and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        return False
    
    #divide and conquer
    def searchMatrix2(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        def helper(bi, bj, ei, ej):
            i, j = bi, bj
            while i < ei or j < ej:
                if matrix[i][j] == target:  return True
                elif matrix[i][j] < target:
                    i += 1
                    j += 1
                    if i == ei and j == ej: return False
                    if i == ei: i = bi
                    if j == ej: j = bj
                        
                else:
                    if abs(bi-ei) < 2 or abs(bj-ej) < 2: return False
                    else:
                        return helper(bi, j, i, ej) or helper(i, bj, ei, j)
            return False
        return helper(0, 0, len(matrix), len(matrix[0]))
    

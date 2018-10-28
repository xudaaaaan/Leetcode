class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        row = zip(*matrix)[0]
        l, r = 0, len(row)
        while l < r:
            mid = l + (r - l) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid
        row = l - 1
        if row < 0:
            return False
        l, r = 0, len(matrix[0])
        while l < r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid
        return False
        

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 2:
            return [1 for i in range(rowIndex + 1)]
        last = [1, 1]
        for i in range(rowIndex - 1):
            current = [1 for k in range(i + 3)]
            for k in range(1, len(current) - 1):
                current[k] = last[k - 1] + last[k]
            last = current
        return current
        

class Solution(object):
    def maxIncreaseKeepingSkyline1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        r_m = [0 for i in range(n)]
        c_m = [0 for i in range(n)]
        for i in range(n):
            m1, m2 = 0, 0
            for j in range(n):
                m1 = max(m1, grid[i][j])
                m2 = max(m2, grid[j][i])
            r_m[i] = m1
            c_m[i] = m2
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(r_m[i], c_m[j]) - grid[i][j]
        return res
    
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
        

class Solution:
    def numIslands1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        r, c, dic, res = len(grid), len(grid[0]), {}, 0
        
        def inBounds(i, j):
            return 0 <= i and i < r and 0 <= j and j < c
        
        for i in range(r):
            for j in range(c):
                flag, stack = 0, [(i, j)]
                while stack:
                    m, n = stack.pop()
                    #（m, n）在边界内，未被访问过，且其值为1
                    if inBounds(m, n) and dic.get((m, n), True) and grid[m][n] == "1":
                        dic[(m, n)] = False
                        if flag == 0:
                            res += 1
                            flag = 1
                        stack.append((m - 1, n))
                        stack.append((m + 1, n))
                        stack.append((m, n - 1))
                        stack.append((m, n + 1))
        return res
    
    def numIslands(self, grid):
        res, r, c = 0, len(grid), len(grid[0]) if grid else 0
        
        def explore(i, j):
            grid[i][j] == "-1"
            if i > 0 and grid[i - 1][j] == "1": 
                explore(i - 1, j)
            if i + 1 < r and grid[i + 1][j] == "1": 
                explore(i + 1, j)
            if j > 0 and grid[i][j - 1] == "1": 
                explore(i, j - 1)
            if j + 1 < c and grid[i][j + 1] == "1": 
                explore(i, j + 1) 
            
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1": 
                    explore(i, j)
                    res += 1
        return res
            

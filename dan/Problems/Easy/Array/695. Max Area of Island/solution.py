class Solution:
    #dfs(recursive)
    def maxAreaOfIsland1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        check, r, c = {}, len(grid), len(grid[0])
        def helper(i, j):
            if not(0 <= i < r and 0 <= j < c and check.get((i, j), True) and grid[i][j]):
                return 0
            else:
                check[(i, j)] = False
                return 1 + helper(i - 1, j) + helper(i + 1, j) + helper(i, j - 1) + helper(i, j + 1)
            
        return max([helper(i, j) for i in range(r) for j in range(c)])
    #dfs(iterative)
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        r, c, maxArea, check = len(grid), len(grid[0]), 0, {}
        for i in range(r):
            for j in range(c):
                stack, area = [(i, j)], 0
                while stack:
                    cell = stack.pop()
                    if (0 <= cell[0] < r and 0 <= cell[1] < c and check.get(cell, True) and grid[cell[0]][cell[1]]):
                        check[cell] = False
                        area += 1
                        stack.append((cell[0] - 1, cell[1]))
                        stack.append((cell[0] + 1, cell[1]))
                        stack.append((cell[0], cell[1] + 1))
                        stack.append((cell[0], cell[1] - 1))
                maxArea = max(maxArea, area)
        return maxArea
            
        
        
        
                
        
        

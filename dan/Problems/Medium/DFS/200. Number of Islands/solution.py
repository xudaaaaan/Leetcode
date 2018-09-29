class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        res = 0
        is_visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(x, y):
            for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])) or is_visited[i][j] or grid[i][j] == '0':
                    continue
                is_visited[i][j] = True
                dfs(i, j)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(i, j, is_visited[i][j], grid[i][j])
                if not is_visited[i][j] and grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
                
        
        

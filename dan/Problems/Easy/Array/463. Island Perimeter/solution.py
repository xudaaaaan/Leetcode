class Solution(object):
    #Complicated solution!!
    def islandPerimeter1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        adj_num = [0] * 5
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(x, y):
            if visited[x][y]:
                return
            visited[x][y] = 1
            adj = 0
            for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])) or grid[i][j] == 0:
                    continue
                adj += 1
                dfs(i, j)
          
            adj_num[adj] += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
                
        print(adj_num)
        return 4 * adj_num[0] + 3 * adj_num[1] + 2 * adj_num[2] + adj_num[3]
    
    #Everytime 0-1 or 1-0 change happens, there will be an edge.
    def islandPerimeter(self, grid):
        m, n = len(grid), len(grid[0])
        return sum([(i - 1 < 0 or grid[i - 1][j] == 0) +\
                   (i == m - 1 or grid[i + 1][j] == 0) +\
                   (j - 1 < 0 or grid[i][j - 1] == 0) +\
                   (j == n - 1 or grid[i][j + 1] == 0)\
                   for i in range(m)\
                   for j in range(n) if grid[i][j] == 1])
       

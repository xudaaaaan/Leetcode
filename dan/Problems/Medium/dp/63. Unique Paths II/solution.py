class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        flag = True
        for i in range(m):
            if flag and obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
                flag = False
        print(obstacleGrid)
        flag = True
        for j in range(1, n):
            if flag and obstacleGrid[0][j] == 0:
                obstacleGrid[0][j] = 1
            else:
                obstacleGrid[0][j] = 0
                flag = False
        
        print(obstacleGrid)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]



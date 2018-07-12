class Solution:
    #dfs:time limit exceeded
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth, paths = len(triangle), []
        stack = [(0, 0, triangle[0][0])]
        while stack:
            i, j, path = stack.pop()
            if i == depth - 1:
                paths.append(path)
            else:
                stack.append((i+1, j, path + triangle[i+1][j]))
                stack.append((i+1, j+1, path + triangle[i+1][j+1]))
        return min(paths)
    
    #dp:from bottom to up
    def minimumTotal2(self, triangle):
        row = len(triangle) - 1
        for i in range(row - 1, -1, -1):
            for j in range(0, len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return min(triangle[0])

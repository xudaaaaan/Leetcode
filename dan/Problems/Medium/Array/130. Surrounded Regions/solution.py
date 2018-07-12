iclass Solution:
    #dfs
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        row, colume = len(board), len(board[0])
        #visited = [[False] * colume] * row
        visited = [[False for _ in range(colume)] for _ in range(row)]
        #Traverse the board
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= colume or board[r][c] == "X" or visited[r][c]:
                return 
            visited[r][c] = True
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for i in range(row):
            if i == 0 or i == row - 1:
                for j in range(colume):
                    dfs(i,j)
            else:
                dfs(i, 0)
                dfs(i, colume - 1)
        #Traverse the whole grid
        for i in range(row):
            for j in range(colume):
                if visited[i][j] == False and board[i][j] == "O":
                    board[i][j] = "X"
        
                

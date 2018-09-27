class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #Using 2 bits. The first bit represents the current state, the second bit the next state.
        row, col = len(board), len(board[0])
        def numberOfNeighbors(r, c):
            n = 0
            for i in [r - 1, r, r + 1]:
                for j in [c - 1, c, c + 1]:
                    if (i < 0) or (i >= row) or (j < 0) or (j >= col) or (i == r and j == c):
                        continue
                    if board[i][j] & 1 == 1:
                        n += 1
            return n
        
        for r in range(row):
            for c in range(col):
                n = numberOfNeighbors(r, c)
                if n == 2:
                    board[r][c] = (board[r][c] ^ (board[r][c] >> 1)) << 1 | board[r][c]
                if n == 3:
                    board[r][c] = board[r][c] | 2
                    
        for r in range(row):
            for c in range(col):
                board[r][c] = board[r][c] >> 1
        
                    
                

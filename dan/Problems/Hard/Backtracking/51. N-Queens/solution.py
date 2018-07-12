from collections import defaultdict
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        col, left, right = defaultdict(int), defaultdict(int), defaultdict(int)
        board = [['.' for i in range(n)] for j in range(n)]
        self.dfs(n, board, -1, col, left, right)
        return self.res
    
    def dfs(self, n, board, k, col, left, right):
        """
        :type board: List[str]
        :type k: int (k queens has been in the board)
        :type res: List[List[str]]
        :type col: dict[int]
        :rtype: boolean
        """                          
        if k == n-1:
            self.res.append(["".join(board[i]) for i in range(n)])
            return
        for c in range(n):
            if not col[c] and not left[k+c+1] and not right[k+1-c]:
                board[k + 1][c] = 'Q'
                col[c] = 1
                left[k+c+1] = 1
                right[k+1-c] = 1
                self.dfs(n, board, k+1, col, left, right)
                board[k + 1][c] = '.'
                col[c] = 0
                left[k+c+1] = 0
                right[k+1-c] = 0                       
        return




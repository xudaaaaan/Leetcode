from collections import defaultdict
from collections import deque

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row, column, square, visited = defaultdict(set), defaultdict(set), defaultdict(set), deque([])
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    column[j].add(board[i][j])
                    square[3 * (i//3) + (j//3)].add(board[i][j])
                else:
                    visited.append((i, j))
        
        def dfs():
            if not visited:
                return True
            i, j = visited[0]
            for dig in ("1","2","3","4","5","6","7","8","9"):
                if not (dig in row[i]) and not (dig in column[j]) and not (dig in square[3 * (i//3) + (j//3)]):
                    board[i][j] = dig
                    row[i].add(dig)
                    column[j].add(dig)
                    square[3 * (i//3) + (j//3)].add(dig)
                    visited.popleft()
                    if dfs():
                        return True
                    else:
                        board[i][j] = "."
                        row[i].remove(dig)
                        column[j].remove(dig)
                        square[3 * (i//3) + (j//3)].remove(dig)
                        visited.appendleft((i, j))
            return False
        dfs()
                        

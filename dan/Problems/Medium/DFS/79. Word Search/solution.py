class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(word, board, visited, i, j):
                    return True
        return False
    
    def dfs(self, word, board, visited, i, j, pos = 0):
        if pos == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited.get((i, j)) or not board[i][j] == word[pos]:
            return False
        visited[(i, j)] = True
        res = self.dfs(word, board, visited,i - 1, j, pos + 1) or self.dfs(word, board, visited,i + 1, j, pos + 1) or self.dfs(word, board, visited, i, j + 1, pos + 1) or self.dfs(word, board, visited,i, j - 1, pos + 1)
        visited[(i, j)] = False
        return res
        

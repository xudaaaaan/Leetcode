class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic_r = [{},{},{},{},{},{},{},{},{}]
        dic_c = [{},{},{},{},{},{},{},{},{}]
        dic_s = [{},{},{},{},{},{},{},{},{}]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in dic_r[i]) or (board[i][j] in dic_c[j]) or (board[i][j] in dic_s[3 * (i//3) + j//3]):
                    return False
                else:
                    dic_r[i][board[i][j]] = 1
                    dic_c[j][board[i][j]] = 1
                    dic_s[3 * (i//3) + j//3][board[i][j]] = 1
        return True

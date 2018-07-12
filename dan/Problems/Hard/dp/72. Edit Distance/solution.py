
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return len(word1) or len(word2)
        len1, len2 = len(word1), len(word2)
        dp = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = dp[i][j - 1] + 1
                    delete = dp[i - 1][j] + 1
                    change = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(insert, delete, change)
        return dp[len1][len2]




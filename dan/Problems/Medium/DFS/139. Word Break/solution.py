class Solution:
    #DFS
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        records = {}
        def dfs(string, dic):
            if string == "":
                return True
            if string in records:
                return records[string]
            for i in range(len(string)):
                if string[: (i+1)] in dic:
                    records[string[: (i+1)]] = True
                    if dfs(string[(i+1):], dic):
                        return True
            records[string] = False
            return False
        
        dic = set(wordDict)
        return dfs(s, dic)
    
    #Dynamic programming
    def wordBreak(self, s, wordDict):
        dp, dic = [False] * (len(s) + 1), set(wordDict)
        dp[0] = True

        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
                    break  
        return dp[-1]
                
        
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(l, r, res, string):
            if l > r:
                return 
            if not l and not r:
                res.append(string)
                return
            if l:
                dfs(l - 1, r, res, string + "(")
            if r:
                dfs(l, r - 1, res, string + ")")
        res = []
        dfs(n, n, res, "")
        return res
        

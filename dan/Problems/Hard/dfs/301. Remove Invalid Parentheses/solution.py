class Solution1:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = set()
        um_l, um_r = 0, 0
        for i in s:
            if i == "(":
                um_l += 1
            elif i == ")":
                if um_l == 0:
                    um_r += 1
                else:
                    um_l -= 1
        
        def dfs(s, res, left, right, um_l, um_r):
            if left < right:
                return
            if len(s) == 0:
                if um_l or um_r:
                    return
                self.result.add(res)
                return
            
            if s[0] == "(":
                if um_l > 0:
                    dfs(s[1:], res, left, right, um_l-1, um_r)
                dfs(s[1:], res + s[0], left+1, right, um_l, um_r)
                
            if s[0] == ")":
                if um_r > 0:
                    dfs(s[1:], res, left, right, um_l, um_r-1)
                dfs(s[1:], res + s[0], left, right+1, um_l, um_r)
                
            else:
                dfs(s[1:], res + s[0], left, right, um_l, um_r)
            return
        
        dfs(s, "", 0, 0, um_l, um_r)
        
        return list(self.result)
            
            

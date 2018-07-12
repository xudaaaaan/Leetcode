class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        res = str(t.val)
        leftstr = self.tree2str(t.left)
        rightstr = self.tree2str(t.right)
        
        if t.left or t.right:
            res += "(%s)" % leftstr
        if t.right:
            res += "(%s)" % rightstr
            
        return res
        
            



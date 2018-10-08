class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (p and not q) or (q and not p) or (not p.val == q.val):
            return False
        a = self.isSameTree(p.left, q.left)
        b = self.isSameTree(p.right, q.right)
        return a and b

        
        

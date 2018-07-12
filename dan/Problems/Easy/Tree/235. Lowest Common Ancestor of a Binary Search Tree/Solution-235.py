# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (p.val - root.val) * (q.val - root.val) <= 0:
            return root
        if p.val > root.val:
            root = root.right
            return self.lowestCommonAncestor(root, p, q)
        else:
            root = root.left
            return self.lowestCommonAncestor(root, p, q)
        
    def lowestCommonAncestor(self, root, p, q):
        while not (p.val - root.val) * (q.val - root.val) <= 0:
            if p.val > root.val:
                root = root.right
            else:
                root = root.left
                
        return root
                

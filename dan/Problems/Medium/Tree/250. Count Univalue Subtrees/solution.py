# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def is_uni(node):
            if not node:
                return True
            if (node and not node.right and not node.left):
                self.res += 1
                return True
            f = True
            if node.left:
                f = (is_uni(node.left) and node.val == node.left.val)
            if node.right:
                f = (is_uni(node.right) and node.val == node.right.val) and f
            if f:
                self.res += 1
            return f
        is_uni(root)
        return self.res
        
        

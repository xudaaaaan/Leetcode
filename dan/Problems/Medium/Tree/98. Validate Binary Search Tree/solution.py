# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, ceiling = float('inf'), floor = float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if floor < root.val < ceiling:
            return self.isValidBST(root.left, min(ceiling, root.val), floor) and self.isValidBST(root.right, ceiling, max(floor, root.val))
        return False
       

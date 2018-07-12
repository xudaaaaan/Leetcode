# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right and s == sum:
                return True
            if node.right:
                stack.append((node.right, node.right.val + s))
            if node.left:
                stack.append((node.left, node.left.val + s))
        return False

            
        

i# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    def maxDepth(self, root):
        m, stack = 0, [(root, 1)]
        if not root:
            return 0
        while stack:
            node, d = stack.pop()
            if not node.right and not node.left:
                m = max(m, d)
            if node.right:
                stack.append((node.right , d + 1))
            if node.left:
                stack.append((node.left, d + 1 ))
        return m
                
        
            
        

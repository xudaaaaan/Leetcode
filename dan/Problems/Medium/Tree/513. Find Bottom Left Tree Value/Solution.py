# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack, leaves = [(root, 1)], []
        while stack:
            node, depth = stack.pop()
            if not node.right and not node.left:
                leaves.append((node.val, depth))
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max(leaves, key = lambda x: x[1])[0]

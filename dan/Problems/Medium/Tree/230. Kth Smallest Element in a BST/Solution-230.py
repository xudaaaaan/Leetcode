# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        i, stack = 0, []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
    
            root = stack.pop()
            i += 1
            if i == k:
                return root.val
            root = root.right
            
    def kthSmallest(self, root, k):
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return sorted(res)[k - 1]
            

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        if not root.left and not root.right:
            return float("inf")
        if root.left:
            res.append(self.getMinimumDifference(root.left))
            res.append(root.val - root.left.val)
            node = root.left
            while node.right:
                node = node.right
            res.append(root.val - node.val)
        if root.right:
            res.append(self.getMinimumDifference(root.right))
            res.append(root.right.val - root.val)
            node = root.right
            while node.left:
                node = node.left
            res.append(node.val - root.val)
            
        return min(res)
    
    def getMinimumDifference(self, root):
        def dfs(root, ls):
            if root.left:
                dfs(root.left, ls)
            ls.append(root.val)
            if root.right:
                dfs(root.right, ls)
            return ls
        ls = dfs(root, [])
        return min([abs(a - b) for a, b in zip(ls, ls[1:])])
            
        
